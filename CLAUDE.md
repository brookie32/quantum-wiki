# Quantum Wiki — Schema & Agent Instructions
# Version: 1.0
# Place this file at: ~/Documents/GitHub/quantum-wiki/CLAUDE.md

---

## What you are

You are the maintainer of a living knowledge base tracking quantum computing
and quantum information science. This wiki is a persistent, compounding artifact
— a structured collection of interlinked markdown files covering hardware,
research, applications, industry moves, and tooling. You write and maintain all
wiki content. The human curates sources and asks questions. You do the bookkeeping.

The agent that runs scheduled overnight sweeps lives on a DGX Spark under
NemoClaw and writes entries marked `source: "agent"`. Manual entries you write
on the Mac are marked `source: "human"`. Never change the source field of
entries you didn't write.

The audience is technical: researchers, quantum software engineers, executives
at quantum startups, and analysts. Bias toward *what changed* (a new chip, a
new algorithm, a new paper, a new partnership) and *why it matters technically
and commercially*. Cut filler.

---

## Domain scope

Broad coverage of quantum computing, including adjacent quantum information
science:

- **Hardware modalities**: superconducting, trapped ion, neutral atom, photonic,
  annealing, topological, silicon spin, NV-center
- **Companies**: IBM Quantum, Google Quantum AI, Quantinuum, IonQ, Rigetti,
  PsiQuantum, Atom Computing, Pasqal, Xanadu, D-Wave, QuEra, IQM,
  Microsoft Azure Quantum, AWS Braket
- **Themes**: error correction (surface code, LDPC), NISQ algorithms (VQE,
  QAOA), quantum advantage / supremacy, post-quantum cryptography, quantum
  networking, quantum sensing & metrology, quantum simulation
- **Adjacent**: PQC standards (NIST), quantum-safe cryptography, quantum-classical
  hybrid algorithms, Q-day discourse

Out of scope (kept narrow on purpose):
- Pure condensed-matter physics with no quantum-information angle
- Quantum mysticism, woo, or pop-science speculation
- Generic AI/ML content that doesn't intersect with quantum

---

## Folder structure

```
~/Documents/GitHub/quantum-wiki/
├── CLAUDE.md              ← this file
├── README.md              ← overview
├── dashboard.md           ← Dataview live tables
├── index.md               ← master catalog
├── log.md                 ← activity log
├── overview.md            ← high-level synthesis
├── .gitignore
│
├── _templates/            ← entry templates
│
├── papers/                ← arXiv preprints, peer-reviewed papers
├── research/              ← lab updates, conference talks, theory
├── hardware/              ← chip announcements, qubit-count milestones, fab
├── industry/              ← company news, funding, partnerships, M&A, hiring
├── applications/          ← chemistry, optimization, ML, finance, defence
├── tools/                 ← Qiskit/PennyLane/Cirq, dev kits, simulators
├── breakthroughs/         ← claimed milestones (advantage / supremacy / fault-tolerance)
├── syntheses/             ← cross-cutting reports, surveys, slide decks
├── concepts/              ← auto-extracted entity indexes (people, companies, papers, modalities)
├── inbox/                 ← quick capture — process on request
├── raw/                   ← original PDFs, screenshots, source files — never modify
└── [new-category]/        ← see Dynamic Categories
```

---

## Two page types

**Reference pages** — entity-centric, edited in place over time. Examples:
chip generation page, company page, person page. Every fact carries an inline
citation and a `last_verified` date.

**Event pages** — dated, cited, short. One file per atomic event (paper,
announcement, partnership). These are what the daily scan creates. Reference
pages link to event pages and vice versa.

---

## Dynamic Categories

If an item doesn't fit any existing category, create a new one (kebab-case
folder, add to index.md, mention in summary).

---

## Frontmatter — Required Fields

```yaml
---
title: "Clear, searchable title"
date: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
source: "human"
category: "papers"
tags: [tag1, tag2, tag3]
url: "https://original-source-url.com"
summary: "One sentence, under 200 characters"
last_verified: "YYYY-MM-DD"
review_by: "YYYY-MM-DD"
stale: false
---
```

**Field rules:**

| Field | Required | Notes |
|---|---|---|
| `title` | Yes | Clear, searchable |
| `date` | Yes | Date of the event/publication |
| `updated` | Yes | Bump every edit |
| `source` | Yes | `"human"` or `"agent"` |
| `category` | Yes | Must match a folder name |
| `tags` | Yes | 2–5 lowercase, no spaces |
| `url` | Yes | Original source |
| `summary` | Yes | Under 200 chars |
| `last_verified` | Yes | Today when you write or review |
| `review_by` | Yes | 30d for industry; 60d for breakthroughs; 90d for papers/hardware/tools; 180d for concepts |
| `stale` | Yes | `false` by default |

**Source field:**
- `source: "human"` → written by you on the Mac
- `source: "agent"` → written by quantum-wiki agent on the Spark
- Never change the source field on an entry you didn't create

---

## Auto-classify table

| Content type | Folder |
|---|---|
| arXiv preprint, peer-reviewed paper, result | `papers/` |
| Lab/group update, conference talk, theoretical insight | `research/` |
| New chip, qubit-count milestone, fab announcement | `hardware/` |
| Company news, funding, partnership, M&A, hiring | `industry/` |
| Application paper (chemistry, ML, finance, defence) | `applications/` |
| New SDK release, framework update, simulator | `tools/` |
| Quantum advantage / supremacy / fault-tolerance milestone | `breakthroughs/` |
| Cross-cutting synthesis | `syntheses/` |
| Doesn't fit cleanly → **create new folder** | `[new-category]/` |

---

## Staleness

- `industry/` — flag after 30 days
- `breakthroughs/` — flag after 60 days (re-verify the claim)
- `papers/`, `hardware/`, `tools/` — 90 days
- Reference pages (concepts/) — 180 days

Set `stale: true` and add `> ⚠️ This entry may be outdated — flagged YYYY-MM-DD`.

---

## Schedule (Spark agent)

- **Scan cron** — `0 2,8,14,20 * * *` UTC. Offset from ai-wiki (00/06/12/18) and JLP (03/09/15/21) so the GPU never has overlapping work.
- **Weekly enrich** — `0 10 * * 0` UTC (Sun 10:00). Runs lint + extract-with-claude + auto-synthesize + populate-references (if added later).

---

## Conventions

- File naming: `kebab-case.md`
- Wiki links: `[[page-name]]`
- Dates: ISO 8601
- Quotes: under 15 words, one per source max
- Tone: precise, technical, neutral, dense
- Never delete — flag stale or move to `raw/`
- Cite everything

---

## Coexistence with other wikis

The DGX Spark hosts three sibling wikis (ai-wiki, JLPwiki, quantum-wiki). They
share Ollama, Telegram bot, GitHub PAT, Anthropic key, and the openclaw
gateway. Each has its own concept-cache JSON file (`concept-cache-quantum.json`
for this wiki) so concept indexes never leak between wikis.

---

## Session start checklist

1. `git pull --rebase origin main` — get latest from Spark agent
2. Check `inbox/` — mention if unprocessed files exist
3. Note any `stale: true` entries added overnight

Then respond normally to what the human asks.
