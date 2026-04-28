#!/usr/bin/env python3
"""
Weekly wiki lint — finds stale entries, orphans, broken links, missing fields.
Writes report to syntheses/lint-YYYY-MM-DD.md
Runs as part of the weekly cron (Sundays at 9am).
"""
import os, re, json, sys
from datetime import datetime, timezone
from collections import defaultdict

WIKI_DIR = "/sandbox/quantum-wiki"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

def load_entries():
    """Load all entries with metadata."""
    entries = {}
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
            eid = f.replace('.md', '')
            meta = {}
            for line in fm.strip().splitlines():
                if ':' in line:
                    k, _, v = line.partition(':')
                    meta[k.strip()] = v.strip().strip('"').strip("'")
            # Extract wiki links
            wiki_links = re.findall(r'\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]', body)
            wiki_links = [re.sub(r'[^a-z0-9-]', '-', l.strip().lower()).strip('-') for l in wiki_links if l.strip()]
            entries[eid] = {
                'id': eid,
                'path': path,
                'meta': meta,
                'body': body,
                'wiki_links': wiki_links,
                'category': os.path.basename(root),
            }
    return entries

def run_lint():
    entries = load_entries()
    print(f"Loaded {len(entries)} entries")

    errors = []    # Red — broken, must fix
    warnings = []  # Yellow — stale, weak
    info = []      # Blue — suggestions

    # 1. Missing required frontmatter fields
    required = ['title', 'date', 'source', 'category', 'url', 'summary']
    for eid, e in entries.items():
        missing = [f for f in required if not e['meta'].get(f)]
        if missing:
            errors.append(f"Missing fields in `{eid}`: {', '.join(missing)}")

    # 2. Stale entries (review_by has passed)
    stale = []
    for eid, e in entries.items():
        review_by = e['meta'].get('review_by', '')
        if review_by and review_by < TODAY:
            stale.append((eid, review_by))
    for eid, date in stale:
        warnings.append(f"Stale: `{eid}` — review_by was {date}")

    # 3. Already flagged stale but not reviewed
    flagged = [(eid, e) for eid, e in entries.items() if e['meta'].get('stale') == 'true']
    for eid, e in flagged:
        warnings.append(f"Flagged stale: `{eid}` — needs human review")

    # 4. Orphan pages (no incoming links from any other entry)
    all_targets = set()
    for e in entries.values():
        all_targets.update(e['wiki_links'])
    orphans = [eid for eid in entries if eid not in all_targets]
    # Don't count concept index pages as orphans
    real_orphans = [o for o in orphans if not o.endswith('-index')]
    if len(real_orphans) > 20:
        info.append(f"Orphan pages (no incoming links): {len(real_orphans)} entries")
        info.append(f"  Sample: {', '.join(real_orphans[:10])}")
    else:
        for o in real_orphans:
            info.append(f"Orphan: `{o}` — no other entry links to this")

    # 5. Broken wiki-links (point to non-existent entries)
    broken_links = []
    for eid, e in entries.items():
        for target in e['wiki_links']:
            if target not in entries:
                broken_links.append((eid, target))
    if broken_links:
        errors.append(f"Broken wiki-links: {len(broken_links)} total")
        for src, tgt in broken_links[:20]:
            errors.append(f"  `{src}` → `{tgt}` (not found)")

    # 6. Entries with no tags
    no_tags = [eid for eid, e in entries.items() if not e['meta'].get('tags')]
    if no_tags:
        info.append(f"Entries with no tags: {len(no_tags)}")

    # 7. Categories with very few entries (possible misfiling)
    cat_counts = defaultdict(int)
    for e in entries.values():
        cat_counts[e['category']] += 1
    small_cats = [(c, n) for c, n in cat_counts.items() if n <= 2]
    for cat, count in small_cats:
        info.append(f"Small category `{cat}`: only {count} entries — possible misfiling?")

    # 8. Entries with body = title (still unfixed)
    title_only = 0
    for eid, e in entries.items():
        title = e['meta'].get('title', '').strip().rstrip('.')
        first_line = e['body'].strip().split('\n')[0].strip().rstrip('.')
        if first_line == title:
            title_only += 1
    if title_only:
        warnings.append(f"Entries with body = title only: {title_only} (need better summaries)")

    # 9. Duplicate URLs
    url_map = defaultdict(list)
    for eid, e in entries.items():
        url = e['meta'].get('url', '').strip().rstrip('/')
        if url:
            url_map[url].append(eid)
    dupes = {url: eids for url, eids in url_map.items() if len(eids) > 1}
    if dupes:
        warnings.append(f"Duplicate URLs: {len(dupes)} URLs shared by multiple entries")
        for url, eids in list(dupes.items())[:10]:
            warnings.append(f"  {url[:60]} → {', '.join(eids[:3])}")

    # Write report
    report_dir = os.path.join(WIKI_DIR, "syntheses")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"lint-{TODAY}.md")

    lines = [
        "---",
        f'title: "Wiki Lint Report — {TODAY}"',
        f'date: "{TODAY}"',
        f'updated: "{TODAY}"',
        f'source: "agent"',
        f'category: "syntheses"',
        f'tags: [lint, health-check, automated]',
        f'url: ""',
        f'summary: "Automated lint: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info"',
        f'last_verified: "{TODAY}"',
        f'review_by: "{TODAY}"',
        f'stale: false',
        "---",
        "",
        f"# Wiki Lint Report — {TODAY}",
        "",
        f"Scanned {len(entries)} entries across {len(cat_counts)} categories.",
        "",
    ]

    if errors:
        lines.append("## Errors")
        lines.append("")
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")

    if warnings:
        lines.append("## Warnings")
        lines.append("")
        for w in warnings:
            lines.append(f"- {w}")
        lines.append("")

    if info:
        lines.append("## Info")
        lines.append("")
        for i in info:
            lines.append(f"- {i}")
        lines.append("")

    if not errors and not warnings:
        lines.append("## All clear!")
        lines.append("")
        lines.append("No issues found. The wiki is healthy.")

    # Category breakdown
    lines.append("## Category Breakdown")
    lines.append("")
    for cat, count in sorted(cat_counts.items(), key=lambda x: -x[1]):
        lines.append(f"- **{cat}**: {count} entries")

    open(report_path, 'w').write("\n".join(lines))
    print(f"\nLint report written to {report_path}")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Info: {len(info)}")

if __name__ == "__main__":
    run_lint()
