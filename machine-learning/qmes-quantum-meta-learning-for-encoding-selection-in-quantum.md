---
title: "Qmes: Quantum Meta-Learning for Encoding Selection in Quantum Kernel Methods"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.04652"
summary: "arXiv:2609.04652v1 Announce Type: new Abstract: Selecting an effective encoding quantum circuit is a key challenge in quantum kernel methods because different feature maps can lead to different perfor"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.04652v1 Announce Type: new Abstract: Selecting an effective encoding quantum circuit is a key challenge in quantum kernel methods because different feature maps can lead to different performance. Conventional methods require constructing and evaluating every circuit for each new dataset, making it computationally expensive. We present Qmes, an open-source Python package that automatically recommends circuits through meta-learning. Qmes characterizes a dataset using classical complexity measures and queries a pre-trained model to recommend circuits without quantum evaluation at inference time. The package provides modular components for meta-feature extraction, quantum-kernel evaluation, recommender training, model selection, and user-defined circuit extension. We validate Qmes on 105 classification and 86 regression benchmark datasets. Qmes reduces the mean recommendation regret by 2.2x and 4.2x for classification and regression, respectively, compared to a non-adaptive baseline, with statistical significance confirmed via a paired Wilcoxon signed-rank test (p < 10^{-4}). Qmes thus enables efficient and practical encoding-circuit selection for quantum kernel methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.04652) | 2026-09-07
