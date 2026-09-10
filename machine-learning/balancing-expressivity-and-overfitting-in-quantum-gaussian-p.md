---
title: "Balancing Expressivity and Overfitting in Quantum Gaussian Process Regression"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.09407"
summary: "arXiv:2609.09407v1 Announce Type: new Abstract: Active learning is a paradigm of machine learning that can be utilized to model expensive black-box functions by training a surrogate model from activel"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09407v1 Announce Type: new Abstract: Active learning is a paradigm of machine learning that can be utilized to model expensive black-box functions by training a surrogate model from actively queried training points. The performance of this framework depends heavily on the choice of the surrogate model. When the surrogate is Gaussian Process Regression (GPR), its performance is largely determined by the expressivity of the underlying kernel. In this work, we investigate the peculiarities of using a quantum kernel to change the computational dynamics of active learning with GPR, focusing on the sensitivity to regularization by hyperparameter tuning. While generic, unstructured kernels suffer from exponential concentration at large scale, we empirically demonstrate that even at small scale overfitting can collapse GPR performance. Kernel regularization can be used to counteract this effect, but due to the smoothness of the quantum fidelity kernel, regularization must be carefully chosen to balance expressivity and overfitting. Our qualitative results transfer to the practical application of restricted quantum kernels designed to avoid exponential concentration and also present the kinds of noise that may be valuable to kernel training in near-term quantum devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.09407) | 2026-09-10
