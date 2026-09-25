---
title: "Quantum Computing Solution of the Bethe-Salpeter Equation for Relativistic Scalar Bound States via Tensor-Network VQE"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.24282"
summary: "arXiv:2609.24282v1 Announce Type: new Abstract: We present a gate-based quantum computing solution of the homogeneous Bethe-Salpeter equation (hBSE) for the bound state of two massive relativistic sca"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.24282v1 Announce Type: new Abstract: We present a gate-based quantum computing solution of the homogeneous Bethe-Salpeter equation (hBSE) for the bound state of two massive relativistic scalar particles interacting via ladder-approximation scalar exchange. After Wick rotation to Euclidean space and O(4) S-wave partial-wave projection, the hBSE is reduced to a symmetric matrix eigenvalue problem of dimension N = 2^n. We decompose the resulting Hamiltonian into a sum of n-qubit Pauli operators and solve it with the Variational Quantum Eigensolver (VQE) using a Matrix Product State (MPS) tensor-network ansatz. For N=16 (n=4 qubits), the VQE recovers the maximum eigenvalue - which encodes the minimum coupling constant for binding - to better than 1 % mean relative error compared to classical diagonalization. Entanglement analysis of the BSE amplitude shows low, area-law-like entanglement over the tested sizes, which motivates the MPS ansatz. A critical analysis of three independent barriers - exponential Pauli overhead, approximately size-independent low entanglement, and decreasing VQE gradient scales for the tested ansatz, consistent with generic barren-plateau concerns at larger n - reveals that the specific problem studied here lies in a classically tractable regime: over the tested range it is well described by low-bond-dimension tensor networks and efficiently handled by MPS/Lanczos methods. This negative result provides, to our knowledge, the first entanglement quantification of the BSE amplitude in qubit encoding, establishes the Pauli Hamiltonian framework for future BSE variants, and identifies 2D Minkowski-space BSE, N-body bound states, and non-ladder kernels as physically motivated extensions where genuine quantum advantage may become plausible.



## Related
- [[hamilton-zero-a-neural-tensor-network-foundation-model-for-g|Hamilton-Zero: A Neural Tensor-Network Foundation Model for Ground States of Arbitrary Quadratic Qubit Hamiltonians]]
- [[efficient-treatment-of-non-linearity-in-quantum-computationa|Efficient Treatment of Non-Linearity in Quantum Computational Fluid Dynamics Using Hybrid Tensor Networks]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.24282) | 2026-09-22
