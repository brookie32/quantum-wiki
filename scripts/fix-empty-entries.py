#!/usr/bin/env python3
"""Fix entries where body just repeats the title — fetch page and summarize with Ollama."""
import os, re, json, subprocess, html as html_mod

WIKI_DIR = "/sandbox/quantum-wiki"
OLLAMA_URL = "http://host.openshell.internal:11434/v1/chat/completions"

def extract_page_text(html):
    """Extract readable text from HTML using multiple strategies."""
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            text = json.dumps(data.get("props", {}).get("pageProps", {}))
            text = re.sub(r'[{}\[\]",:]+', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 100: return text[:3000]
        except: pass
    for tag in ['article', 'main']:
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', html, re.DOTALL | re.IGNORECASE)
        if m:
            text = re.sub(r'<[^>]+>', ' ', m.group(1))
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 100: return text[:3000]
    descs = []
    for attr in ['description', 'og:description', 'twitter:description']:
        # Match content="..." or content='...' with name/property before or after content
        m = re.search(rf'<meta[^>]*(?:name|property)=["\']?{attr}["\']?[^>]*content=["\']([^"\']+)["\']', html, re.IGNORECASE)
        if not m:
            # Also match when content appears before name/property
            m = re.search(rf'<meta[^>]*content=["\']([^"\']+)["\'][^>]*(?:name|property)=["\']?{attr}["\']?', html, re.IGNORECASE)
        if m:
            desc = html_mod.unescape(m.group(1))
            descs.append(desc)
    if descs: return ' '.join(descs)[:3000]
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) > 100 and text.count('function') < 5: return text[:3000]
    return None

def fetch_and_summarize(url, title):
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "10",
             "-A", "WikiAgent/1.0 (AI Wiki; contact: rksbrooke@gmail.com)", url],
            capture_output=True, text=True)
        if result.returncode != 0 or not result.stdout.strip():
            return None
        page_text = extract_page_text(result.stdout)
        if not page_text: return None
        payload = json.dumps({
            "model": "gemma4",
            "messages": [{"role": "user", "content":
                f"Summarize this in 2-3 sentences for an AI knowledge base. Be factual and concise.\n"
                f"Title: {title}\n\nContent:\n{page_text[:2000]}"}],
            "max_tokens": 200
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-X", "POST",
             OLLAMA_URL, "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0: return None
        resp = json.loads(result.stdout)
        summary = resp.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        return summary if summary and len(summary) > 20 else None
    except:
        return None

fixed = 0
skipped = 0
for root, dirs, files in os.walk(WIKI_DIR):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d not in {'scripts','public','openclaw','_templates','raw','inbox'}]
    for f in files:
        if not f.endswith('.md'): continue
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
        
        # Check if body is just the title
        if first_line != title.rstrip('.'):
            continue
        
        print(f"Fixing: {f} — fetching {url[:50]}...")
        summary = fetch_and_summarize(url, title)
        if summary:
            # Update body and summary in frontmatter
            new_body = f"{summary}\n\n**Source:** [{os.path.basename(root)}]({url})"
            short_summary = summary[:197] + "..." if len(summary) > 200 else summary
            new_frontmatter = re.sub(
                r'summary:\s*"[^"]*"',
                f'summary: "{short_summary.replace(chr(34), chr(39))}"',
                frontmatter)
            new_text = f"---{new_frontmatter}---\n\n{new_body}\n"
            open(path, 'w').write(new_text)
            fixed += 1
            print(f"  ✓ Fixed with AI summary")
        else:
            skipped += 1
            print(f"  ✗ Could not summarize")

print(f"\nDone: {fixed} fixed, {skipped} skipped")
