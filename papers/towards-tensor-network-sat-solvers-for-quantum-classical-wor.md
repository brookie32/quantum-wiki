---
title: "Towards Tensor-Network SAT-Solvers for Quantum-Classical Workflows"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02041"
summary: "arXiv:2608.02041v1 Announce Type: new Abstract: Integrated HPC/QC systems aim to combine classical high-performance computing with quantum processors, but cannot be reduced to mechanisms for dispatchi"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.02041v1 Announce Type: new Abstract: Integrated HPC/QC systems aim to combine classical high-performance computing with quantum processors, but cannot be reduced to mechanisms for dispatching quantum kernels. An integrated architecture must support aspects such as observability, which cannot be implemented using QPUs alone, as well as fallback execution and cost-aware decisions on whether to replace quantum tasks with classical surrogates. Such mechanisms must be approximate or benefit from problem structure to soften the inescapable exponential classical worst-case complexity. In this work, we study tensor-network ground-state search, as such a surrogate, for optimisation problems. This combines key quantum primitives with advanced classical simulation. It provides initial empirical indicators for surrogate selection criteria, and exposes end-to-end toolchain effects that may be missed when transformation steps are studied in isolation. We compare a native polynomial unconstrained optimisation to-higher-order-Ising and a quadratised quadratic unconstrained binary optimization to-quadratic-Ising formulation for Max-3-SAT. Both are encoded as matrix product operator and optimised using density matrix renormalisation group approaches, with simulated annealing (SA) as classical performance baseline. Our results show that quadratisation is not a neutral transformation step: auxiliary variables and pairwise couplings substantially degrade solution quality relative to the native higher-order representation, while SA matches or outperforms DMRG across all tested instances. Since the optima of Boolean satisfiability (SAT)-derived problems are classical product states, DMRGs advantages dont materialise here. These findings suggest that surrogate selection in HPC/QC runtimes must be encoding- and instance-aware and provide empirical groundwork for informed decisions on fallback strategies and architecture co-design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02041) | 2026-08-04
