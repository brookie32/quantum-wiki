---
title: "Causal Query Compression for Lindblad Dynamics: Optimal Queries and Nearly Linear Local Simulation"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31312"
summary: "arXiv:2609.31312v1 Announce Type: new Abstract: We construct a causal query compiler for time-dependent Lindblad dynamics and establish query and gate bounds under distinct input models. With coherent"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31312v1 Announce Type: new Abstract: We construct a causal query compiler for time-dependent Lindblad dynamics and establish query and gate bounds under distinct input models. With coherent block encodings of the Hamiltonian and individual jump operators, a Lipschitz generator can be simulated to diamond-norm error arepsilon using O(1+au+log(1/arepsilon)/log(e+log(1/arepsilon)/au)) controlled queries, where au=T(alpha_H+sum_mualpha_mu^2). This bound is independent of the time-grid size and is worst-case optimal for auge1. Weak active entry and clean return yield a factorial history tail; combining two reuse lengths removes the auxiliary input. A three-call polar correction supplies the Lindblad cells. The compiler also characterizes the minimum oracle action of bounded adaptive Markovian protocols by quantum query complexity and the general adversary bound, up to constant factors. For finite-range dynamics on n lattice sites, efficient coherent evaluation of the local matrices and fixed local parameters give O(n(T+1)operatorname{polylog}X) elementary gates, where X=max{e,n(T+1)(1+K_t+B)/arepsilon}, for piecewise Holder generators with fixed exponent, local variation bound K_t, and at most B breakpoints per term. The jumps need not commute. This gate bound includes evaluation, arithmetic, selection, routing, and environment storage. Its proof combines a spatial decomposition on a common bath, compilation on occupied inputs, and routing on compressed records. Reusing bath storage between short segments gives depth (T+1)operatorname{polylog}X and space noperatorname{polylog}X.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31312) | 2026-09-28
