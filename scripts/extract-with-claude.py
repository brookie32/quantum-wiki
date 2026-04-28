#!/usr/bin/env python3
"""
Extract named entities (models, papers, people, companies, tools) using Claude API.
~$0.004 per entry, ~$8.50 for 2,121 entries.
"""
import os, re, json, subprocess, sys
from collections import defaultdict

WIKI_DIR = "/sandbox/quantum-wiki"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
if not ANTHROPIC_KEY:
    try:
        ANTHROPIC_KEY = open("/sandbox/.openclaw-data/anthropic-key").read().strip()
    except:
        pass

CONCEPT_DIR = os.path.join(WIKI_DIR, "concepts")
CACHE_FILE = "/sandbox/.openclaw-data/concept-cache-quantum.json"

def load_cache():
    try:
        return json.load(open(CACHE_FILE))
    except:
        return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    json.dump(cache, open(CACHE_FILE, 'w'))

def claude_extract(title, summary):
    """Ask Claude to extract named entities."""
    prompt = (
        f"Extract named AI/ML entities from this wiki entry. "
        f"Return ONLY valid JSON with these arrays (no markdown, no preamble):\n"
        f'{{"models":[],"papers":[],"people":[],"companies":[],"tools":[]}}\n\n'
        f"Title: {title}\n"
        f"Summary: {summary[:400]}\n\n"
        f"Rules:\n"
        f'- models: AI model names (e.g. "GPT-5","Claude Sonnet 4.6","Llama 70B","Gemini 2","Qwen 3","DeepSeek V3")\n'
        f'- papers: arxiv paper titles or paper-style names\n'
        f'- people: researchers/founders (e.g. "Karpathy","LeCun","Sutskever","Hinton","Altman")\n'
        f'- companies: AI labs/companies (e.g. "OpenAI","Anthropic","Mistral","DeepMind","Hugging Face")\n'
        f'- tools: software tools (e.g. "Cursor","LangChain","Ollama","Vercel","Pinecone")\n'
        f"- Maximum 4 per category. Empty arrays if none.\n"
        f"- Use exact canonical names. No duplicates.\n"
        f"- Return ONLY the JSON object, nothing else."
    )
    try:
        payload = json.dumps({
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}]
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-X", "POST", ANTHROPIC_URL,
             "-H", f"x-api-key: {ANTHROPIC_KEY}",
             "-H", "anthropic-version: 2023-06-01",
             "-H", "content-type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0: return None
        resp = json.loads(result.stdout)
        text_blocks = [b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text"]
        text = " ".join(text_blocks).strip()
        # Strip markdown fences if any
        text = re.sub(r'^```(?:json)?\s*', '', text)
        text = re.sub(r'\s*```$', '', text)
        m = re.search(r'\{.*?\}', text, re.DOTALL)
        if not m: return None
        data = json.loads(m.group(0))
        return {
            "models": [str(x) for x in data.get("models", [])][:4],
            "papers": [str(x) for x in data.get("papers", [])][:4],
            "people": [str(x) for x in data.get("people", [])][:4],
            "companies": [str(x) for x in data.get("companies", [])][:4],
            "tools": [str(x) for x in data.get("tools", [])][:4],
        }
    except:
        return None

def load_entries():
    """Load all entries with metadata."""
    entries = []
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'scripts','public','openclaw','_templates','raw','inbox','concepts'}]
        for f in files:
            if not f.endswith('.md'): continue
            path = os.path.join(root, f)
            text = open(path).read()
            parts = text.split('---', 2)
            if len(parts) < 3: continue
            fm = parts[1]
            title_m = re.search(r'title:\s*"(.+?)"', fm)
            summary_m = re.search(r'summary:\s*"(.+?)"', fm)
            if not title_m: continue
            entries.append({
                "id": f.replace('.md',''),
                "title": title_m.group(1),
                "summary": summary_m.group(1) if summary_m else "",
                "category": os.path.basename(root),
                "path": path,
            })
    return entries

def slug(s):
    s = str(s).lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:50]

def build_concept_pages(concept_index):
    """Write category index pages to /concepts/."""
    os.makedirs(CONCEPT_DIR, exist_ok=True)
    for category in ["models", "papers", "people", "companies", "tools"]:
        items = concept_index[category]
        if not items: continue
        # Group entries by concept name (normalize for grouping)
        grouped = defaultdict(set)
        for concept, entry_ids in items.items():
            key = concept.strip()
            grouped[key].update(entry_ids)

        index_path = os.path.join(CONCEPT_DIR, f"{category}-index.md")
        lines = [
            "---",
            f'title: "All {category.title()}"',
            f'date: "2026-04-11"',
            f'updated: "2026-04-11"',
            f'source: "agent"',
            f'category: "concepts"',
            f'tags: [concepts, {category}, index]',
            f'url: ""',
            f'summary: "Auto-generated index of all {category} mentioned across the wiki."',
            f'last_verified: "2026-04-11"',
            f'review_by: "2026-07-11"',
            f'stale: false',
            "---",
            "",
            f"# All {category.title()}",
            "",
            f"Auto-generated index of {category} extracted from wiki entries. {len([k for k,v in grouped.items() if len(v)>=2])} {category} with 2+ mentions.",
            "",
        ]
        # Sort by mention count
        sorted_items = sorted(grouped.items(), key=lambda x: -len(x[1]))
        for concept, entry_ids in sorted_items:
            if len(entry_ids) < 2: continue
            lines.append(f"## {concept}")
            lines.append(f"*Mentioned in {len(entry_ids)} entries*")
            lines.append("")
            for eid in sorted(entry_ids)[:15]:
                lines.append(f"- [[{eid}]]")
            lines.append("")
        open(index_path, 'w').write("\n".join(lines))
        print(f"  ✓ Wrote {category}-index.md ({len([k for k,v in grouped.items() if len(v)>=2])} concepts)")

def main():
    if not ANTHROPIC_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    cache = load_cache()
    print(f"Loaded {len(cache)} cached extractions")

    entries = load_entries()
    print(f"Found {len(entries)} entries")

    concept_index = {
        "models": defaultdict(list),
        "papers": defaultdict(list),
        "people": defaultdict(list),
        "companies": defaultdict(list),
        "tools": defaultdict(list),
    }

    # Load existing extractions — ONLY for entries that belong to THIS wiki
    # (cache file is/was shared with another wiki; without this filter, indexes
    # could include entries from other wikis.)
    local_ids = {e["id"] for e in entries}
    for eid, ents in cache.items():
        if eid not in local_ids: continue
        if not ents: continue
        for cat in concept_index:
            for name in ents.get(cat, []):
                concept_index[cat][name].append(eid)

    processed = 0
    extracted = 0
    for entry in entries:
        if processed >= limit: break
        if entry["id"] in cache:
            continue

        ents = claude_extract(entry["title"], entry["summary"])
        cache[entry["id"]] = ents or {}
        if ents and any(ents.get(c) for c in concept_index):
            extracted += 1
            for cat in concept_index:
                for name in ents.get(cat, []):
                    if name and isinstance(name, str):
                        concept_index[cat][name].append(entry["id"])
        processed += 1
        if processed % 25 == 0:
            save_cache(cache)
            print(f"  ...{processed} processed, {extracted} with entities")

    save_cache(cache)
    print(f"\nExtracted entities from {extracted} entries (out of {processed} processed)")
    print("\nBuilding concept pages...")
    build_concept_pages(concept_index)

if __name__ == "__main__":
    main()
