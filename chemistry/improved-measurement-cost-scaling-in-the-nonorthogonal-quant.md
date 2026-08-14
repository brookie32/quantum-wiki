---
title: "Improved Measurement Cost Scaling in the Nonorthogonal Quantum Eigensolver"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12830"
summary: "arXiv:2608.12830v1 Announce Type: new Abstract: Quantum subspace diagonalization methods are promising algorithms for quantum chemistry on near-term quantum computers. These methods can estimate low-l"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12830v1 Announce Type: new Abstract: Quantum subspace diagonalization methods are promising algorithms for quantum chemistry on near-term quantum computers. These methods can estimate low-lying energies of molecular systems using shallow quantum circuits, at the cost of many circuit repetitions to estimate the projected matrix elements. Errors in these matrix elements can be converted into much larger eigenvalue errors by an ill-conditioned overlap matrix. We study this bottleneck for the nonorthogonal quantum eigensolver (NOQE), which constructs a compact multireference subspace from dressed unrestricted Hartree-Fock states. We prove a finite-shot perturbation bound showing that, after overlap thresholding, the eigenvalue sensitivity is controlled by the condition number of the retained overlap matrix rather than by a worst-case dimension factor. With a scalable thresholding scheme, the upper bound on the per-matrix-element shot count required to reach a target accuracy scales as O(M), improving on the previously known O(M^3) bound, where M is the number of reference states. Numerical experiments on hydrogen chains and rings suggest that, in practice, the measurement cost of structured NOQE instances can grow even more slowly than this linear bound.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12830) | 2026-08-14
