---
title: "Local and Multi-Scale Strategies to Mitigate Exponential Concentration in Quantum Kernels"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.16097"
summary: "arXiv:2602.16097v2 Announce Type: replace Abstract: Fidelity-based quantum kernels provide a direct interface between quantum feature maps and classical kernel methods, but they can exhibit exponentia"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2602.16097v2 Announce Type: replace Abstract: Fidelity-based quantum kernels provide a direct interface between quantum feature maps and classical kernel methods, but they can exhibit exponential concentration: with increasing system size or circuit expressivity, the Gram matrix approaches the identity and suppresses informative similarity structure. We present an empirical study of two mitigation strategies implemented in Qiskit: (i) local (patch-wise) kernels that aggregate subsystem similarities, and (ii) multi-scale kernels that mix local and global similarity across patch granularities. We benchmark baseline, local, and multi-scale kernels under matched preprocessing, splits, and SVM protocols on several tabular datasets, sweeping the feature dimension din{4,6,ots,20}. We report concentration diagnostics based on off-diagonal kernel statistics, spectral richness via effective rank, and centered alignment with labels. Across datasets, local and multi-scale constructions consistently mitigate concentration and yield richer kernel spectra relative to the global fidelity baseline, while the impact on classification accuracy depends on the dataset and dimension.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.16097) | 2026-08-05
