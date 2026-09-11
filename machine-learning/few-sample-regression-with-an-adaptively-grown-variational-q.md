---
title: "Few-sample regression with an adaptively grown variational quantum Kolmogorov--Arnold network"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.21336"
summary: "arXiv:2503.21336v4 Announce Type: replace Abstract: Kolmogorov-Arnold networks place learnable one-dimensional functions on the edges of a network rather than fixed activations on its nodes, and sever"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2503.21336v4 Announce Type: replace Abstract: Kolmogorov-Arnold networks place learnable one-dimensional functions on the edges of a network rather than fixed activations on its nodes, and several quantum realisations have been proposed. Whether any of them offers a practical benefit is unclear, because the reported comparisons rest on single training runs, untuned baselines, and test sets that were also used for model selection. Here we evaluate a variational quantum Kolmogorov-Arnold network whose ansatz is grown one Pauli operator at a time, under a protocol with seed-paired comparisons, a stopping rule that never sees the test set, and a confirmatory study whose hypotheses, seeds, and analysis were committed before the runs. On four-qubit benchmarks the model is indistinguishable from a quantum neural network of the same parameter count and is outperformed by classical regressors. On a difficulty-controlled family of 12- and 16-dimensional targets learned from ten training points, the 32-parameter quantum model beats the best of four unregularised classical regressors and a tuned quantum neural network with Holm-corrected p <= 0.017; the result is unchanged with 256 measurement shots per circuit, and the trained models run on a 156-qubit IBM processor with test errors within 0.3 of the exact values. A kernel ridge regressor with hyperparameters chosen by leave-one-out cross-validation on the same ten points matches the quantum model, and a sample-size sweep shows that the quantum model's error is nearly flat in the training-set size while the classical models keep improving. The benefit of the quantum model is therefore an implicit regularisation of a low-capacity model, present only in the few-sample regime and absent at 18 dimensions, not an expressivity advantage. These results give a reproducible reference point for the resources and limits of variational quantum Kolmogorov-Arnold networks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.21336) | 2026-09-11
