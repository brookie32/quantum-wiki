---
title: "Certifying quantum code and circuit distances at scale"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08247"
summary: "arXiv:2611.08247v1 Announce Type: new Abstract: Code and circuit distances characterize how strongly quantum error correction suppresses logical errors and guide code comparisons, schedule choices and"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.08247v1 Announce Type: new Abstract: Code and circuit distances characterize how strongly quantum error correction suppresses logical errors and guide code comparisons, schedule choices and resource estimates. Yet many published distances are only upper bounds from heuristic searches. Here, we express both distances as tropical partition functions and evaluate them with rank-based dynamic programming and weight-bounded search. Circuit reductions and relaxations shrink the problems, and proved lower bounds with explicit logical errors of matching weight certify exact values. On two benchmarks, our method certifies more instances than all other tested exact solvers combined. We certify distances for codes with up to 31,200 qubits, such as Google's modular hyperbolic codes, and for memory circuits with up to 8imes10^5 fault mechanisms, such as those of high-rate Cornucopia codes. Our audit of 26 recent papers identifies overestimated distances and non-tight upper bounds in 10 papers, with a maximum discrepancy of at least eight. Certified distances also guide circuit design and show which defective chips remain usable. In particular, we certify circuit distance 16 for IBM's two-gross memory circuits with the standard schedule, not the assumed 18, whereas redesigned schedules reach 18 at one noisy cycle, at the cost of one more timestep per cycle. At 99.98% junction yield, keeping gross-code memory blocks with dead checks that are certified at distance 10 or more raises the estimated usable share from 53% for perfect blocks alone to 94% with an improved schedule.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08247) | 2026-11-06
