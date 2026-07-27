---
title: "Graph-Theoretic Neural Network Fragmentation with Covariant Direct Molecular Force Learning: Enabling Coupled-Cluster Accuracy AIMD for Fluxional Systems"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.21779"
summary: "arXiv:2607.21779v1 Announce Type: new Abstract: Accurate ab initio molecular dynamics (AIMD) simulations of complex, fluxional chemical systems are severely limited by the high computational scaling o"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.21779v1 Announce Type: new Abstract: Accurate ab initio molecular dynamics (AIMD) simulations of complex, fluxional chemical systems are severely limited by the high computational scaling of correlated electronic structure methods. To overcome this bottleneck, we present a robust, graph-theoretic molecular fragmentation framework integrated with machine learning to directly model post-Hartree-Fock nuclear forces at coupled cluster accuracy. Bypassing the limitations of automatic differentiation on learned energy surfaces that may struggle with link-atom Jacobians, our approach directly predicts nuclear force vectors. By projecting these vectors onto fragment-fixed principal axes of inertia, we establish co-variant descriptors that naturally preserve rotational, translational, and permutational invariance. The methodology achieves exceptional high parameter efficiency through a vector-valued training protocol that reduces trainable parameters by over an order of magnitude, while an unsupervised mini-batch k-means space tessellation algorithm constructs highly representative training databases using only 10% to 20% of reference configurations. We rigorously validated this framework on the highly fluxional solvated Zundel cation H_{13}O_6^+ ). Our fully machine-learning-predicted AIMD trajectories successfully reproduced complex dynamical signatures and key structural characteristics, including radial distribution functions and the velocity autocorrelation power spectrum. Ultimately, this scalable, systematically improvable framework bridges the gap between high-level correlated wavefunction theories and long-timescale reactive sampling, laying the foundation for advanced, LLM-inspired transfer learning in modern chemical dynamics simulations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.21779) | 2026-07-27
