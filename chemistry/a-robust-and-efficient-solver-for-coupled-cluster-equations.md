---
title: "A robust and efficient solver for coupled cluster equations"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.06669"
summary: "arXiv:2608.06669v1 Announce Type: new Abstract: The coupled-cluster (CC) equations are most frequently solved via fixed-point (FP) iterations. However, when formulated in a non-canonical gauge, as in "
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06669v1 Announce Type: new Abstract: The coupled-cluster (CC) equations are most frequently solved via fixed-point (FP) iterations. However, when formulated in a non-canonical gauge, as in local correlation CC, the FP iteration may converge slowly or even diverge. Practical fixes, such as level-shifting and a direct inversion of iterative subspace (DIIS), often improve the convergence, but remain fundamentally heuristic and gauge dependent. {it Yang et al.}~demonstrated that preconditioned Newton--Krylov (PNK) methods provide substantial wall-time advantage for canonical CC. In this work, we generalize the preconditioner to arbitrary gauges by replacing the energy denominator with a gauge-invariant formulation. Combined with Krylov-based approximate Jacobian inversion, the resulting framework removes the need for level-shifting and yields robust and efficient convergence across various gauges and challenging chemical systems. Our numerical results indicate that PNK consistently outperforms carefully optimized FP-based approaches across a range of molecular systems, positioning the proposed PNK method as a promising new standard for solving the CC equations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.06669) | 2026-08-10
