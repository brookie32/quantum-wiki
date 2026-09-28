---
title: "Modeling quantum neural network gradient with reinforcement learning"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31066"
summary: "arXiv:2609.31066v1 Announce Type: new Abstract: Training quantum neural networks (QNNs) on near-term hardware remains hampered by two compounding difficulties: the exponential vanishing of gradient va"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31066v1 Announce Type: new Abstract: Training quantum neural networks (QNNs) on near-term hardware remains hampered by two compounding difficulties: the exponential vanishing of gradient variance known as the barren plateau, and the O(L dot 2^n) time and memory cost of differentiating through an n-qubit, L-layer circuit. We propose RLQ-Grad, a reinforcement-learning-based optimizer in which a classical policy pi_phi (a spectrally-normalized PPO agent) learns to propose parameter updates directly, conditioned on the QNN's current parameters, loss, accuracy, and previous update. Because the surrogate gradient is emitted by a classical network rather than obtained by differentiating through the unitary U(heta), its variance is not constrained by the barren plateau concentration bound, and its cost scales with the number of trainable parameters rather than the Hilbert-space dimension. We prove these properties formally and verify them on a hardware-efficient ansatz across four supervised benchmarks with up to n=20 qubits. RLQ-Grad preserves a near-flat gradient-variance curve where backpropagation, parameter-shift, and adjoint differentiation decay by 1 to 2 orders of magnitude. Accounting for the full training pipeline (PPO rollouts, actor-critic updates, and optimizer states), RLQ-Grad needs under 2 MB of memory and runs 2490imes, 7876imes, and 673imes faster per iteration than these three methods at n=20. It improves top-1 accuracy by up to +10% over gradient-based baselines on circuits of up to 12 qubits, and matches dedicated barren plateau mitigation methods on CIFAR-10 at 14 to 20 qubits, where evolutionary and gradient-free optimizers collapse to chance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31066) | 2026-09-28
