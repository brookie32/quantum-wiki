---
title: "Shot-based quantum encoding: a data-loading paradigm for quantum neural networks"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.06135"
summary: "arXiv:2604.06135v2 Announce Type: replace Abstract: Efficient data loading remains a bottleneck for near-term quantum machine learning. Existing schemes (angle, amplitude, and basis encoding) either u"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2604.06135v2 Announce Type: replace Abstract: Efficient data loading remains a bottleneck for near-term quantum machine learning. Existing schemes (angle, amplitude, and basis encoding) either underuse the exponential Hilbert-space capacity or require circuit depths that exceed the coherence budgets of noisy intermediate-scale quantum hardware. We introduce shot-based quantum encoding (SBQE), a data embedding strategy that distributes the hardware's native resource, shots, according to a data-dependent classical distribution over multiple initial quantum states. By treating the shot counts as a learnable degree of freedom, SBQE produces a mixed-state representation whose expectation values are linear in the classical probabilities and can therefore be composed with nonlinear activation functions. We show that SBQE is structurally equivalent to a multilayer perceptron whose weights are realized by quantum circuits, and we describe a hardware-compatible implementation protocol. Benchmarks on three image datasets, with 10 independent initializations per model, show that SBQE achieves 89.1% +- 0.9% test accuracy on Semeion (reducing error by 5.3% relative to amplitude encoding and matching a width-matched classical network), 80.95% +- 0.10% on Fashion MNIST (exceeding amplitude encoding by +2.0% and a linear multilayer perceptron by +1.3%), and 90.25% +- 0.18% on MNIST (exceeding amplitude encoding by 2.1 percentage points and the width-matched classical network by 0.3), all without any data-encoding gates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.06135) | 2026-07-30
