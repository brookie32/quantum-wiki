---
title: "Selected Coupled Cluster Guided by Selected Configuration Interaction"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10829"
summary: "arXiv:2609.10829v1 Announce Type: cross Abstract: Coupled Cluster (CC) theory is one of the most popular correlated wavefunction methods, yet the steep computational cost scaling of CC truncated at hi"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.10829v1 Announce Type: cross Abstract: Coupled Cluster (CC) theory is one of the most popular correlated wavefunction methods, yet the steep computational cost scaling of CC truncated at higher rank limits its application. Modern Selected Configuration Interaction (SCI) methods successfully exploit the sparsity of ground-state wavefunctions in the determinant space, motivating an analogous approach with the exponential CC ansatz. In this work, we introduce Selected Coupled Cluster (SCC), an arbitrary-order sparse CC method that explicitly solves the CC residual equations within a compact amplitude space guided by an SCI wavefunction. SCC optimizes the CC amplitudes in the sparse amplitude space. Using a pilot Just-in-Time (JIT) compiled implementation, we benchmark SCC against SCI, SCI+PT2, standard rank-truncated dense CC (CCSD, CCSDT), and DMRG across various chemical systems. We demonstrate that SCC exhibits fast, monotonic convergence with the SCI variational threshold, outperforming SCI and surpassing SCI+PT2 in the tight-threshold regime. SCC also provides accurate energies for high-dimensional topologies, where DMRG typically converges slowly with bond dimension. SCC thus presents an efficient drop-in enhancement for modern SCI workflows.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10829) | 2026-09-11
