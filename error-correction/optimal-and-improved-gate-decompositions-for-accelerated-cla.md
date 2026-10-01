---
title: "Optimal and improved gate decompositions for accelerated classical simulation of near-Gaussian fermionic circuits"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.18869"
summary: "arXiv:2603.18869v2 Announce Type: replace Abstract: Fermionic Gaussian circuits can be simulated efficiently on a classical computer, but become universal when supplemented with non-Gaussian operation"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2603.18869v2 Announce Type: replace Abstract: Fermionic Gaussian circuits can be simulated efficiently on a classical computer, but become universal when supplemented with non-Gaussian operations. Similar to stabilizer circuits augmented with non-stabilizer resources, these non-Gaussian circuits can be simulated classically using rank- or extent-based methods. These methods decompose non-Gaussian states or operations into Gaussian ones, with runtimes that scale polynomially with measures of non-Gaussianity such as the rank and the extent -- quantities that typically grow exponentially with the number of non-Gaussian resources. Current fermionic rank- and extent-based simulators have mostly been limited to Gaussian circuits with magic-state injection. Extending them to mixed states and non-unitary channels has been hindered by the lack of known extent-optimized decompositions for physically relevant gates and noisy channels. In this work, we address this gap. First, we derive analytic decompositions for key non-Gaussian gates and channels, including decompositions for arbitrary two-qubit fermionic gates which are provably optimal for diagonal gates or those acting on Jordan-Wigner-adjacent qubit pairs. Second, we show that stochastic Pauli noise can reduce the effective extent of non-Gaussian rotation gates, but that fermionic magic is substantially more robust to such noise than stabilizer magic. Finally, we demonstrate how these decompositions can accelerate classical sampling from the output distribution of a quantum circuit. This involves a generalization of existing sparsification methods, previously limited to convex-unitary channels, to circuits involving intermediate measurements and feed-forward. Our decompositions also yield speedups for emulating noisy Pauli rotations with quasiprobability simulators in the large-angle/arbitrary-strength-noise and small-angle/low-noise parameter regimes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.18869) | 2026-10-01
