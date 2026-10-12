---
title: "NucleoNet: A Nuclear-Aware Determinant Ansatz for Multi-Geometry Neural Variational Monte Carlo"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.12985"
summary: "arXiv:2610.12985v1 Announce Type: new Abstract: Neural-network variational Monte Carlo provides an accurate route to solving the electronic Schrodinger equation, but many neural wavefunctions are opti"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.12985v1 Announce Type: new Abstract: Neural-network variational Monte Carlo provides an accurate route to solving the electronic Schrodinger equation, but many neural wavefunctions are optimized for a single nuclear geometry, requiring separate calculations to map out a potential energy surface. We introduce NucleoNet, a nuclear-aware determinant ansatz in which electrons and nuclei form a unified particle set propagated through a shared electron--nucleus backbone that jointly evolves one-particle and two-particle representations. Nuclei carry learned representations that evolve alongside the electronic representations and condition orbital construction, while antisymmetry is imposed only by electronic determinants. On equilibrium small-molecule benchmarks, NucleoNet achieves accuracy comparable to established neural-wavefunction baselines with substantially fewer parameters. For each molecular system, a single model optimized jointly across geometries describes the N_2 dissociation curve, Li displacement in LiCN, and the ethane and formamide minimum-energy paths for bond dissociation. Sparse-geometry training generalizes to unseen geometries for N_2 and LiCN without further optimization, and N_2 ablations show that nuclear streams substantially improve this interpolation. These results show that a compact wavefunction with jointly evolved nuclear representations can describe the geometries of a molecular system with a single set of parameters.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.12985) | 2026-10-12
