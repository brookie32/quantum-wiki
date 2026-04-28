---
title: "Constant Factor Analysis of Optimal Quantum Linear Solvers in Practice"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.22185"
summary: "arXiv:2604.22185v2 Announce Type: replace Abstract: Optimal quantum linear equation solvers provide complexity O(kappalog(1/epsilon)), where kappa is the condition number and epsilon is the allowable "
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.22185v2 Announce Type: replace Abstract: Optimal quantum linear equation solvers provide complexity O(kappalog(1/epsilon)), where kappa is the condition number and epsilon is the allowable error. The optimal solver using a discrete adiabatic approach [PRX Quantum 3, 040303 (2022)] has large analytically proven constant factors for the upper bound on the complexity. The constant factors were later found to be about 1,200 times smaller in numerical testing [Quantum 9, 1887 (2025)]. This meant it is about an order of magnitude more efficient than using a randomised approach from [PRX Quantum 6, 040373 (2025)], which has far smaller analytically proven constant factors. Recently, a ``Shortcut'' method has been found to provide an optimal solver which also has small proven constant factors. In the present work, we conduct a comprehensive numerical analysis comparing this method with the adiabatic solver for two families of random linear systems. We find that, in the case where the solution norm is unknown, the adiabatic solver provides slightly better performance. If the solution norm is known, then the shortcut method provides significantly better performance for non-Hermitian matrices.



## Related
- [[symplectic-perspective-to-quantum-computing-for-hamiltonian-|Symplectic perspective to quantum computing for Hamiltonian systems]]
- [[quantum-algorithm-for-solving-high-dimensional-linear-stocha|Quantum algorithm for solving high-dimensional linear stochastic differential equations via amplitude encoding of the noise term]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.22185) | 2026-04-28
