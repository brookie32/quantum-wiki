#!/usr/bin/env python3
"""
build-wiki.py
Converts all .md files in the wiki into public/data/entries.json
Run this: python3 scripts/build-wiki.py
Also called automatically by the GitHub Action on every push.
"""

import os, json, re, hashlib
from datetime import datetime, timezone
from pathlib import Path

# ── CONFIG ──────────────────────────────────────────────────────────────────
WIKI_ROOT   = Path(__file__).parent.parent          # ai-wiki/
CONTENT_DIR = WIKI_ROOT                              # where .md files live
OUTPUT_DIR  = WIKI_ROOT / "public" / "data"
OUTPUT_FILE = OUTPUT_DIR / "entries.json"

# Folders to skip entirely
SKIP_DIRS = {".git", "node_modules", "scripts", "public", ".obsidian", "templates", "_templates", "openclaw", "raw", "inbox"}

# Map folder names to display categories
# Handles both old Mac folder names and new unified Spark folder names
CATEGORY_MAP = {
    # ── New unified categories (Spark + Mac going forward) ──────────────
    "model-releases":  "model-releases",
    "research":        "research",
    "tools":           "tools",
    "local-ai":        "local-ai",
    "agents":          "agents",
    "industry":        "industry",
    "hardware":        "hardware",
    "safety":          "safety",
    "applications":    "applications",
    "tutorials":       "tutorials",
    "concepts":        "concepts",
    "people":          "people",
    "companies":       "companies",
    "syntheses":       "syntheses",
    "inbox":           "inbox",
    # ── Legacy Mac folder names (kept for backwards compatibility) ───────
    "papers":          "research",       # papers/ → research
    "models":          "model-releases", # models/ → model-releases
    "projects":        "applications",   # projects/ → applications
}

