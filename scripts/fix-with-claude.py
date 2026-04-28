#!/usr/bin/env python3
"""Fix entries with empty bodies using Claude API + web search."""
import os, re, json, subprocess, sys

WIKI_DIR = "/sandbox/quantum-wiki"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"

# Read API key from env
API_KEY = os.environ.get("ANTHROPIC_API_KEY", "").strip()
if not API_KEY:
    print("ERROR: ANTHROPIC_API_KEY not set")
    sys.exit(1)

def claude_summarize(title, source_name, url):
    """Ask Claude (with web search) to fetch and summarize a URL."""
    prompt = (
        f"Fetch this URL and write a concise 2-3 sentence factual summary "
        f"for an AI knowledge base entry. Return ONLY the summary text, no preamble.\n\n"
        f"Title: {title}\n"
        f"Source: {source_name}\n"
        f"URL: {url}"
    )
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 300,
        "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": 2}],
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60", "-X", "POST", ANTHROPIC_URL,
             "-H", f"x-api-key: {API_KEY}",
             "-H", "anthropic-version: 2023-06-01",
             "-H", "content-type: application/json",
             "-d", json.dumps(payload)],
            capture_output=True, text=True)
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        # Find the text content
        text_blocks = [b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text"]
        summary = " ".join(text_blocks).strip()
        return summary if summary and len(summary) > 30 else None
    except Exception as e:
        print(f"    ⚠ Claude error: {e}")
        return None

def main():
    fixed = 0
    skipped = 0
    total = 0
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 999999

    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'scripts','public','openclaw','_templates','raw','inbox'}]
        for f in files:
            if not f.endswith('.md') or fixed >= limit:
                continue
            path = os.path.join(root, f)
            text = open(path).read()
            parts = text.split('---', 2)
            if len(parts) < 3: continue

            frontmatter = parts[1]
            body = parts[2].strip()

            title_m = re.search(r'title:\s*"(.+?)"', frontmatter)
            url_m = re.search(r'url:\s*"(.+?)"', frontmatter)
            if not title_m or not url_m: continue

            title = title_m.group(1).strip()
            url = url_m.group(1).strip()
            first_line = body.split('\n')[0].strip().rstrip('.')

            # Strip the **Source:** footer to get just the article body
            body_only = re.sub(r'\n+\*\*Source:\*\*.*$', '', body, flags=re.DOTALL).strip()

            # Fix if body is just title OR very short (likely RSS teaser only)
            is_title_only = first_line == title.rstrip('.')
            is_too_short = len(body_only) < 200
            if not is_title_only and not is_too_short:
                continue

            total += 1
            print(f"[{total}] {f[:60]}")
            print(f"  → {url[:70]}")

            desc = claude_summarize(title, os.path.basename(root), url)

            if desc:
                short_summary = desc[:197] + "..." if len(desc) > 200 else desc
                new_frontmatter = re.sub(
                    r'summary:\s*"[^"]*"',
                    f'summary: "{short_summary.replace(chr(34), chr(39))}"',
                    frontmatter)
                new_body = f"{desc}\n\n**Source:** [{os.path.basename(root)}]({url})"
                new_text = f"---{new_frontmatter}---\n\n{new_body}\n"
                open(path, 'w').write(new_text)
                fixed += 1
                print(f"  ✓ {desc[:80]}...")
            else:
                skipped += 1
                print(f"  ✗ Skipped")

    print(f"\nDone: {fixed} fixed, {skipped} skipped, {total} processed")

if __name__ == "__main__":
    main()
