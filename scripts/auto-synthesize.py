#!/usr/bin/env python3
"""
Auto-synthesis: when 5+ entries cluster around a topic, generate a synthesis page.
Uses Claude API to write the synthesis from the clustered entries.
Runs weekly after lint.
"""
import os, re, json, subprocess, sys
from collections import defaultdict

WIKI_DIR = "/sandbox/quantum-wiki"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_KEY = ""
try:
    ANTHROPIC_KEY = open("/sandbox/.openclaw-data/anthropic-key").read().strip()
except:
    ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()

TODAY = __import__('datetime').datetime.now(__import__('datetime').timezone.utc).strftime("%Y-%m-%d")

def load_entries():
    entries = []
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'scripts','public','openclaw','_templates','raw','inbox','syntheses'}]
        for f in files:
            if not f.endswith('.md'): continue
            path = os.path.join(root, f)
            text = open(path).read()
            parts = text.split('---', 2)
            if len(parts) < 3: continue
            fm = parts[1]
            title_m = re.search(r'title:\s*"(.+?)"', fm)
            summary_m = re.search(r'summary:\s*"(.+?)"', fm)
            tags_m = re.search(r'tags:\s*\[(.+?)\]', fm)
            date_m = re.search(r'date:\s*"(.+?)"', fm)
            if not title_m: continue
            entries.append({
                'id': f.replace('.md',''),
                'title': title_m.group(1),
                'summary': summary_m.group(1) if summary_m else '',
                'tags': [t.strip() for t in tags_m.group(1).split(',')] if tags_m else [],
                'date': date_m.group(1) if date_m else '',
                'category': os.path.basename(root),
            })
    return entries

def find_clusters(entries, min_size=5):
    """Find topic clusters based on tag co-occurrence."""
    # Count tag combinations
    tag_entries = defaultdict(list)
    for e in entries:
        for tag in e['tags']:
            tag = tag.strip().lower()
            if tag and len(tag) > 2:
                tag_entries[tag].append(e)

    # Filter to tags with 5+ entries
    clusters = {}
    for tag, ents in tag_entries.items():
        if len(ents) >= min_size:
            # Skip generic tags
            if tag in ('research','industry','tools','agents','safety','model-releases',
                       'local-ai','hardware','applications','tutorials','concepts',
                       'simon-willison','the-verge-ai','techcrunch-ai','ars-technica',
                       'venturebeat-ai','karpathy--x-','yann-lecun--x-'):
                continue
            clusters[tag] = ents
    return clusters

def existing_syntheses():
    """Get list of existing synthesis slugs."""
    synth_dir = os.path.join(WIKI_DIR, "syntheses")
    if not os.path.exists(synth_dir):
        return set()
    return {f.replace('.md','').replace('synthesis-','') for f in os.listdir(synth_dir) if f.endswith('.md')}

def claude_synthesize(topic, entries):
    """Ask Claude to write a synthesis page from clustered entries."""
    if not ANTHROPIC_KEY: return None
    entry_list = "\n".join(
        f'- [{e["category"]}] {e["title"]}: {e["summary"][:150]}'
        for e in entries[:15]
    )
    prompt = (
        f"Write a synthesis overview for an AI knowledge wiki on the topic: '{topic}'.\n\n"
        f"Based on these {len(entries)} related entries:\n{entry_list}\n\n"
        f"Write:\n"
        f"1. A 2-3 sentence overview of the current state of this topic\n"
        f"2. Key developments (bullet points)\n"
        f"3. Key players/companies involved\n"
        f"4. Where this is heading (brief outlook)\n\n"
        f"Be factual and concise. Use markdown formatting. Under 300 words total."
    )
    try:
        payload = json.dumps({
            "model": "claude-sonnet-4-6",
            "max_tokens": 500,
            "messages": [{"role": "user", "content": prompt}]
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60", "-X", "POST", ANTHROPIC_URL,
             "-H", f"x-api-key: {ANTHROPIC_KEY}",
             "-H", "anthropic-version: 2023-06-01",
             "-H", "content-type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0: return None
        resp = json.loads(result.stdout)
        text_blocks = [b.get("text","") for b in resp.get("content",[]) if b.get("type")=="text"]
        return " ".join(text_blocks).strip()
    except:
        return None

def slug(s):
    s = str(s).lower()
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:50]

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    entries = load_entries()
    print(f"Loaded {len(entries)} entries")

    clusters = find_clusters(entries)
    print(f"Found {len(clusters)} topic clusters with 5+ entries")

    existing = existing_syntheses()
    synth_dir = os.path.join(WIKI_DIR, "syntheses")
    os.makedirs(synth_dir, exist_ok=True)

    written = 0
    for topic, ents in sorted(clusters.items(), key=lambda x: -len(x[1])):
        if written >= limit: break
        topic_slug = f"synthesis-{slug(topic)}"
        if topic_slug in existing:
            continue

        print(f"\n  Synthesizing: {topic} ({len(ents)} entries)")
        content = claude_synthesize(topic, ents)
        if not content:
            print(f"    ✗ Failed")
            continue

        # Build entry references
        refs = "\n".join(f"- [[{e['id']}|{e['title']}]]" for e in ents[:15])

        page = f"""---
title: "Synthesis: {topic.title()}"
date: "{TODAY}"
updated: "{TODAY}"
source: "agent"
category: "syntheses"
tags: [synthesis, {topic}, auto-generated]
url: ""
summary: "Auto-generated synthesis of {len(ents)} entries about {topic}"
last_verified: "{TODAY}"
review_by: "{TODAY}"
stale: false
---

{content}

## Source Entries

{refs}
"""
        filepath = os.path.join(synth_dir, f"{topic_slug}.md")
        open(filepath, 'w').write(page)
        written += 1
        print(f"    ✓ Wrote {topic_slug}.md")

    print(f"\nDone: {written} synthesis pages written")

if __name__ == "__main__":
    main()