# ── FRONTMATTER PARSER ─────────────────────────────────────────────────────
def parse_frontmatter(text):
    """Extract YAML frontmatter and body from a markdown file."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1].strip()
            body   = parts[2].strip()
            for line in fm_raw.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    # Handle lists (tags: [a, b, c] or tags:\n  - a)
                    if v.startswith("[") and v.endswith("]"):
                        v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                    meta[k] = v
    return meta, body

# ── GENERATE SUMMARY ───────────────────────────────────────────────────────
def extract_summary(body, meta):
    """Pull summary from frontmatter or first non-heading paragraph."""
    if "summary" in meta and meta["summary"]:
        return meta["summary"]
    lines = body.splitlines()
    paras = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("---"):
            if paras:
                break
            continue
        paras.append(line)
    summary = " ".join(paras)
    # Strip markdown syntax
    summary = re.sub(r'\*\*(.+?)\*\*', r'\1', summary)
    summary = re.sub(r'\*(.+?)\*', r'\1', summary)
    summary = re.sub(r'`(.+?)`', r'\1', summary)
    summary = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', summary)
    return summary[:280] + ("…" if len(summary) > 280 else "")

# ── INFER CATEGORY ─────────────────────────────────────────────────────────
def infer_category(filepath, meta):
    if "category" in meta and meta["category"]:
        return meta["category"]
    parts = filepath.relative_to(CONTENT_DIR).parts
    for part in parts[:-1]:  # exclude filename
        mapped = CATEGORY_MAP.get(part.lower())
        if mapped:
            return mapped
    return "general"

# ── INFER SOURCE ──────────────────────────────────────────────────────────
def infer_source_type(url, body):
    """Infer the content source type from URL patterns."""
    u = url.lower()
    if 'x.com/' in u or 'twitter.com/' in u or 'fxtwitter.com/' in u or '(X)' in body:
        return 'x-post'
    if 'youtube.com/' in u or 'youtu.be/' in u:
        return 'youtube'
    if 'arxiv.org/' in u:
        return 'paper'
    if 'reddit.com/' in u:
        return 'reddit'
    if 'github.com/' in u or 'github.blog' in u:
        return 'github'
    return 'article'

def infer_source(meta):
    src = meta.get("source", "").lower()
    if src in ("agent", "openclaw", "bot", "auto"):
        return "agent"
    return "human"

# ── MAIN BUILD ─────────────────────────────────────────────────────────────
def build():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    seen_ids = set()

    md_files = []
    for root, dirs, files in os.walk(CONTENT_DIR):
        # Prune skip dirs
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for fname in files:
            if fname.endswith(".md") and not fname.startswith("_"):
                md_files.append(Path(root) / fname)

    for fpath in sorted(md_files):
        try:
            text = fpath.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  ⚠ skip {fpath.name}: {e}")
            continue

        meta, body = parse_frontmatter(text)

        # Skip drafts
        if str(meta.get("draft", "false")).lower() == "true":
            continue
        # Skip private entries
        if str(meta.get("private", "false")).lower() == "true":
            continue
        # Skip non-entry root files (docs, config, meta pages)
        skip_files = {"CLAUDE.md", "MAC-SETUP.md", "SPARK-SETUP-GUIDE.md",
                       "dashboard.md", "index.md", "log.md", "overview.md",
                       "README.md", "wiki-lint.sh"}
        if fpath.name in skip_files:
            continue
        # Skip files without proper frontmatter (templates with placeholder comments)
        title_check = str(meta.get("title", ""))
        summary_check = str(meta.get("summary", ""))
        if "<!--" in title_check or "<!--" in summary_check:
            continue

        # ID: use frontmatter id, or slug from filename
        entry_id = meta.get("id") or re.sub(r"[^a-z0-9-]", "-", fpath.stem.lower())
        if entry_id in seen_ids:
            # make unique
            entry_id = entry_id + "-" + hashlib.md5(str(fpath).encode()).hexdigest()[:6]
        seen_ids.add(entry_id)

        title = meta.get("title") or fpath.stem.replace("-", " ").replace("_", " ").title()
        date  = meta.get("date") or meta.get("created") or ""
        tags_raw = meta.get("tags", [])
        if isinstance(tags_raw, str):
            tags = [t.strip() for t in tags_raw.split(",") if t.strip()]
        else:
            tags = tags_raw if isinstance(tags_raw, list) else []

        # Extract internal [[wiki-links]] from body for related entries panel
        wiki_links = re.findall(r'\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]', body)
        wiki_links = list(set(
            re.sub(r'[^a-z0-9-]', '-', l.strip().lower()).strip('-')
            for l in wiki_links if l.strip()
        ))

        url_val = meta.get("url") or meta.get("source_url") or ""
        entry = {
            "id":          entry_id,
            "title":       title,
            "category":    infer_category(fpath, meta),
            "source":      infer_source(meta),
            "source_type": infer_source_type(url_val, body),
            "date":        date,
            "summary":     extract_summary(body, meta),
            "content":     body,
            "body_text":   re.sub(r'[#*`\[\]_>]+', ' ', body),
            "tags":        tags,
            "url":         url_val,
            "file":        str(fpath.relative_to(CONTENT_DIR)),
            "wiki_links":  wiki_links,
        }
        entries.append(entry)
        print(f"  ✓ {entry['source'][:1].upper()} {fpath.name} → [{entry['category']}]")

    # ── Compute bidirectional backlinks ──
    # For each entry, find which OTHER entries link to it
    backlink_map = {}  # target_id -> [source_id, source_title, source_category]
    for entry in entries:
        for target in entry.get("wiki_links", []):
            if target not in backlink_map:
                backlink_map[target] = []
            backlink_map[target].append({
                "id": entry["id"],
                "title": entry["title"],
                "category": entry["category"],
            })
    # Attach backlinks to each entry (entries that link TO this one)
    for entry in entries:
        entry["backlinks"] = backlink_map.get(entry["id"], [])

    # Sort: newest first
    entries.sort(key=lambda e: e["date"] or "0000-00-00", reverse=True)

    output = {
        "meta": {
            "buildTime":    datetime.now(timezone.utc).isoformat(),
            "totalEntries": len(entries),
            "categories":   list(set(e["category"] for e in entries)),
        },
        "entries": entries,
    }

    OUTPUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n✅ Built {len(entries)} entries → {OUTPUT_FILE}")
    return len(entries)

if __name__ == "__main__":
    print("🔨 Building wiki entries.json…")
    count = build()
    print(f"   Done. {count} entries ready for deployment.")
