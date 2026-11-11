---
title: "A New Computational Model for the Spin-Free Sum-of-Squares Energy Bounds of Electronic Hamiltonian"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14319"
summary: "arXiv:2611.14319v1 Announce Type: cross Abstract: Optimizing spin-free sum-of-squares (SOS) energy bounds for electronic Hamiltonians leads to semidefinite programs whose expanded size grows rapidly w"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14319v1 Announce Type: cross Abstract: Optimizing spin-free sum-of-squares (SOS) energy bounds for electronic Hamiltonians leads to semidefinite programs whose expanded size grows rapidly with the orbital dimension. We derive an exact reformulation of an established spin-free SOS model as a convex quadratic problem over a single symmetric matrix constrained between zero and the identity. Explicit recovery maps connect feasible quadratic-program iterates to certificates in the original SOS formulation, and identify the Frank--Wolfe gap with the separation between recovered primal and dual objectives. We implement the quadratic action through GPU-accelerated Coulomb contractions and solve the reformulated problem using a cached implementation of fully corrective Frank--Wolfe, referred to here as the dimension-reduced simplicial method (DRSM) that caches operator products and optimizes convex-combination weights in a small corrective quadratic program. Numerical experiments cover 65 FCIDUMP models, molecular geometries, and regular hydrogen rings, including original-coordinate recovery checks on nine instances and comparisons with FISTA and a boundary-point SDP solver. On eight H100 GPUs, a cold-start calculation for C_{720} with 10,080 spatial orbitals reaches a freshly recomputed Frank--Wolfe gap of 8.82imes10^{-9} hartree in 5.02 hours. Full-space hydrogen-ring calculations reach 10,000 orbitals, with cyclic reduction providing further computational savings. These results show how exact reformulation, data structure exploitation and reuse of Coulomb actions make optimization of the selected large-scale SOS relaxation practical.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14319) | 2026-11-11
