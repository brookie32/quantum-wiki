#!/usr/bin/env python3
"""
Add Karpathy-style cross-references to wiki entries using Ollama.
For each entry, ask Ollama which other entries are related and add [[wiki-links]].
Free — uses local Ollama, not Claude API.
"""
import os, re, json, subprocess, sys

WIKI_DIR = "/sandbox/quantum-wiki"
OLLAMA_URL = "http://host.openshell.internal:11434/v1/chat/completions"

def slugify(s):
    s = str(s).lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:60]

def load_entries():
    """Load all entries with id, title, category, summary."""
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

def find_candidates_by_overlap(entry, all_entries, top_n=30):
    """Find candidate related entries using tag/category/word overlap."""
    target_tags = set(re.findall(r'[a-z0-9-]+', entry["tags"].lower()))
    target_words = set(re.findall(r'\b[a-z]{4,}\b', (entry["title"] + " " + entry["summary"]).lower()))
    target_words -= {'with','from','this','that','have','been','will','your','more','these','they','their'}

    scored = []
    for other in all_entries:
        if other["id"] == entry["id"]: continue
        other_tags = set(re.findall(r'[a-z0-9-]+', other["tags"].lower()))
        other_words = set(re.findall(r'\b[a-z]{4,}\b', (other["title"] + " " + other["summary"]).lower()))
        # Score: tag overlap (3x) + word overlap (1x) + category match (2x)
        score = len(target_tags & other_tags) * 3 + len(target_words & other_words) + (2 if other["category"] == entry["category"] else 0)
        if score > 2:
            scored.append((score, other))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [s[1] for s in scored[:top_n]]

def ask_ollama_for_links(entry, candidates):
    """Ask Ollama to pick the 3-5 most related entries from candidates."""
    if len(candidates) == 0:
        return []
    candidate_list = "\n".join(f'{i+1}. {c["title"]} ({c["category"]}) — {c["summary"][:100]}'
                                for i, c in enumerate(candidates[:20]))
    prompt = (
        f"You are linking related entries in an AI knowledge wiki.\n"
        f"CURRENT ENTRY:\n"
        f"Title: {entry['title']}\n"
        f"Summary: {entry['summary'][:300]}\n\n"
        f"CANDIDATE RELATED ENTRIES:\n{candidate_list}\n\n"
        f"Pick the 3-5 candidates MOST related to the current entry. "
        f"Reply with ONLY the numbers separated by commas. Example: 1,3,7\n"
        f"If none are clearly related, reply: NONE"
    )
    try:
        payload = json.dumps({
            "model": "gpt-oss",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-X", "POST", OLLAMA_URL,
             "-H", "Content-Type: application/json", "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0: return []
        resp = json.loads(result.stdout)
        text = resp.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        if "NONE" in text.upper(): return []
        # Extract numbers
        nums = re.findall(r'\b(\d+)\b', text)
        picks = []
        for n in nums[:5]:
            idx = int(n) - 1
            if 0 <= idx < len(candidates):
                picks.append(candidates[idx])
        return picks
    except:
        return []

def add_links_to_body(body, related):
    """Append a Related section to the body if it doesn't exist."""
    if not related: return body
    if "## Related" in body:
        return body  # already has links
    related_md = "\n\n## Related\n" + "\n".join(
        f'- [[{r["slug"]}|{r["title"]}]]' for r in related
    )
    # Insert before the **Source:** line if present
    if "**Source:**" in body:
        return body.replace("**Source:**", related_md + "\n\n**Source:**", 1)
    return body + related_md

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    print(f"Loading entries...")
    entries = load_entries()
    print(f"Loaded {len(entries)} entries")

    processed = 0
    linked = 0
    for entry in entries:
        if processed >= limit: break
        # Skip if already has Related section
        if "## Related" in entry["body"]: continue

        candidates = find_candidates_by_overlap(entry, entries)
        if not candidates: continue

        related = ask_ollama_for_links(entry, candidates)
        if related:
            new_body = add_links_to_body(entry["body"], related)
            new_text = f"---{entry['frontmatter']}---{new_body}"
            open(entry["path"], 'w').write(new_text)
            linked += 1
            if linked <= 5 or linked % 25 == 0:
                print(f"  ✓ [{linked}] {entry['title'][:50]} → {len(related)} links")

        processed += 1
        if processed % 50 == 0:
            print(f"  ...processed {processed}, linked {linked}")

    print(f"\nDone: {linked} entries linked out of {processed} processed")

if __name__ == "__main__":
    main()
