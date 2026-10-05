---
title: "Root-sparsity scaling for Hamiltonian simulation, differential equations and linear-system solvers"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02939"
summary: "arXiv:2610.02939v1 Announce Type: new Abstract: We give quantum algorithms for Hamiltonian simulation, linear differential equations, and linear systems with square-root dependence on sparsity. For an"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02939v1 Announce Type: new Abstract: We give quantum algorithms for Hamiltonian simulation, linear differential equations, and linear systems with square-root dependence on sparsity. For an s-sparse Hermitian matrix with row and column Euclidean norms bounded by eta, evolution for time t to error epsilon uses O(sqrt{s}au+sqrt{saulog(1/epsilon)}+log(1/epsilon)) queries, where au=eta|t|. The same bound holds for time-dependent Hamiltonians with coherent time-indexed sparse access and certified time discretisation. Our construction combines an exact entrywise representation with Cayley transducers. A joint lower bound nearly matches the time, sparsity, and precision dependence, ruling out a uniformly additive bound in sqrt{s}au and log(1/epsilon). For dissipative linear differential equations we obtain O(ar g[sqrt{s}(au+sqrt{au})+1]log(Car g/epsilon)) queries, where au is the evolution time multiplied by a norm bound, ar g bounds the ratio of combined input and source norms to the final-solution norm, and C is an absolute constant. We sharpen this bound by separating Hamiltonian and dissipative components, and treat general constant generators. Lower bounds capture joint parameter dependence for time-dependent equations and precision hardness for constant positive semidefinite dissipation. For linear systems, a Cayley walk and Chebyshev filter give O(kappasqrt{s}log(1/epsilon)) queries when |A|le1 and |A^{-1}|lekappa, and we give an alternative proof of a matching joint lower bound. We also give gate-efficient implementations of time-independent Hamiltonian simulation and the dissipative ODE solver, including Lipschitz time dependence, retaining the query bounds with polylogarithmic overhead in inverse precision given efficient entry decoding, arithmetic, and required source preparations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02939) | 2026-10-05
