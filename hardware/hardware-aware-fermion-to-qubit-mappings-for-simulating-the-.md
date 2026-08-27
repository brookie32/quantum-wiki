---
title: "Hardware-Aware Fermion-to-Qubit Mappings for Simulating the 2D Hubbard Model on Heavy-Hexagon Quantum Processors"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.25024"
summary: "arXiv:2608.25024v1 Announce Type: new Abstract: Quantum simulation of strongly correlated fermionic systems is among the most promising near- term applications of quantum computing, but its practical "
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2608.25024v1 Announce Type: new Abstract: Quantum simulation of strongly correlated fermionic systems is among the most promising near- term applications of quantum computing, but its practical efficiency depends critically on the choice of fermion-to-qubit mapping and on the connectivity of the underlying hardware. In this work we address this problem in the context of the two-dimensional Hubbard model, simulated on IBM superconducting quantum processors with heavy-hexagon connectivity. We numerically benchmark the Jordan-Wigner, Bravyi-Kitaev, and Bonsai transformations, evaluating their Pauli weight and SWAP overhead across seven heavy-hexagon chips of increasing size. We show that, while the Bravyi-Kitaev mapping initially exhibits a lower Pauli weight, this advantage is eliminated once routing costs are taken into account, confirming the Bonsai mapping as the most hardware-efficient baseline transformation for this architecture. We then use the Bonsai mapping to construct the qubit Hamiltonian of the 2D spinful Fermi-Hubbard model, introducing a simulated annealing algorithm that optimizes the assignment of Majorana strings to lattice sites, reducing the cost function by nearly 50% percent. Finally, we simulate on quantum hardware the time evolution of fermionic states up to 6x6 lattices, confirming the viability of the Bonsai encoding for hardware-aware large-scale two-dimensional simulations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.25024) | 2026-08-27
