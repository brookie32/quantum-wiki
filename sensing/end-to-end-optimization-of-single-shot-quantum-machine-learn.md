---
title: "End-to-end Optimization of Single-Shot Quantum Machine Learning for Bayesian Inference"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.20492"
summary: "arXiv:2512.20492v2 Announce Type: replace Abstract: We introduce an end-to-end optimization strategy for quantum machine learning that directly targets performance under finite measurement resources, "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2512.20492v2 Announce Type: replace Abstract: We introduce an end-to-end optimization strategy for quantum machine learning that directly targets performance under finite measurement resources, where learning objectives are defined directly at the level of task performance. The method is applied on a Bayesian quantum metrology task since it provides a natural testbed with known fundamental limits and scaling with system size. The sampling-aware hybrid algorithm achieves a single-shot risk within 1 dB of the -20 dB Bayesian limit using 32 qubits. We extend the Bayesian framework from parameter estimation to global function inference, where the task is to infer a target function of the sensor input drawn from an arbitrary prior, and we demonstrate a clear computational-sensing advantage for direct functional inference over indirect reconstruction. We relate the corresponding Bayesian risk to the Capacity metric and argue that the Resolvable Expressive Capacity provides a natural measure of the space of functions accessible in a single shot. The resulting eigentask analysis identifies noise-robust feature combinations that yield compact estimators with improved accuracy and reduced optimization cost in resource-limited or real-time on-device settings. Going beyond the irreducible statistical uncertainty associated with finite measurement records, we study implementation-induced distortions of the sensor response focusing on representative imperfections arising from readout errors and static coherent gate disorder. We show that when these imperfections are stationary across training and inference, end-to-end optimization can adapt the quantum circuit and classical estimator to the implemented hardware response, preserving high inference performance over a broad range of imperfection strengths.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.20492) | 2026-09-22
