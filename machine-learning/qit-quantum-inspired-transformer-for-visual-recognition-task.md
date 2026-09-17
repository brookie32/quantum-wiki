---
title: "QiT: Quantum-Inspired Transformer for Visual Recognition Task"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.17789"
summary: "arXiv:2609.17789v1 Announce Type: new Abstract: Quantum machine learning offers a compelling representational perspective: angle-encoded states inhabit Hilbert spaces in which periodic similarities an"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.17789v1 Announce Type: new Abstract: Quantum machine learning offers a compelling representational perspective: angle-encoded states inhabit Hilbert spaces in which periodic similarities and interactions can be expressed naturally. Realizing this perspective for visual recognition remains difficult, however, because present quantum neural networks are constrained by limited qubit counts, costly circuit simulation and measurement, noise, and unstable optimization on noisy intermediate-scale quantum devices. We investigate whether useful structural ideas from quantum models can instead be realized as scalable classical Transformer operations. We introduce QiT, a Quantum-inspired Transformer for vision tasks with three components: (i) angle-inspired encoding that maps image tokens to learned trigonometric Hilbert-space features analogous to quantum rotation-based state encoding; (ii) self-attention over these periodic features, inducing a classical cosine kernel approximated to quantum fidelity kernels; and (iii) gated multiplicative emulation, a trainable classical surrogate for interaction terms found in variational circuits. All components are differentiable tensor operations, so QiT claims neither quantum computation nor quantum speedup and retains the O(N^2D) attention complexity of a standard Vision Transformer. Across image-classification benchmarks, QiT is competitive with a matched classical Transformer while avoiding the severe runtime cost observed for a small simulated quantum Transformer. QiT-B reaches 78.3% ImageNet-1K top-1 accuracy with 45.7M parameters and 11.5 GFLOPs. These results position QiT as a scalable baseline for isolating and evaluating quantum-motivated inductive biases in visual recognition.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.17789) | 2026-09-17
