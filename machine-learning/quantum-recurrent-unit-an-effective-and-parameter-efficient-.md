---
title: "Quantum Recurrent Unit: An Effective and Parameter-Efficient Quantum Neural Network Architecture for NISQ Devices"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.18164"
summary: "arXiv:2601.18164v3 Announce Type: replace Abstract: The rapid growth of modern machine learning models presents fundamental challenges in parameter efficiency and computational resource requirements. "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2601.18164v3 Announce Type: replace Abstract: The rapid growth of modern machine learning models presents fundamental challenges in parameter efficiency and computational resource requirements. We introduce the Quantum Recurrent Unit (QRU), a novel quantum neural network architecture specifically designed to address these challenges while maintaining compatibility with Noisy Intermediate-Scale Quantum (NISQ) devices. QRU leverages quantum controlled-SWAP (C-SWAP) gates to implement an information selection mechanism inspired by classical Gated Recurrent Units (GRUs), enabling selective processing of temporal information through quantum operations. The architecture features a measurement results feedforward scheme with shared parameters across time steps, achieving a constant parameter count and constant per-step effective quantum circuit depth (the depth of the effectively executed quantum circuit incurred over a single QRU time step) regardless of input sequence length. We validate QRU's performance through three progressive experiments under statevector simulation: oscillatory behavior prediction, high-dimensional feature classification of the Wisconsin Diagnostic Breast Cancer (WDBC) dataset, and MNIST handwritten digit classification. Across all tasks, QRU achieves 46.2%-99.7% parameter reduction compared to classical counterparts while achieving comparable performance. Preliminary hardware inference experiments on IBM quantum processors provide initial evidence of execution feasibility on real NISQ devices. The architecture's quantum-native design points toward a candidate quantum-native alternative to classical neural network components, offering a promising direction for parameter-efficient quantum machine learning as hardware capabilities and error mitigation techniques continue to improve.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.18164) | 2026-11-11
