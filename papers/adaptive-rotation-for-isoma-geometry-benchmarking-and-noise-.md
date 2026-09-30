---
title: "Adaptive Rotation for iSOMA: Geometry, Benchmarking, and Noise Robustness in Variational Quantum Objectives"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37193"
summary: "arXiv:2609.37193v1 Announce Type: cross Abstract: We study whether the coordinate dependence of the improved Self-Organizing Migrating Algorithm (iSOMA) can be reduced while retaining its inexpensive "
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37193v1 Announce Type: cross Abstract: We study whether the coordinate dependence of the improved Self-Organizing Migrating Algorithm (iSOMA) can be reduced while retaining its inexpensive leader-directed migration mechanism. We introduce iSOMA-AR, which learns a basis from successful migration displacements and selectively applies the standard perturbation mask in that basis. On the complete noiseless BBOB suite, iSOMA- AR significantly outperformed baseline iSOMA across matched conditions, with the largest gains on geometrically difficult landscapes. A targeted ablation shows that the learned orientation is beneficial on a rotated ill-conditioned landscape and that moderate changes of the gate threshold and rotation cap preserve the qualitative result. On CEC 2011 Real World Optimization Problems, iSOMA-AR outperformed iL-SHADE on most problems, although its advantage over baseline iSOMA was not statistically significant. A canonical-jSO rerun is reported as a post-hoc sensitivity check alongside the original jSO-derived comparator. On frustrated-spin variational quantum objectives, adaptive rotation improved most transverse-field conditions, while gains on the diagonal and anisotropic models were absent or selective. Under strong effective sampling noise, the SOMA variants were the most robust population-based methods in the comparison, but iSOMA-AR was not significantly better than baseline iSOMA. Repairing all-zero PRT masks greatly reduced repeated-point evaluations without changing endpoint quality significantly, making this implementation detail unlikely to explain the noise result. Overall, adaptive rotation is most useful on coordinate-sensitive deterministic problems, while the observed noise robustness appears to arise mainly from the underlying SOMA migration mechanism.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37193) | 2026-09-30
