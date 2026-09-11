---
title: "Periodic Symmetry-Adapted Encoding: Qubit Reduction in Crystalline Electronic Structure"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.05777"
summary: "arXiv:2606.05777v2 Announce Type: replace Abstract: We introduce periodic symmetry-adapted encoding (SAE) for qubit-efficient simulations of crystalline materials, extending the molecular SAE framewor"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2606.05777v2 Announce Type: replace Abstract: We introduce periodic symmetry-adapted encoding (SAE) for qubit-efficient simulations of crystalline materials, extending the molecular SAE framework developed in earlier work to periodic systems. The method constructs a Gamma-point supercell active-space Hamiltonian from k-point Hartree-Fock data and identifies independent Boolean symmetry generators arising from spin parity, crystal translations, and point-group operations. Each generator removes one qubit while preserving the Hamiltonian spectrum in the target symmetry sector. The inclusion of crystal translations increases the maximum number of independent generators, and hence the number of removable qubits, from five in molecular SAE to eight in periodic SAE. Across ten crystals spanning cubic, hexagonal, trigonal, and tetragonal structures, the method removes four to eight qubits. In CsCl, all eight generators are realised, reducing CAS(6,7) from 14 qubits to 6. Complete-spectrum comparisons verify target-sector isospectrality, while noiseless UCCSD-VQE reaches the fixed-particle FCI energies throughout the suite. The resulting circuits reduce unoptimised logical CNOT counts by up to 99.7% relative to the full Jordan-Wigner encoding. The method is implemented in the open-source QuantumSymmetry package.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.05777) | 2026-09-11
