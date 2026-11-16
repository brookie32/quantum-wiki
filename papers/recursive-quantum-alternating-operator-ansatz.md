---
title: "Recursive Quantum Alternating Operator Ansatz"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.17537"
summary: "arXiv:2611.17537v1 Announce Type: new Abstract: The recursive quantum approximate optimisation algorithm~(RQAOA) shrinks an unconstrained combinatorial optimisation problem by eliminating one variable"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.17537v1 Announce Type: new Abstract: The recursive quantum approximate optimisation algorithm~(RQAOA) shrinks an unconstrained combinatorial optimisation problem by eliminating one variable at a time, guided by correlations measured in variational quantum states. We extend this recursion to constrained problems by building on the quantum alternating operator ansatz, which restricts the evolution to feasible solutions through a feasible initial state and feasibility-preserving mixers. However, every elimination alters the feasibility structure, so that such a mixer for the original problem generally fails to be one for the subproblems. Previous extensions to Maximum Independent Set and Minimum Vertex Cover sidestep this with tailored reduction rules that keep every subproblem within the original problem class. We resolve this by identifying, for a given constraint structure, a broader problem class that is closed under all eliminations, and by efficiently constructing feasible initial states and feasibility-preserving mixers for every class member. We do so for monotone constraints, such as for the knapsack problem, for linear equality constraints with polynomially bounded weights, including Hamming weight constraints, and for combinations of equality constraints with a single inequality constraint, such as the cardinality-constrained knapsack problem. Conversely, we show that these restrictions cannot be lifted in general without leaving the realm of efficient constructions. Exact simulations on knapsack and vertex-weighted max-bisection instances demonstrate that our recursive scheme can outperform both its non-recursive counterpart and penalty-based QAOA and RQAOA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.17537) | 2026-11-16
