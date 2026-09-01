---
title: "A priori Assessment of Tensor-Network Encoding for Isotropic Turbulent Flows"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.28869"
summary: "arXiv:2608.28869v1 Announce Type: cross Abstract: Tensor networks (TNs), originally developed for simulating many-body quantum systems, provide a systematic framework for approximating high-dimensiona"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.28869v1 Announce Type: cross Abstract: Tensor networks (TNs), originally developed for simulating many-body quantum systems, provide a systematic framework for approximating high-dimensional fields. This is achieved by factorizing the field into interconnected tensors with small bond dimensions, thereby restricting the correlations captured across field bipartitions. Belonging to the family of TNs, the matrix product state (MPS) ansatz is utilized here as a reduced-order modeling framework to construct truncated representations of isotropic turbulent flow data. Two direct numerical simulation (DNS) datasets are considered: the hydrodynamic field of an incompressible three-dimensional flow, and a conserved Fickian scalar in a similar flow. Each field is encoded as an MPS through a sequence of singular value decompositions (SVDs) in which small singular values are discarded. The truncated representation is contracted back to the full grid, and the resulting reconstructed field is compared against DNS. An interleaved ordering of the spatial tensor indices of the transport variables is applied prior to decomposition in order to localize the dominant inter-tensor correlations. Velocity reconstructions achieve 99.8% fidelity using only 5% of the original DNS memory, while the scalar field reaches the same fidelity at 15% memory usage. A wide range of lower- and higher-order statistics, including velocity gradients, dissipation, and structure functions, are systematically examined. At these compression levels, the total kinetic energy and the scalar energy are both recovered within 0.2% relative error, while the mean dissipation and mean scalar dissipation remain within approximately 10% of the DNS generated values. These findings support the suitability of MPS for scalable reduced-order analysis of complex turbulent datasets and motivate further exploration of TN-based methods in computational turbulence.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.28869) | 2026-09-01
