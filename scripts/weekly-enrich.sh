#!/bin/bash
# Weekly enrichment — runs Sundays 9am (after lint)
# Does: lint, extractor on all entries without concepts, auto-synthesis
set -e

export ANTHROPIC_API_KEY=$(cat /sandbox/.openclaw-data/anthropic-key 2>/dev/null || echo "")
cd /sandbox/quantum-wiki

echo "🔍 Running wiki lint..."
python3 scripts/wiki-lint.py

echo ""
echo "🏷  Running concept extractor on all entries..."
python3 scripts/extract-with-claude.py

echo ""
echo "📝 Running auto-synthesis on topic clusters..."
python3 scripts/auto-synthesize.py 10

echo ""
echo "💾 Committing weekly enrichment..."
git add -A
git commit -m "agent: weekly enrichment — lint + concepts + synthesis" 2>/dev/null || echo "nothing to commit"
git -c http.sslVerify=false pull --rebase origin main 2>/dev/null || true
git -c http.sslVerify=false push origin main 2>/dev/null && echo "✅ Pushed"
