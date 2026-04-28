#!/usr/bin/env python3
"""
Generate embeddings for all wiki entries using Ollama's nomic-embed-text.
Stores in public/data/embeddings.json — loaded by the frontend for semantic search.
Free — runs locally on Ollama.
"""
import json, subprocess, sys, os

WIKI_DIR = "/sandbox/quantum-wiki"
ENTRIES_FILE = os.path.join(WIKI_DIR, "public/data/entries.json")
OUTPUT_FILE = os.path.join(WIKI_DIR, "public/data/embeddings.json")
CACHE_FILE = "/sandbox/.openclaw-data/embeddings-cache-quantum.json"
OLLAMA_URL = "http://host.openshell.internal:11434/api/embeddings"

def load_cache():
    try:
        return json.load(open(CACHE_FILE))
    except:
        return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    json.dump(cache, open(CACHE_FILE, 'w'))

def get_embedding(text):
    """Get embedding from Ollama nomic-embed-text."""
    try:
        payload = json.dumps({"model": "nomic-embed-text", "prompt": text})
        result = subprocess.run(
            ["curl", "-s", "--max-time", "15", "-X", "POST",
             "https://inference.local/api/embeddings",
             "-H", "Content-Type: application/json", "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        return resp.get("embedding")
    except:
        return None

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999

    entries = json.load(open(ENTRIES_FILE))["entries"]
    cache = load_cache()
    print(f"Entries: {len(entries)}, Cached: {len(cache)}")

    processed = 0
    new_embeddings = 0
    for entry in entries:
        if processed >= limit:
            break
        eid = entry["id"]
        if eid in cache:
            continue

        # Embed title + summary (concise, good for search)
        text = f"{entry.get('title', '')}. {entry.get('summary', '')}"
        embedding = get_embedding(text[:500])  # Limit input length

        if embedding:
            cache[eid] = embedding
            new_embeddings += 1

        processed += 1
        if processed % 50 == 0:
            save_cache(cache)
            print(f"  ...{processed} processed, {new_embeddings} new embeddings")

    save_cache(cache)
    print(f"\nGenerated {new_embeddings} new embeddings (total cached: {len(cache)})")

    # Build output file — compact format: {id: [float, float, ...]}
    # Only include entries that have embeddings
    output = {}
    for entry in entries:
        if entry["id"] in cache:
            # Reduce precision to save file size (768 dims * 4 chars each)
            output[entry["id"]] = [round(x, 4) for x in cache[entry["id"]]]

    json.dump(output, open(OUTPUT_FILE, 'w'))
    size_mb = os.path.getsize(OUTPUT_FILE) / 1024 / 1024
    print(f"Wrote {len(output)} embeddings to {OUTPUT_FILE} ({size_mb:.1f} MB)")

if __name__ == "__main__":
    main()
