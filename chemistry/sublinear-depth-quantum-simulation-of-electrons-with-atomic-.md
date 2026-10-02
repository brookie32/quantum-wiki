---
title: "Sublinear-depth Quantum Simulation of Electrons with Atomic Orbitals"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00950"
summary: "arXiv:2610.00950v1 Announce Type: new Abstract: Discretizing electronic degrees of freedom into atomic orbitals is the default choice to accurately model electrons in molecules in a compact and flexib"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00950v1 Announce Type: new Abstract: Discretizing electronic degrees of freedom into atomic orbitals is the default choice to accurately model electrons in molecules in a compact and flexible way. We consider the task of simulating such electronic structure models on a quantum computer for N orbitals, keeping the number of orbitals per atom constant. Atomic orbitals give rise to Hamiltonians with potentially up to O(N^4) terms and little structure, which made it challenging to match the complexity of methods based on plane waves and real-space grids. In this work, we show that a Trotter step for atomic orbitals can be implemented in depth O(polylog(N)) without ancillas by combining a rigorous treatment of orbital localization, a hierarchical Hamiltonian decomposition based on the Fast Multipole Method, and shallow quantum Fourier arithmetic circuits. By bounding the Trotter error, we obtain sublinear simulation depth, and our total gate count N^{5/3 + o(1)} matches the best scaling known for any basis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00950) | 2026-10-02
