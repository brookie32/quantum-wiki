---
title: "Highly Parallel Real-Space Random Phase Approximation Using Lanczos Quadrature and Interpolation"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.16408"
summary: "arXiv:2609.16408v1 Announce Type: cross Abstract: We present a highly parallelizable, matrix-free, real-space method for computing the random phase approximation (RPA) correlation energy within Kohn-S"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16408v1 Announce Type: cross Abstract: We present a highly parallelizable, matrix-free, real-space method for computing the random phase approximation (RPA) correlation energy within Kohn-Sham density functional theory. In particular, we avoid the explicit construction and eigen-decomposition of the response function matrix and use Lanczos quadrature to evaluate the trace of a matrix function on a real-space grid. We also show it is possible to exploit the spatial smoothness of the RPA correlation energy density in real-space to reduce computational cost. Specifically, we compute the energy density on a coarse grid, then reconstruct an approximation to the full, fine grid via interpolation. We implement this formulation within the SPARC electronic structure package and demonstrate its convergence, accuracy, agreement with planewave results, and scaling. Interpolation can enable an 8imes reduction in the computational prefactor. Given the embarrassingly parallel nature of the proposed method, we achieve near-ideal speedups and near-cubic scaling, thus allowing us to compute the RPA correlation energy for a silicon system with 256 valence electrons at chemical accuracy in less than 30 minutes on 4,096 CPU cores.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.16408) | 2026-09-16
