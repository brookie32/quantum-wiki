---
title: "Tree-Structured Commutativity Packing in Adaptive Variational Quantum Simulation: Measurement Overhead and Representation Limits"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.13387"
summary: "arXiv:2606.13387v2 Announce Type: replace Abstract: While fermion-to-qubit isomorphisms are mathematically invariant under exact unitary statevector transformations, their physical implementation on n"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2606.13387v2 Announce Type: replace Abstract: While fermion-to-qubit isomorphisms are mathematically invariant under exact unitary statevector transformations, their physical implementation on noisy intermediate-scale quantum (NISQ) devices introduces severe, practical measurement bottlenecks. In this work, we systematically investigate the measurement efficiency of adaptive derivative-assembled pseudo-trotter variational quantum eigensolver (ADAPT-VQE) algorithms across three critical molecular benchmarks (LiH, BeH2, and H2O) at stretched bond lengths (2xRe) covering distinct point-group symmetries. First, we establish exact representation invariance across all target multi-reference geometries, demonstrating that operator pool gradients and statevector electronic energies remain strictly isomorphic under exact mathematical execution (E(LiH) = -7.691469 Ha, E(BeH2) = -15.110110 Ha, and E(H2O) = -74.566874 Ha). Second, we quantify the hardware measurement overhead by partitioning operator pool observables into qubit-wise commuting (QWC) tensor-product basis (TPB) cliques. We reveal that while both Jordan-Wigner (JW) and Bravyi-Kitaev (BK) encodings yield identical total Pauli term counts across the singlet excitation manifold (128 terms for H2O and BeH2), the hierarchical binary-tree layout of the BK mapping dramatically compresses the required measurement circuits---achieving up to a 45.31% reduction in total hardware execution steps compared to 12.50% under JW. Our findings demonstrate that tree-structured mappers serve as implicit, highly efficient measurement-packing engines for adaptive quantum simulations without altering the underlying variational trajectory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.13387) | 2026-08-04
