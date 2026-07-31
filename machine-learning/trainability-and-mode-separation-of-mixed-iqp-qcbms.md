---
title: "Trainability and Mode Separation of Mixed IQP-QCBMs"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.27883"
summary: "arXiv:2607.27883v1 Announce Type: new Abstract: Quantum circuit Born machines (QCBMs) based on instantaneous quantum polynomial-time (IQP) circuits are promising quantum generative models for their cl"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.27883v1 Announce Type: new Abstract: Quantum circuit Born machines (QCBMs) based on instantaneous quantum polynomial-time (IQP) circuits are promising quantum generative models for their classical trainability. It is known that their ancilla-free form avoids barren plateaus under certain initializations, but remains non-universal. Although adding ancilla qubits raises the expressivity, whether the ancilla-extended model retains local trainability remains unknown. We propose the mixed IQP-QCBM, which generalizes the ancilla-extended circuit as a weighted mixture of ancilla-free IQP circuits, called branches. For a polynomial number of branches, we prove local barren-plateau avoidance from data-agnostic and, under certain assumptions, data-dependent initializations. We further show that the mixed IQP-QCBM can surpass the best ancilla-free IQP circuit only if its branches generate a number of distinct distributions. In particular, we focus on a behavior we call mode separation, in which each branch captures a particular feature of the target. Mode separation is hard to attain from an initialization whose branches generate the same distribution: the gradients that would separate them are suppressed while the distributions they generate remain close. This motivates cluster initialization, which assigns a different unsupervised data cluster to each branch and provides an initial degree of mode separation. Exact calculations on two 16-bit datasets support the barren-plateau and gradient-suppression claims. On four benchmarks, binary clusters, a two-dimensional Ising model, binarized MNIST, and a 484-spin glass, cluster initialization converges fastest and reaches the lowest mean test MMD^2. We observe that, when achieving the lowest test MMD^2, the mixed IQP-QCBM contains branches specialized to distinguishable data features such as blob patterns, magnetization sectors, or digit shapes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.27883) | 2026-07-31
