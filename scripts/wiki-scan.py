#!/usr/bin/env python3
"""Wiki agent: scan RSS feeds, write markdown entries, commit and push."""

import subprocess, json, re, os, sys
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET
from html import unescape
from urllib.request import urlopen, Request
from urllib.error import URLError
import ssl

WIKI_DIR = "/sandbox/quantum-wiki"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
REVIEW_BY = (datetime.now(timezone.utc) + timedelta(days=90)).strftime("%Y-%m-%d")
CUTOFF = datetime.now(timezone.utc) - timedelta(hours=72)

# SSL context that doesn't verify (sandbox proxy terminates TLS)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

FEEDS = [
    # ══════════════════════════════════════════════════════════════════
    # TIER 1 — ACADEMIC PRE-PRINTS & PEER-REVIEWED RESEARCH
    # ══════════════════════════════════════════════════════════════════
    ("http://export.arxiv.org/rss/quant-ph",                             "papers",            "arXiv quant-ph"),
    ("http://export.arxiv.org/rss/cond-mat.quant-gas",                   "papers",            "arXiv cond-mat.quant-gas"),
    ("http://export.arxiv.org/rss/physics.atom-ph",                      "papers",            "arXiv physics.atom-ph"),
    ("https://www.nature.com/subjects/quantum-physics.rss",              "papers",            "Nature: Quantum Physics"),
    ("https://www.nature.com/nphys.rss",                                 "papers",            "Nature Physics"),
    ("https://journals.aps.org/prxquantum/rss",                          "papers",            "PRX Quantum"),
    ("https://journals.aps.org/prl/rss",                                 "papers",            "Physical Review Letters"),
    ("https://www.science.org/rss/news_current.xml",                     "papers",            "Science (general)"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 2 — QUANTUM-FOCUSED PRESS & NEWS AGGREGATORS
    # ══════════════════════════════════════════════════════════════════
    ("https://thequantuminsider.com/feed/",                              "industry",          "The Quantum Insider"),
    ("https://quantumcomputingreport.com/feed/",                         "industry",          "Quantum Computing Report"),
    ("https://www.hpcwire.com/category/quantum-computing/feed/",         "industry",          "HPCwire Quantum"),
    ("https://www.quantamagazine.org/category/quantum-physics/feed/",    "research",          "Quanta Magazine"),
    ("https://phys.org/rss-feed/physics-news/quantum-physics/",          "research",          "Phys.org Quantum"),
    ("https://physicsworld.com/c/quantum/feed/",                         "research",          "Physics World Quantum"),
    ("https://www.newscientist.com/subject/physics/feed/",               "research",          "New Scientist Physics"),
    ("https://spectrum.ieee.org/feeds/topic/quantum-computing.rss",      "industry",          "IEEE Spectrum Quantum"),
    ("https://techcrunch.com/category/quantum/feed/",                    "industry",          "TechCrunch Quantum"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 3 — INDUSTRY HARDWARE / PLATFORM COMPANY BLOGS
    # ══════════════════════════════════════════════════════════════════
    ("https://research.ibm.com/blog/feed.xml",                           "industry",          "IBM Research Blog"),
    ("https://blog.google/technology/research/rss/",                     "industry",          "Google Research Blog"),
    ("https://cloudblogs.microsoft.com/quantum/feed/",                   "industry",          "Microsoft Azure Quantum"),
    ("https://aws.amazon.com/blogs/quantum-computing/feed/",             "industry",          "AWS Quantum Blog"),
    ("https://ionq.com/news/feed",                                       "industry",          "IonQ News"),
    ("https://www.quantinuum.com/news/feed",                             "industry",          "Quantinuum News"),
    ("https://pasqal.com/news/feed",                                     "industry",          "Pasqal News"),
    ("https://www.atom-computing.com/news/feed",                         "industry",          "Atom Computing News"),
    ("https://www.dwavesys.com/news/feed",                               "industry",          "D-Wave News"),
    ("https://psiquantum.com/news/feed",                                 "industry",          "PsiQuantum News"),
    ("https://www.xanadu.ai/blog/feed",                                  "industry",          "Xanadu Blog"),
    ("https://www.rigetti.com/news/feed",                                "industry",          "Rigetti News"),
    ("https://www.iqmquantum.com/news/feed",                             "industry",          "IQM News"),
    ("https://www.quera.com/news/feed",                                  "industry",          "QuEra News"),
    ("https://www.riverlane.com/news/feed",                              "industry",          "Riverlane News"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 4 — TOOLS, FRAMEWORKS, OPEN SOURCE
    # ══════════════════════════════════════════════════════════════════
    ("https://qiskit.org/blog/feed.xml",                                 "tools",             "Qiskit Blog"),
    ("https://pennylane.ai/blog/feed",                                   "tools",             "PennyLane Blog"),
    ("https://medium.com/feed/qiskit",                                   "tools",             "Qiskit Medium"),
    ("https://www.cqcl.io/news/feed",                                    "tools",             "CQC News"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 5 — SUBREDDITS (community sentiment)
    # ══════════════════════════════════════════════════════════════════
    ("https://www.reddit.com/r/QuantumComputing/.rss",                   "research",          "r/QuantumComputing"),
    ("https://www.reddit.com/r/quantum/.rss",                            "research",          "r/quantum"),
    ("https://www.reddit.com/r/Physics/.rss",                            "research",          "r/Physics"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 6 — X / TWITTER via fxtwitter (industry company accounts)
    # ══════════════════════════════════════════════════════════════════
    ("https://fxtwitter.com/IBMQuantum/feed.xml",                        "industry",          "IBM Quantum (X)"),
    ("https://fxtwitter.com/GoogleQuantumAI/feed.xml",                   "industry",          "Google Quantum AI (X)"),
    ("https://fxtwitter.com/IonQ_Inc/feed.xml",                          "industry",          "IonQ (X)"),
    ("https://fxtwitter.com/Quantinuum/feed.xml",                        "industry",          "Quantinuum (X)"),
    ("https://fxtwitter.com/rigetti/feed.xml",                           "industry",          "Rigetti (X)"),
    ("https://fxtwitter.com/PsiQuantum/feed.xml",                        "industry",          "PsiQuantum (X)"),
    ("https://fxtwitter.com/AtomComputing/feed.xml",                     "industry",          "Atom Computing (X)"),
    ("https://fxtwitter.com/PasqalQuantum/feed.xml",                     "industry",          "Pasqal (X)"),
    ("https://fxtwitter.com/XanaduAI/feed.xml",                          "industry",          "Xanadu (X)"),
    ("https://fxtwitter.com/AzureQuantum/feed.xml",                      "industry",          "Azure Quantum (X)"),
    ("https://fxtwitter.com/AWSQuantum/feed.xml",                        "industry",          "AWS Quantum (X)"),
    ("https://fxtwitter.com/dwavesys/feed.xml",                          "industry",          "D-Wave (X)"),
    ("https://fxtwitter.com/IQMQuantum/feed.xml",                        "industry",          "IQM (X)"),
    ("https://fxtwitter.com/QuEraComputing/feed.xml",                    "industry",          "QuEra (X)"),

    # ══════════════════════════════════════════════════════════════════
    # TIER 7 — RESEARCHERS & COMMENTATORS (X)
    # ══════════════════════════════════════════════════════════════════
    ("https://fxtwitter.com/preskill/feed.xml",                          "research",          "John Preskill (X)"),
    ("https://fxtwitter.com/ScottAaronson/feed.xml",                     "research",          "Scott Aaronson (X)"),
    ("https://fxtwitter.com/dabacon/feed.xml",                           "research",          "Dave Bacon (X)"),
    ("https://fxtwitter.com/quantum_aviary/feed.xml",                    "research",          "Quantum Aviary (X)"),
    ("https://fxtwitter.com/QuantumPhysical/feed.xml",                   "research",          "QuantumPhysical (X)"),
    ("https://fxtwitter.com/QuantumNetwork/feed.xml",                    "research",          "Quantum Network (X)"),
    ("https://fxtwitter.com/PhysicsTalk/feed.xml",                       "research",          "Physics Talk (X)"),
    ("https://fxtwitter.com/QuantumWomen/feed.xml",                      "research",          "Quantum Women (X)"),

    # ══════════════════════════════════════════════════════════════════
    # ADDED 2026-04-29 — quantum specialist categories
    # ══════════════════════════════════════════════════════════════════

    # — Networking: quantum internet, repeaters, switches ──────────────
    ("https://newsroom.cisco.com/rss/news.xml",                          "networking",        "Cisco Newsroom"),
    ("https://aliroquantum.com/blog/feed/",                              "networking",        "Aliro Quantum"),
    ("https://quantum-internet.team/feed/",                              "networking",        "Quantum Internet Alliance"),
    ("https://evolutionq.com/feed/",                                     "networking",        "EvolutionQ"),
    ("https://qunnect.inc/feed/",                                        "networking",        "Qunnect"),

    # — Cryptography: QKD, post-quantum, quantum-safe ──────────────────
    ("https://eprint.iacr.org/rss/rss.xml",                              "cryptography",      "IACR ePrint Archive"),
    ("https://www.schneier.com/feed/atom/",                              "cryptography",      "Schneier on Security"),
    ("https://csrc.nist.gov/projects/post-quantum-cryptography",         "cryptography",      "NIST PQC"),
    ("https://openquantumsafe.org/papers/",                              "cryptography",      "Open Quantum Safe"),
    ("https://www.idquantique.com/blog/feed/",                           "cryptography",      "ID Quantique Blog"),
    ("https://www.idquantique.com/news/feed/",                           "cryptography",      "ID Quantique News"),
    ("https://pqshield.com/blog/feed/",                                  "cryptography",      "PQShield Blog"),
    ("https://aws.amazon.com/blogs/security/category/security-cryptography/feed/", "cryptography", "AWS Security Crypto"),

    # — Sensing: magnetometers, atomic clocks, gravimeters ─────────────
    ("https://infleqtion.com/feed/",                                     "sensing",           "Infleqtion"),
    ("https://q-ctrl.com/feed/",                                         "sensing",           "Q-CTRL Blog"),
    ("https://qnami.ch/feed/",                                           "sensing",           "Qnami"),
    ("https://quspin.com/feed/",                                         "sensing",           "QuSpin"),
    ("https://www.vectoratomic.com/feed/",                               "sensing",           "Vector Atomic"),
    ("https://quantxlabs.com/feed/",                                     "sensing",           "QuantX Labs"),
    ("http://export.arxiv.org/rss/physics.atom-ph",                      "sensing",           "arXiv physics.atom-ph"),

    # — Error correction: FTQC, surface code, LDPC ─────────────────────
    ("https://www.riverlane.com/feed/",                                  "error-correction",  "Riverlane Blog"),
    ("https://research.google/blog/rss/",                                "error-correction",  "Google Research"),

    # — Chemistry: quantum chemistry, drug discovery ───────────────────
    ("https://www.phasecraft.io/feed/",                                  "chemistry",         "Phasecraft"),
    ("https://qsimulate.com/feed/",                                      "chemistry",         "QSimulate"),
    ("https://1qbit.com/feed/",                                          "chemistry",         "1QBit"),
    ("http://export.arxiv.org/rss/physics.chem-ph",                      "chemistry",         "arXiv physics.chem-ph"),

    # — Machine learning: QML, hybrid algorithms ───────────────────────
    ("https://qcware.com/feed/",                                         "machine-learning",  "QC Ware Blog"),
    ("https://multiversecomputing.com/feed/",                            "machine-learning",  "Multiverse Computing"),
    ("https://pennylane.ai/qml/feed.xml",                                "machine-learning",  "PennyLane QML"),
    ("https://developer.nvidia.com/blog/category/quantum-computing/feed/","machine-learning", "NVIDIA Quantum"),
]

def _sanitize_xml(data):
    """Fix common XML issues that cause strict parsers to fail."""
    # Remove XML declaration if malformed (re-add a clean one)
    data = re.sub(r'<\?xml[^?]*\?>', '', data, count=1).strip()
    # Fix unescaped ampersands (but not valid XML entities or numeric refs)
    data = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', data)
    # Strip control characters (except tab, newline, carriage return)
    data = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', data)
    # Replace common HTML entities that aren't valid in XML
    html_entities = {
        '&nbsp;': '&#160;', '&ndash;': '&#8211;', '&mdash;': '&#8212;',
        '&lsquo;': '&#8216;', '&rsquo;': '&#8217;', '&ldquo;': '&#8220;',
        '&rdquo;': '&#8221;', '&bull;': '&#8226;', '&hellip;': '&#8230;',
        '&eacute;': '&#233;', '&copy;': '&#169;', '&reg;': '&#174;',
        '&trade;': '&#8482;', '&euro;': '&#8364;', '&pound;': '&#163;',
    }
    for ent, repl in html_entities.items():
        data = data.replace(ent, repl)
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + data


def _parse_xml_tree(data):
    """Try parsing XML: strict first, then sanitized. Returns root or None."""
    # Attempt 1: strict parse
    try:
        return ET.fromstring(data)
    except ET.ParseError:
        pass

    # Attempt 2: sanitize and retry
    try:
        return ET.fromstring(_sanitize_xml(data))
    except ET.ParseError:
        pass

    return None


def _extract_items_from_tree(root):
    """Extract items from a parsed XML tree (RSS or Atom)."""
    items = []
    # Atom feeds
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for entry in root.findall("a:entry", ns):
        title = entry.findtext("a:title", "", ns).strip()
        link_el = entry.find("a:link", ns)
        link = link_el.get("href", "") if link_el is not None else ""
        published = entry.findtext("a:published", "", ns) or entry.findtext("a:updated", "", ns)
        summary = entry.findtext("a:summary", "", ns)
        items.append({"title": title, "url": link, "date": published, "summary": summary or ""})

    # RSS feeds
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = item.findtext("pubDate") or item.findtext("dc:date") or ""
        desc = item.findtext("description") or ""
        items.append({"title": title, "url": link, "date": pub_date, "summary": desc})

    return items


def _regex_extract_items(data):
    """Last-resort regex extraction of <item> and <entry> blocks."""
    items = []

    # Extract RSS <item> blocks
    for m in re.finditer(r'<item[^>]*>(.*?)</item>', data, re.DOTALL):
        block = m.group(1)
        title = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', block, re.DOTALL)
        link = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', block, re.DOTALL)
        pub_date = re.search(r'<pubDate[^>]*>(.*?)</pubDate>', block, re.DOTALL)
        desc = re.search(r'<description[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', block, re.DOTALL)
        items.append({
            "title": unescape(title.group(1).strip()) if title else "",
            "url": unescape(link.group(1).strip()) if link else "",
            "date": pub_date.group(1).strip() if pub_date else "",
            "summary": unescape(desc.group(1).strip()) if desc else "",
        })

    # Extract Atom <entry> blocks
    for m in re.finditer(r'<entry[^>]*>(.*?)</entry>', data, re.DOTALL):
        block = m.group(1)
        title = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', block, re.DOTALL)
        link = re.search(r'<link[^>]*href=["\']([^"\']+)["\']', block)
        if not link:
            link = re.search(r'<link[^>]*>(.*?)</link>', block, re.DOTALL)
        published = re.search(r'<published[^>]*>(.*?)</published>', block, re.DOTALL)
        if not published:
            published = re.search(r'<updated[^>]*>(.*?)</updated>', block, re.DOTALL)
        summary = re.search(r'<summary[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</summary>', block, re.DOTALL)
        if not summary:
            summary = re.search(r'<content[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</content>', block, re.DOTALL)

        link_val = ""
        if link:
            link_val = link.group(1).strip()

        items.append({
            "title": unescape(title.group(1).strip()) if title else "",
            "url": unescape(link_val),
            "date": published.group(1).strip() if published else "",
            "summary": unescape(summary.group(1).strip()) if summary else "",
        })

    return items


def fetch_feed(url):
    """Fetch and parse an RSS/Atom feed, return list of items."""
    items = []
    try:
        result = subprocess.run(["curl", "-s", "-L", "--max-time", "15",
                                "-A", "WikiAgent/1.0 (AI Wiki; contact: rksbrooke@gmail.com)",
                                url],
                               capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ✗ Failed to fetch {url}: curl error {result.returncode}")
            return items
        data = result.stdout
    except Exception as e:
        print(f"  ✗ Failed to fetch {url}: {e}")
        return items

    if not data.strip():
        print(f"  ✗ Empty response from {url}")
        return items

    # Try XML parsing (strict, then sanitized)
    root = _parse_xml_tree(data)
    if root is not None:
        items = _extract_items_from_tree(root)
        return items

    # Last resort: regex-based extraction
    print(f"  ⚠ XML parse failed for {url}, falling back to regex extraction")
    items = _regex_extract_items(data)
    if not items:
        print(f"  ✗ Regex extraction also found no items from {url}")

    return items

def parse_date(date_str):
    """Try to parse various date formats."""
    for fmt in [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S",
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%d",
    ]:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except (ValueError, AttributeError):
            continue
    return None

def clean_latex(text):
    """Remove LaTeX escape sequences from titles (common in arXiv)."""
    text = re.sub(r"\\['`^~\"=.uvHtcdb]\{?(\w)\}?", r'\1', text)  # \'o -> o
    text = re.sub(r"\$([^$]+)\$", r'\1', text)  # $math$ -> math
    text = re.sub(r"\\(?:textbf|textit|emph|mathrm|mathbb|mathcal)\{([^}]+)\}", r'\1', text)
    text = text.replace('\\\\', ' ').replace('\\', '')
    return text

def clean_html(text, max_len=200):
    """Strip HTML tags, decode entities, clean LaTeX."""
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = clean_latex(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_len]

def clean_html_full(text):
    """Strip HTML tags, keep full text for body content."""
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = clean_latex(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def slugify(title):
    """Convert title to kebab-case filename slug."""
    s = title.lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s).strip("-")
    return s[:60]

def smart_classify(title, summary, default_category):
    """Classify entry based on title/summary keywords, overriding default if confident."""
    text = (title + " " + summary).lower()

    # Model releases — new models, benchmarks, version updates
    if re.search(r'\b(gpt-[45o]|claude|gemini|gemma|llama|mistral|qwen|nemotron|deepseek|phi-|command-r|released|launches|benchmark|parameter|token.per.sec|context.window|new model)\b', text):
        return "model-releases"

    # Local AI — ollama, llama.cpp, local inference, DGX, quantization
    if re.search(r'\b(ollama|llama\.cpp|gguf|ggml|quantiz|local.*(model|inference|ai|llm)|dgx|vram|on-device|edge.ai|mlx)\b', text):
        return "local-ai"

    # Safety — alignment, safety, regulation, policy, bias
    if re.search(r'\b(safety|alignment|guardrail|jailbreak|red.team|bias|fairness|regulat|legislation|eu.ai.act|policy|existential|x-risk|responsible.ai)\b', text):
        return "safety"

    # Hardware — GPU, TPU, chip, inference hardware
    if re.search(r'\b(gpu|tpu|nvidia|h100|a100|b200|gb200|blackwell|inference.chip|datacent|silicon|tensor.core|cuda)\b', text):
        return "hardware"

    # Agents — agentic, autonomous, agent framework
    if re.search(r'\b(agent|agentic|autonomous|tool.use|function.call|mcp|openclraw|nemoclaw|multi-agent|swarm)\b', text):
        return "agents"

    # Tutorials — how to, guide, tutorial, course
    if re.search(r'\b(tutorial|how.to|step.by.step|guide|course|learn|beginner|walkthrough|hands-on)\b', text):
        return "tutorials"

    # Applications — deployment, case study, real-world use
    if re.search(r'\b(deploy|production|case.study|real.world|enterprise|healthcare|finance|legal|education|manufacturing)\b', text):
        return "applications"

    return default_category

def existing_urls():
    """Collect all URLs already in the wiki to avoid duplicates."""
    urls = set()
    for root, dirs, files in os.walk(WIKI_DIR):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in {"scripts", "public", "openclaw", "_templates", "raw"}]
        for f in files:
            if f.endswith(".md"):
                try:
                    text = open(os.path.join(root, f)).read()
                    for m in re.findall(r'url:\s*"?([^"\n]+)', text):
                        urls.add(m.strip().rstrip("/"))
                except:
                    pass
    return urls

OLLAMA_URL = "http://host.openshell.internal:11434/v1/chat/completions"
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_KEY_FILES = [
    "/sandbox/.openclaw-data/anthropic-key",
    "/etc/openclaw-secrets/anthropic-key",
]

def _read_anthropic_key():
    for path in ANTHROPIC_KEY_FILES:
        try:
            return open(path).read().strip()
        except:
            continue
    return os.environ.get("ANTHROPIC_API_KEY", "").strip()

ANTHROPIC_KEY = _read_anthropic_key()

def extract_page_text(html):
    """Extract readable text from HTML, trying multiple strategies."""
    # Strategy 1: Try __NEXT_DATA__ (Next.js sites)
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            text = json.dumps(data.get("props", {}).get("pageProps", {}))
            text = re.sub(r'[{}\[\]",:]+', ' ', text)
            text = re.sub(r'\\[nrt]', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 100:
                return text[:3000]
        except:
            pass

    # Strategy 2: Try <article> or <main> content
    for tag in ['article', 'main', 'div class="post', 'div class="blog', 'div class="content']:
        m = re.search(rf'<{tag}[^>]*>(.*?)</{tag.split()[0]}>', html, re.DOTALL | re.IGNORECASE)
        if m:
            text = re.sub(r'<[^>]+>', ' ', m.group(1))
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 100:
                return text[:3000]

    # Strategy 3: Try meta description + og:description
    descs = []
    for attr in ['description', 'og:description', 'twitter:description']:
        m = re.search(rf'<meta[^>]*(?:name|property)="{attr}"[^>]*content="([^"]+)"', html, re.IGNORECASE)
        if m:
            descs.append(m.group(1))
    if descs:
        return ' '.join(descs)[:3000]

    # Strategy 4: Strip all HTML and take what's left
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Skip if it's mostly JavaScript garbage
    if len(text) > 100 and text.count('function') < 5:
        return text[:3000]

    return None

def ollama_summarize(text, title):
    """Ask Ollama to summarize extracted text."""
    try:
        payload = json.dumps({
            "model": "qwen3:30b",
            "messages": [{"role": "user", "content":
                f"Summarize this in 2-3 sentences for an AI knowledge base. Be factual and concise.\n"
                f"Title: {title}\n\nContent:\n{text[:2000]}"}],
            "max_tokens": 200
        })
        result = subprocess.run(
            ["curl", "-s", "--max-time", "30", "-X", "POST",
             OLLAMA_URL, "-H", "Content-Type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        summary = resp.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
        return summary if summary and len(summary) > 20 else None
    except:
        return None

def claude_summarize(title, source_name, url, use_web_search=False):
    """Fallback: ask Claude to summarize.
    use_web_search=True: uses web_search tool (~$0.16/call, more accurate, recent content)
    use_web_search=False: uses training only (~$0.005/call, may be stale for very recent items)
    """
    if not ANTHROPIC_KEY:
        return None
    try:
        msg_body = {
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 300,
            "messages": [{"role": "user", "content":
                f"Write a concise 2-3 sentence factual summary for an AI knowledge base entry. "
                f"Return ONLY the summary text, no preamble. If you don't have specific info, "
                f"describe what this likely covers based on the title and source.\n\n"
                f"Title: {title}\nSource: {source_name}\nURL: {url}"}]
        }
        if use_web_search:
            msg_body["tools"] = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 1}]
        payload = json.dumps(msg_body)
        result = subprocess.run(
            ["curl", "-s", "--max-time", "60", "-X", "POST", ANTHROPIC_URL,
             "-H", f"x-api-key: {ANTHROPIC_KEY}",
             "-H", "anthropic-version: 2023-06-01",
             "-H", "content-type: application/json",
             "-d", payload],
            capture_output=True, text=True)
        if result.returncode != 0:
            return None
        resp = json.loads(result.stdout)
        text_blocks = [b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text"]
        summary = " ".join(text_blocks).strip()
        return summary if summary and len(summary) > 30 else None
    except Exception as e:
        print(f"    ⚠ Claude error: {e}")
        return None

def is_recent_url(item_date_str):
    """Check if entry is from the last 7 days (worth web search)."""
    try:
        from datetime import datetime, timedelta, timezone
        for fmt in ["%Y-%m-%dT%H:%M:%S%z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%d"]:
            try:
                dt = datetime.strptime(item_date_str.strip(), fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                cutoff = datetime.now(timezone.utc) - timedelta(days=7)
                return dt > cutoff
            except:
                continue
    except:
        pass
    return False

def fetch_and_summarize(url, title, source_name="", item_date=""):
    """Try Ollama first, fall back to Claude API.
    Claude uses web_search ONLY for entries from the last 7 days (cost saving)."""
    # Step 1: Try fetching the page and using Ollama
    try:
        result = subprocess.run(
            ["curl", "-s", "-L", "--max-time", "10",
             "-A", "WikiAgent/1.0 (AI Wiki; contact: rksbrooke@gmail.com)", url],
            capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            page_text = extract_page_text(result.stdout)
            if page_text:
                summary = ollama_summarize(page_text, title)
                if summary:
                    return summary
    except Exception as e:
        print(f"    ⚠ Ollama path failed: {e}")

    # Step 2: Fall back to Claude API
    # Use web search only for recent entries (last 7 days) to save cost
    if ANTHROPIC_KEY:
        recent = is_recent_url(item_date)
        print(f"    → Falling back to Claude API (web_search={recent})")
        return claude_summarize(title, source_name, url, use_web_search=recent)
    return None

def write_entry(item, category, source_name):
    """Write a wiki entry .md file."""
    item["title"] = clean_latex(item["title"])
    slug = slugify(item["title"])
    if not slug:
        return None

    cat_dir = os.path.join(WIKI_DIR, category)
    os.makedirs(cat_dir, exist_ok=True)
    filepath = os.path.join(cat_dir, f"{slug}.md")

    if os.path.exists(filepath):
        return None

    pub_date = parse_date(item["date"])
    date_str = pub_date.strftime("%Y-%m-%d") if pub_date else TODAY
    summary = clean_html(item["summary"])
    if not summary:
        summary = item["title"]

    tags = [category]
    if source_name:
        tags.append(re.sub(r"[^a-z0-9]", "-", source_name.lower()).strip("-"))

    # Get full body text from RSS description
    body_text = clean_html_full(item.get("summary", ""))
    # If body is too short, just teaser, or same as title, try fetching and summarizing
    if len(body_text) < 200 or body_text.lower().strip() == item["title"].lower().strip():
        if item.get("url"):
            print(f"    → Fetching & summarizing: {item['url'][:60]}...")
            ai_summary = fetch_and_summarize(item["url"], item["title"], source_name, item.get("date", ""))
            if ai_summary:
                body_text = ai_summary
                summary = clean_html(ai_summary)
            else:
                body_text = ""

    # Build body sections
    body_lines = []
    if body_text:
        body_lines.append(f"{body_text}")
    else:
        body_lines.append(f"{item['title']}.")

    content = f"""---
title: "{item['title'].replace('"', "'")}"
date: "{date_str}"
updated: "{TODAY}"
source: "agent"
category: "{category}"
tags: [{", ".join(tags)}]
url: "{item['url']}"
summary: "{summary.replace('"', "'")}"
last_verified: "{TODAY}"
review_by: "{REVIEW_BY}"
stale: false
---

{chr(10).join(body_lines)}

**Source:** [{source_name}]({item['url']}) | {date_str}
"""

    with open(filepath, "w") as f:
        f.write(content)
    return filepath

def main():
    print(f"🔄 Wiki agent starting — {TODAY}")

    # Git pull
    os.chdir(WIKI_DIR)
    subprocess.run(["git", "-c", "http.sslVerify=false", "pull", "--rebase", "origin", "main"],
                   capture_output=True, text=True)

    known_urls = existing_urls()
    print(f"📚 {len(known_urls)} existing URLs in wiki")

    written = []
    skipped = 0
    errors = 0

    for feed_url, category, name in FEEDS:
        print(f"\n📡 Scanning: {name} ({feed_url})")
        items = fetch_feed(feed_url)
        print(f"   Found {len(items)} items")

        for item in items:
            if not item["title"] or not item["url"]:
                continue

            # Skip duplicates
            clean_url = item["url"].strip().rstrip("/")
            if clean_url in known_urls:
                skipped += 1
                continue

            # Skip old items
            pub_date = parse_date(item["date"])
            if pub_date and pub_date < CUTOFF:
                skipped += 1
                continue

            # Smart classify based on content
            actual_category = smart_classify(item["title"], item.get("summary", ""), category)

            # Write entry
            path = write_entry(item, actual_category, name)
            if path:
                written.append((item["title"], actual_category))
                known_urls.add(clean_url)
                print(f"   ✓ {item['title'][:60]}")

    print(f"\n{'='*60}")
    print(f"📊 Results: {len(written)} new, {skipped} skipped, {errors} errors")

    if written:
        # Run Karpathy-style enrichment on the new entries (Claude API, ~$0.01/entry)
        env = os.environ.copy()
        if ANTHROPIC_KEY:
            env["ANTHROPIC_API_KEY"] = ANTHROPIC_KEY
        print(f"\n🔗 Enriching {len(written)} new entries with cross-references...")
        try:
            subprocess.run(["python3", "/sandbox/quantum-wiki/scripts/link-entries.py", str(len(written))],
                          capture_output=True, text=True, timeout=1200, env=env)
        except Exception as e:
            print(f"  ⚠ link-entries failed: {e}")

        # Concept extraction moved to weekly Sunday cron (saves cost)
        # Auto-synthesis moved to weekly Sunday cron (saves cost)

        # Rebuild entries.json
        print(f"\n🔨 Rebuilding entries.json...")
        subprocess.run(["python3", "/sandbox/quantum-wiki/scripts/build-wiki.py"],
                      capture_output=True, text=True, timeout=600)

        # Commit and push
        subprocess.run(["git", "add", "-A"], capture_output=True)
        msg = f"agent: {TODAY} — {len(written)} new entries (with backlinks + concepts + syntheses)"
        subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
        result = subprocess.run(["git", "-c", "http.sslVerify=false", "push", "origin", "main"],
                               capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Pushed {len(written)} entries to GitHub")
        else:
            print(f"❌ Push failed: {result.stderr}")

        print("\n📚 New entries:")
        for title, cat in written:
            print(f"  · [{cat}] {title[:70]}")
    else:
        print("ℹ️  No new entries to write")

    print(f"\n✅ Wiki agent done — {TODAY}")

if __name__ == "__main__":
    main()
