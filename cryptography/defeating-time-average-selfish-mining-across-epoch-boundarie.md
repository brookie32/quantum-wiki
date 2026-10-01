---
title: "Defeating Time-Average Selfish Mining Across Epoch Boundaries in Nakamoto Consensus"
date: "2026-09-30"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2275"
summary: "Selfish mining profits in Nakamoto consensus because difficulty adjustment mechanisms (DAMs) misinterpret uncounted orphans as hash-rate contraction. Although orphan-aware DAMs record orphaned proof-o"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

Selfish mining profits in Nakamoto consensus because difficulty adjustment mechanisms (DAMs) misinterpret uncounted orphans as hash-rate contraction. Although orphan-aware DAMs record orphaned proof-of-work, strict same-epoch inclusion rules enable an orphan exclusion attack (OEA): an adversary can race private forks near epoch boundaries to permanently exclude honest tail orphans from retargeting, restoring substantial profits in short-epoch protocols. We propose the pipelined buffer difficulty adjustment mechanism (PB-DAM), which partitions each epoch into an accountable prefix and a settlement buffer of depth d. Pipelining estimation windows across epochs grants honest miners a grace period to report prefix uncles while advancing buffer work to subsequent retargets, closing the boundary gap without heuristic damping. Random-walk excursion bounds demonstrate that OEA success decays exponentially with d for all alpha le alpha^star < 1/2, reducing the time-averaged profit advantage to O(arepsilon). Under stylized dynamic scheduling models, intermittent idling is analytically shown to be unable to raise the gross reward rate above alpha. Simulations confirm that buffer depths d = 16 neutralize selfish mining even at L = 64 when alpha = 0.40, and systems recover from a 50% hash-rate crash within 2.2 pm 0.8 epochs, incurring under 1% block capacity overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2275) | 2026-09-30
