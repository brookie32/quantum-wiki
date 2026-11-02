---
title: "Extending Sample-based Quantum Diagonalization to Systems of Linear Equations"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41708"
summary: "arXiv:2610.41708v1 Announce Type: new Abstract: Solving systems of linear equations, Ax=b, is a ubiquitous task in computational science. The Harrow-Hassidim-Lloyd algorithm requires phase estimation,"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41708v1 Announce Type: new Abstract: Solving systems of linear equations, Ax=b, is a ubiquitous task in computational science. The Harrow-Hassidim-Lloyd algorithm requires phase estimation, controlled rotations, and post-selection, impractical on noisy intermediate-scale quantum hardware. We extend sample-based quantum diagonalization (SQD), developed for quantum chemistry, to linear systems. Following the sample-based Krylov variant, the Hermitian matrix A is decomposed in the Pauli basis, the Trotterized time evolution of |brangle is sampled at several times to select computational-basis configurations, and the system is solved classically by a Galerkin projection onto the selected subspace. We prove that the subspace solution is exact when the sampled configurations contain the Krylov support of b and optimal in the energy norm for symmetric positive-definite matrices, so that noise-induced configurations cannot degrade it as long as they do not displace the ideal ones. On IBM Quantum hardware, the sampled distribution of a 4imes4 example deviates from the exact one by eleven times the shot-noise level, yet the solution is recovered exactly. For a localized problem of dimension N=1024, SQD selects 33 configurations, reaches a relative error of 10^{-5}, and its truncated subspaces coincide with the optimal choice; readout errors enlarge the subspace without degrading the accuracy. The tests also show the limitations: the selected subspace coincides with that of inexpensive classical selection, banded matrices require exponentially many Pauli terms in the binary encoding, and Trotter errors populate spurious configurations unless the circuits are deep. An MIT-licensed Python package and notebooks that reproduce the numerical results are provided.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41708) | 2026-11-02
