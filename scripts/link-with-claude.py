#!/usr/bin/env python3
"""
Add Karpathy-style cross-references using Claude API.
For each entry, ask Claude which other entries are most related.
~$0.007 per entry, ~$15 for 2,121 entries.
"""
import os, re, json, subprocess, sys

WIKI_DIR = "/sandbox/quantum-wiki"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
if not ANTHROPIC_KEY:
    try:
        ANTHROPIC_KEY = open("/sandbox/.openclaw-data/anthropic-key").read().strip()
    except:
        pass

def slugify(s):
    s = str(s).lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:60]

def load_entries():
    """Load all entries with metadata."""
    entries = []
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'scripts','public','openclaw','_templates','raw','inbox'}]
        for f in files:
            if not f.endswith('.md'): continue
            path = os.path.join(root, f)
            text = open(path).read()
            parts = text.split('---', 2)
            if len(parts) < 3: continue
            fm = parts[1]
            body = parts[2]
            title_m = re.search(r'title:\s*"(.+?)"', fm)
            summary_m = re.search(r'summary:\s*"(.+?)"', fm)
            tags_m = re.search(r'tags:\s*\[(.+?)\]', fm)
            if not title_m: continue
            entries.append({
                "id": f.replace('.md',''),
                "slug": f.replace('.md',''),
                "title": title_m.group(1),
                "summary": summary_m.group(1) if summary_m else "",
                "tags": tags_m.group(1) if tags_m else "",
                "category": os.path.basename(root),
                "path": path,
                "body": body,
                "frontmatter": fm,
            })
    return entries

def find_candidates(entry, all_entries, top_n=25):
    """Pre-filter candidates using tag/word overlap to reduce token cost."""
    target_tags = set(re.findall(r'[a-z0-9-]+', entry["tags"].lower()))
    target_words = set(re.findall(r'\b[a-z]{4,}\b', (entry["title"] + " " + entry["summary"]).lower()))
    target_words -= {'with','from','this','that','have','been','will','your','more','these','they','their','about','which','were','than','what','some','also','from','into','then','only','used','many','such','each','first','very','most','other','over'}

    scored = []
    for other in all_entries:
        if other["id"] == entry["id"]: continue
        other_tags = set(re.findall(r'[a-z0-9-]+', other["tags"].lower()))
        other_words = set(re.findall(r'\b[a-z]{4,}\b', (other["title"] + " " + other["summary"]).lower()))
        score = len(target_tags & other_tags) * 3 + len(target_words & other_words) + (2 if other["category"] == entry["category"] else 0)
        if score > 1:
            scored.append((score, other))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored[:top_n]]

def claude_pick_related(entry, candidates):
    """Ask Claude to pick 4-6 most related candidates. No web search."""
    if not candidates: return []
    if not ANTHROPIC_KEY: return []
    candidate_list = "\n".join(
        f'{i+1}. [{c["category"]}] {c["title"][:80]} — {c["summary"][:120]}'
        for i, c in enumerate(candidates)
    )
    prompt = (
        f"You're cross-linking entries in an AI knowledge wiki.\n\n"
        f"CURRENT ENTRY:\n"
        f"Title: {entry['title']}\n"
        f"Category: {entry['category']}\n"
        f"Summary: {entry['summary'][:300]}\n\n"
        f"CANDIDATES:\n{candidate_list}\n\n"
        f"Pick the 4-6 candidates MOST semantically related to the current entry. "
        f"Look for: same models/papers/people, related concepts, follow-up work, "
        f"prerequisites, or alternative approaches to the same problem.\n\n"
        f"Reply with ONLY comma-separated numbers. Example: 2,5,8,12,17\n"
        f"If less than 4 are clearly related, return just the relevant ones."
    )
    try:
        payload = json.dumps({
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 100,
            "messages": [{"role": "user", "content": prompt}]
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60", "-X", "POST", ANTHROPIC_URL,
             "-H", f"x-api-key: {ANTHROPIC_KEY}",
             "-H", "anthropic-version: 2023-06-01",
             "-H", "content-type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0: return []
        resp = json.loads(result.stdout)
        text_blocks = [b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text"]
        text = " ".join(text_blocks).strip()
        nums = re.findall(r'\b(\d+)\b', text)
        picks = []
        for n in nums[:6]:
            idx = int(n) - 1
            if 0 <= idx < len(candidates):
                picks.append(candidates[idx])
        return picks
    except Exception as e:
        print(f"    ⚠ Claude error: {e}")
        return []

def add_links_to_body(body, related):
    """Append a Related section if not already present."""
    if not related: return body
    if "## Related" in body: return body
    related_md = "\n\n## Related\n" + "\n".join(
        f'- [[{r["slug"]}|{r["title"]}]]' for r in related
    )
    if "**Source:**" in body:
        return body.replace("**Source:**", related_md + "\n\n**Source:**", 1)
    return body + related_md + "\n"

def main():
    if not ANTHROPIC_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    print(f"Loading entries...")
    entries = load_entries()
    print(f"Loaded {len(entries)} entries")

    processed = 0
    linked = 0
    skipped = 0
    for entry in entries:
        if processed >= limit: break
        # Skip if already has Related section
        if "## Related" in entry["body"]:
            skipped += 1
            continue

        candidates = find_candidates(entry, entries)
        if not candidates:
            processed += 1
            continue

        related = claude_pick_related(entry, candidates)
        if related:
            new_body = add_links_to_body(entry["body"], related)
            new_text = f"---{entry['frontmatter']}---{new_body}"
            open(entry["path"], 'w').write(new_text)
            linked += 1

        processed += 1
        if processed % 50 == 0:
            print(f"  ...{processed} processed, {linked} linked, {skipped} already had Related")

    print(f"\nDone: {linked} entries linked, {skipped} already had Related, {processed} processed")

if __name__ == "__main__":
    main()
