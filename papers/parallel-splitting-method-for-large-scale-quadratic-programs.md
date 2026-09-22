---
title: "Parallel splitting method for large-scale quadratic programs"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.16977"
summary: "arXiv:2503.16977v3 Announce Type: replace Abstract: Current algorithms for large-scale industrial optimization problems typically face a trade-off: they either require exponential time to reach optima"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2503.16977v3 Announce Type: replace Abstract: Current algorithms for large-scale industrial optimization problems typically face a trade-off: they either require exponential time to reach optimal solutions, or employ problem-specific heuristics. To address these limitations, we introduce SPLIT, a general-purpose quantum-inspired framework for decomposing large-scale quadratic programs into smaller subproblems, which are solved in parallel. SPLIT heuristically accounts for objective-function cross-interactions between subproblems, usually neglected in other decomposition techniques. The SPLIT framework can integrate generic subproblem solvers, from branch-and-bound to quantum optimization methods. We demonstrate its effectiveness through comparisons with commercial solvers and published results on MaxCut and Antenna Placement Problems, with up to 20,000 variables. Our results show that SPLIT is capable of providing drastic reductions in computational time, while delivering high-quality solutions. In these regards, the proposed method is well-suited for near real-time applications that require a solution within a strict time frame, or when the problem size exceeds hardware limitations of dedicated devices, such as current quantum computers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.16977) | 2026-09-22
