---
title: "Real-Space Chemistry on Quantum Computers: A Fault-Tolerant Algorithm with Adaptive Grids and Transcorrelated Extension"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2507.20583"
summary: "arXiv:2507.20583v2 Announce Type: replace Abstract: First-quantized, real-space formulations of quantum chemistry on quantum computers are appealing: qubit count scales logarithmically with spatial re"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2507.20583v2 Announce Type: replace Abstract: First-quantized, real-space formulations of quantum chemistry on quantum computers are appealing: qubit count scales logarithmically with spatial resolution, and Coulomb operators achieve quadratic instead of quartic computational scaling of two-electron interactions. However, existing schemes employ uniform discretizations, so the resolution required to capture electron-nuclear cusps in high-density regions oversamples low-density regions, wasting computational resources. We address this by deploying non-uniform, molecule-adaptive grids that concentrate points where electronic density is high. Using Voronoi partitions of these grids, the molecular Hamiltonian is expressed in a Hermitian form and in a transcorrelated, isospectral form that eliminates Coulomb singularities and yields cusp-free eigenfunctions. Both formulations slot naturally into quantum eigenvalue solvers: Hermitian Quantum Phase Estimation (QPE) and the recent generalised Quantum Eigenvalue Estimation (QEVE) protocol for its non-Hermitian, transcorrelated counterpart. Numerical validation on benchmark systems confirms that this non-heuristic ab initio framework offers a promising path for accurate ground-state chemistry on quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2507.20583) | 2026-10-07
