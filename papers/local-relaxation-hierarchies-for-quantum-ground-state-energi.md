---
title: "Local Relaxation Hierarchies for Quantum Ground State Energies: Convergence Guarantees and Message Passing Algorithms"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40336"
summary: "arXiv:2609.40336v1 Announce Type: new Abstract: Convex relaxation hierarchies provide lower bounds to the ground state energy of quantum many-body systems that can be computed in polynomial time on a "
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40336v1 Announce Type: new Abstract: Convex relaxation hierarchies provide lower bounds to the ground state energy of quantum many-body systems that can be computed in polynomial time on a classical computer, at any fixed hierarchy level. However, scaling these methods to large systems and accurate approximations remains challenging due to the computational cost of traditional solvers and the scarcity of efficiency guarantees. In this work, we develop local relaxation hierarchies and efficient, highly parallelisable message passing algorithms for estimating the relaxed ground state energies. We show that the first level of the hierarchy---based on local consistency of pairwise reduced density matrices---is exact for commuting Hamiltonians on trees. We further establish that another hierarchy, based on consistent intervals, converges exponentially fast in the interval size to the ground state energy for weak perturbations of separable Hamiltonians on a chain, thereby providing an efficient classical algorithm for these systems. Then, we introduce two variants of message passing algorithms that run in O(n/epsilon^2) and O(n/epsilon) time for any fixed level of the local hierarchy on bounded-degree graphs, where epsilon is the precision for the relaxed ground state energy per site. This assumes that the optimal messages have O(1) norm---a condition we observe in practical settings in our experiments. These algorithms are based on the subgradient method and the Nesterov-type accelerated gradient descent method applied to an entropy-smoothed objective. Finally, we benchmark the message passing algorithms across different quantum Hamiltonians, lattice geometries, and relaxation levels, validating the theoretical predictions and their potential to surpass standard convex optimisation solvers for this problem. We release the resulting library at github.com/rick1924/gse-message-passing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40336) | 2026-10-01
