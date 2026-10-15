---
title: "Gap-Priced |Trangle-States: Dynamic |Trangle Post-Selection and Budget-Aware Factory Provisioning"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.19299"
summary: "arXiv:2610.19299v1 Announce Type: new Abstract: Magic |Trangle-state preparation dominates the cost of fault-tolerant quantum computation on surface codes, yet cultivation and distillation are typical"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.19299v1 Announce Type: new Abstract: Magic |Trangle-state preparation dominates the cost of fault-tolerant quantum computation on surface codes, yet cultivation and distillation are typically provisioned statically, leaving much of the program's error budget unused. We present Gap-Priced |Trangle States (GP|Trangle-S), a lattice surgery scheduler and factory allocator that co-optimizes both methods under a total T-error budget. GP|Trangle-S uses the complementary gap of each cultivated state as a fidelity estimate and dynamically adjusts the cultivation gap cutoff, converting budget slack into speed by giving the scheduler control over the cultivation post-selection. GP|Trangle-S also characterizes distillation factories by size, |Trangle-state production rate, and budget slack, and introduces cultivating factories that embed cultivation within routing channels, achieving fidelities otherwise requiring two-level distillation at a single-level footprint. GP|Trangle-S organizes these characterizations into a factory catalog, and performs distillation factory allocation over this catalog in tandem with the gap cutoff using dynamic-programming to achieve one of i) minimum spacetime volume, ii) minimum execution time, or iii) minimum space overhead, all within a user-provided T-error budget. Across sixteen benchmarks under high and low T-error budgets of 10^{-3} and 10^{-5} respectively, GP|Trangle-S consistently outperforms cultivation-only and single-factory baselines without exceeding the budget, achieving a 5.5imes geometric mean speedup in logical cycle count and a 3.4imes geometric mean reduction in space-time volume.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.19299) | 2026-10-15
