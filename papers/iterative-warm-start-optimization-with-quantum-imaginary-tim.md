---
title: "Iterative warm-start optimization with quantum imaginary time evolution"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.26047"
summary: "arXiv:2604.26047v2 Announce Type: replace Abstract: Approximate combinatorial optimization is a promising use case for quantum computers. The quantum optimization algorithms often employ a fixed ansat"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2604.26047v2 Announce Type: replace Abstract: Approximate combinatorial optimization is a promising use case for quantum computers. The quantum optimization algorithms often employ a fixed ansatz that evolves an unbiased initial state towards states with better values of the optimand, then samples the states to determine an approximately optimal solution. However, promising alternative approaches have considered ``warm-start" and sampling-based methods that instead begin from the best known solution, which can be directly optimized with the quantum computer and updated as new information becomes available, potentially outperforming the fixed ansatze. Here we use these ideas to design a nonvariational quantum algorithm for combinatorial optimization. At each step the algorithm begins with a state superposed around the best known solution, then drives it to lower energy using quantum imaginary time evolution. These nonvariational, initial-state-dependent circuits are determined using analytic equations that are evaluated using only a conventional computer. After implementing the circuits, the state is sampled, potentially obtaining a new best-known solution to use as the initial state at the next iteration. Using simulations of the algorithm solving MaxCut on 3-regular graphs with 30 or fewer vertices and a shot budget of 100 total shots, the approach obtains median solutions within 95% of the global optimum and finds optimal solutions in 11% or more of cases, significantly outperforming random and simplified classical search procedures. We discuss several future directions.



## Related
- [[trading-imaginary-time-for-randomness-in-ground-state-prepar|Trading Imaginary Time for Randomness in Ground State Preparation]]
- [[ground-state-preparation-in-21-dimensional-pure-z2-lattice-g|Ground state preparation in (2+1)-dimensional pure Z_2 lattice gauge theory via deterministic quantum imaginary time evolution]]
- [[imaginary-time-evolution-and-ground-state-preparation-using-|Imaginary time evolution and ground state preparation using unitary multi-copy protocols]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.26047) | 2026-08-28
