---
title: "Beyond Feasibility: Finite-Depth Accessibility in Constrained QAOA"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00736"
summary: "arXiv:2610.00736v1 Announce Type: new Abstract: Constraint-preserving mixers keep QAOA within a feasible subspace, but feasibility and global mixer connectivity do not determine which feasible configu"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00736v1 Announce Type: new Abstract: Constraint-preserving mixers keep QAOA within a feasible subspace, but feasibility and global mixer connectivity do not determine which feasible configurations are available to a particular shallow circuit. We study constrained QAOA at the level of the circuit actually executed: a specified feasible initial state, finite depth, and finite schedule of mixer interactions. We define the finite-depth accessible set R_p(M,x_0) and show that the computational-basis support of the ideal QAOA circuit is contained within it. This gives a parameter-independent objective ceiling f_R^star=max_{xin R_p}f(x) and a normalized reachable-quality diagnostic Q_R, separating accessible volume from the objective quality contained within it. We evaluate this framework using resource-matched block-local XY mixer schedules for constrained portfolio optimization and synthetic block-constrained quadratic problems. Across 207 favorable-tail CVaR QAOA configurations, Q_R shows the strongest association with realized shallow-QAOA performance among the structural diagnostics considered, with Pearson and Spearman correlations of 0.7003 and 0.8057; the relationship remains positive under controlled and dependence-aware analyses. The distinction persists across changes in feasible initialization, portfolio size, and objective family. A compilation-only study further shows that, for the dense portfolio Hamiltonians considered here, phase-separator routing dominates the compiled two-qubit resource scale, while mixer schedules with comparable compiled two-qubit cost can exhibit markedly different finite-depth accessible quality. These results motivate objective-relevant finite-depth accessibility as a complementary diagnostic for resource-bounded constrained QAOA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00736) | 2026-10-02
