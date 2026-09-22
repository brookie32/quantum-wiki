---
title: "Experimental evidence of generalization in quantum machine learning in small-data regime"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.24666"
summary: "arXiv:2609.24666v1 Announce Type: new Abstract: Quantum machine learning is a promising paradigm for learning from limited data, a central bottleneck in domains such as medical imaging, clinical trial"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.24666v1 Announce Type: new Abstract: Quantum machine learning is a promising paradigm for learning from limited data, a central bottleneck in domains such as medical imaging, clinical trials, and rare diseases. Quantum convolutional neural networks (QCNNs) are particularly attractive in this setting, combining a hierarchical architecture with strong inductive bias and a parameter count that grows only logarithmically with system size. Their appeal rests on the generalization bounds of Caro et al. (2022), which show that the generalization error of a quantum model scales with the number of trainable parameters rather than with the Hilbert-space dimension, placing QCNNs in a potentially sample-efficient regime. We develop a hardware-compatible QCNN with mid-circuit measurement and classical feed-forward, and show on a binary handwritten-digit task that strong test performance is achievable from as few as 10 training samples, with the generalization error decreasing as the training set grows. At a matched 45-parameter budget the QCNN learns where an equally small classical convolutional network stays at chance, although an unconstrained classical baseline with roughly 25,000 parameters remains strongest when data are plentiful. Transpiling amplitude and angle encoded circuits across image resolutions from 2x2 to 512x512 pixels then exposes the dominant scaling bottleneck: amplitude encoding stays qubit-efficient but grows extremely deep, whereas angle encoding stays shallow but becomes qubit-prohibitive. On the medically motivated BreastMNIST benchmark the QCNN does not surpass the unconstrained classical network, yet it learns consistently above chance using orders of magnitude fewer parameters. Our results indicate that for QCNNs, learning from few samples is attainable in practice, whereas scaling to realistic image data is constrained less by optimization than by data encoding and hardware execution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.24666) | 2026-09-22
