---
title: "Best Annealing Path of Quantum Annealing via Efficient Adiabatic Phase Transition"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.30282"
summary: "arXiv:2608.30282v1 Announce Type: new Abstract: Quantum Annealing (QA) has already put into practical use and considered useful for solving many social issues, such as reduction of traffic congestion "
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.30282v1 Announce Type: new Abstract: Quantum Annealing (QA) has already put into practical use and considered useful for solving many social issues, such as reduction of traffic congestion and delivery optimization. But in QA, when the energy difference between the ground state and the first excited state is small, the transition probability between them increases. Therefore, in order to decrease the transition, QA has to be performed at extremely low temperatures. To simulate the situation, it has the problem in that it takes much time. Many studies are underway to accelerate QA theoretically, one of which is to incorporate non-stoquastic Hamiltonian. On the other hand, I proposed Nested Simulated Annealing (NSA) inspired by Quantum Monte Carlo (QMC). I showed the computational speedup could be achieved dramatically, by considering the idea that the effect of flipping a spin preferentially influenced the spins directly interacting with it. Although NSA was based on such classical concept of causality, the hybrid computation both quantum and classical approach worked well. In this paper, in order to discuss the relationship between NSA and non-stoquastic Hamiltonian like XX-interaction, the spins are treated as continuous variables. I derive the formula to calculate the total energy in both with a problem Hamiltonian and the perturbation Hamiltonian induced by a transverse electromagnetic field. And I will show a clear relationship between local-maxima and the convergence speed when calculating it with the binary spin. More precisely, the annealing path with the smallest local-maxima converges fast, even though it consumes fewer computational resources. Therefore, it is possible to induce an optimal adiabatic phase transition by selecting NSA parameters appropriately. This paper shows an effective method to choose the parameters when simulating QMC on a classical computer.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.30282) | 2026-09-01
