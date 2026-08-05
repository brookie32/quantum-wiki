---
title: "Inverse Design of Quantum Control Sequences with Fourier Neural Operators"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03702"
summary: "arXiv:2608.03702v1 Announce Type: new Abstract: Quantum optimal control is a key tool for steering quantum dynamics, but its computational cost grows rapidly with the Hilbert space dimension. Here, we"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03702v1 Announce Type: new Abstract: Quantum optimal control is a key tool for steering quantum dynamics, but its computational cost grows rapidly with the Hilbert space dimension. Here, we introduce a Fourier Neural Operator (FNO)-based framework for learning high dimensional molecular quantum dynamics and accelerating the inverse design of control protocols. Given an initial molecular population distribution, laser frequency, and polarization, the FNO predicts molecular-motional population dynamics up to 10^7 times faster than GPU-accelerated numerical propagation with CUDA-Q Dynamics. Using this fast and differentiable surrogate, we develop the FNO stochastic pulse-measurement planner (FNO-SPMP), which constructs pulse sequences to purify an initially mixed Boltzmann distribution. We demonstrate the protocol in an 888-dimensional subspace of the hydronium molecule at 20 K, achieving a target-state population of 0.98 with a sequence success rate of up to 86.2%. In a shared discrete control space, FNO-SPMP achieves nearly twice the success rate of a reinforcement-learning baseline while using roughly half as many quantum control pulses and reducing pulse-sequence generation time from approximately 10 hours to 10-20 minutes. These results show that operator-learning surrogates can enable inverse design in quantum systems whose Hilbert spaces are too large for conventional direct optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03702) | 2026-08-05
