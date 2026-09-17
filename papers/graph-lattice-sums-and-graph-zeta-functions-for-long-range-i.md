---
title: "Graph lattice sums and graph zeta functions for long-range interacting quantum lattice models"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.18918"
summary: "arXiv:2609.18918v1 Announce Type: cross Abstract: Taming the exponential increase of the Hilbert space dimension with system size in the simulation of gapped quantum lattice models is of the highest r"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18918v1 Announce Type: cross Abstract: Taming the exponential increase of the Hilbert space dimension with system size in the simulation of gapped quantum lattice models is of the highest relevance for understanding and designing exotic quantum materials, where nonlocal interactions are of particular interest. High-order linked-cluster expansions provide access the solution of the eigenvalue problem for the infinite system, yet rely on the computation of high-dimensional oscillatory lattice sums with a graph structure, only approachable with Monte Carlo methods so far. This work resolves this issue, rendering all required graph lattice sums, referred to as graph zeta functions for kernels involving power-laws, computable. The resulting method reduces the evaluation time for state-of-the art series expansions from tenthousands of core-hours to minutes. After factorizing the lattice sum over blocks, each block is evaluated by the cheapest available strategy depending on its treewidth tw. Basic blocks admit analytic forms in terms of generalized zeta functions. Series-parallel blocks with twle 2 can be computed at linear cost in the number of graph nodes and in the size of the momentum grid using a semi-analytical algebra based on Epstein zeta functions and rapidly decaying Fourier series. Finally, for tw>2, the method is combined with tensor-network bucket elimination yielding polynomial scaling of numerical work and memory in momentum grid size with exponents only growing with tw rather than with the number of vertices. Through use of FFT, the full momentum grid is recovered at the cost of a single momentum evaluation. We provide a detailed analysis of the precision and runtime of our method against analytic and numerical benchmarks. We further reproduce published Monte Carlo data for the transverse-field Ising model on different 1D, 2D, and 3D lattices, obtaining full agreement.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.18918) | 2026-09-17
