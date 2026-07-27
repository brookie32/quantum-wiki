---
title: "Parameterized Quantum Circuits as Feature Maps: Representation Quality and Readout Effects in Multispectral Land-Cover Classification"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.26675"
summary: "arXiv:2604.26675v2 Announce Type: replace Abstract: We investigate variational quantum classifiers (VQCs) for land-cover classification from multispectral satellite imagery, adopting a feature-map per"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2604.26675v2 Announce Type: replace Abstract: We investigate variational quantum classifiers (VQCs) for land-cover classification from multispectral satellite imagery, adopting a feature-map perspective in which the quantum circuit defines a nonlinear data embedding while the readout determines how this representation is exploited. Using the EuroSAT-MS dataset, we perform a systematic one-vs-one evaluation across all class pairs under a controlled experimental protocol, comparing classical baselines (logistic regression, SVMs, neural networks) with VQCs employing both linear readout and quantum-kernel SVM strategies. Our results show that, while VQCs with linear readout do not outperform strong classical baselines such as RBF-SVM, the same trained quantum feature map can significantly improve performance when reused within a kernel-based decision framework. A qubit-count sweep further reveals saturation effects consistent with the mismatch between exponential Hilbert space dimension and linear parameter scaling. Overall, our findings highlight that the effectiveness of quantum models depends critically on the interplay between representation and readout, and that meaningful gains may arise from combining learned quantum feature maps with classical decision mechanisms rather than seeking direct replacement of classical models.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.26675) | 2026-07-27
