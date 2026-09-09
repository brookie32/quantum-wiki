#!/usr/bin/env bash
# Weekly enrichment: lint, concepts, synthesis.
# Scheduled from the workstation's crontab (Sundays 13:00) via
# ~/.local/bin/wiki-weekly-enrich, NOT by the OpenClaw gateway. The gateway ran
# this as an LLM agent turn that ended after ~100s while the script needs ~25min,
# so it was killed before its commit/push every week from 2026-08-02 onward and
# still reported "ok". See that wrapper's header for the full story.
#
# Guards below are ported from ai-wiki's copy (2026-09-09). The rule they encode:
# a guard must never refuse on a condition that nothing can clear, or one bad run
# wedges every future run silently. ai-wiki lost six Sundays that way.
set -euo pipefail

ROOT="/sandbox/quantum-wiki"
STATE_DIR="/sandbox/.openclaw-data"
LOCK_FILE="$STATE_DIR/quantum-wiki-writer.lock"
PUSH_FLAG="$ROOT/.push-failed"

mkdir -p "$STATE_DIR"
exec 9>"$LOCK_FILE"
if ! flock -w 3600 9; then
  echo "Another quantum wiki writer held the lock for an hour; weekly enrichment did not run." >&2
  exit 1
fi

cd "$ROOT"

# ── Start guard: a half-finished rebase must never wedge us permanently ──────
if [[ -d "$(git rev-parse --git-path rebase-merge)" || -d "$(git rev-parse --git-path rebase-apply)" ]]; then
  echo "[start-guard] aborting a stale rebase left by a prior run" >&2
  git rebase --abort >/dev/null 2>&1 || true
fi

# ── Start guard: never let a dirty worktree wedge the weekly run ─────────────
# Commit the strays rather than refusing: all of it is mechanically regenerated
# output, and refusing is what turned one interrupted run into a permanent stall
# on ai-wiki.
if [[ -n "$(git status --porcelain --untracked-files=all)" ]]; then
  n="$(git status --porcelain --untracked-files=all | wc -l | tr -d ' ')"
  echo "[start-guard] committing $n stray file(s) left by a prior run" >&2
  git add -A
  git commit -m "agent: $(date -u +%F) — recover $n stray files before weekly enrichment" >/dev/null 2>&1 || true
fi

git -c http.sslVerify=false pull --rebase origin main 2>/dev/null \
  || { echo "[start-guard] pull --rebase failed; aborting rebase and continuing" >&2; git rebase --abort >/dev/null 2>&1 || true; }

export ANTHROPIC_API_KEY="$(cat "$STATE_DIR/anthropic-key" 2>/dev/null || true)"

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
if git diff --cached --quiet; then
  echo "Nothing to commit"
else
  git commit -m "agent: weekly enrichment — lint + concepts + synthesis"
fi

if ! git -c http.sslVerify=false pull --rebase origin main; then
  git rebase --abort 2>/dev/null || true
  echo "Post-run rebase failed. The local commit is preserved; resolve before another writer runs." >&2
  exit 1
fi

# ── Push guard ──────────────────────────────────────────────────────────────
# The old version ended with `git push … 2>/dev/null && echo "✅ Pushed"`, which
# swallowed the error and left nothing behind on failure — the wiki would simply
# stop updating with no trace. Drop a flag file instead; wiki-health fails on it.
if ! git -c http.sslVerify=false push origin main; then
  printf 'PUSH FAILED — weekly enrichment has local commits not on GitHub.\n' > "$PUSH_FLAG"
  echo "Push failed; wrote $PUSH_FLAG and left the commit intact." >&2
  exit 1
fi

git -c http.sslVerify=false fetch origin main
AHEAD="$(git rev-list --count origin/main..HEAD)"
if [[ "$AHEAD" != "0" ]]; then
  printf 'PUSH FAILED — %s local commit(s) not on GitHub.\n' "$AHEAD" > "$PUSH_FLAG"
  echo "Push guard found $AHEAD stranded commit(s)." >&2
  exit 1
fi

rm -f "$PUSH_FLAG"
echo "✅ Weekly enrichment is in sync with origin/main"
