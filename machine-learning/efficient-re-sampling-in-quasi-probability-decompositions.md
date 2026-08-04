---
title: "Efficient re-sampling in quasi-probability decompositions"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02075"
summary: "arXiv:2608.02075v1 Announce Type: new Abstract: Near-term quantum devices are limited by noise and hardware constraints, motivating algorithmic approaches that trade circuit complexity for increased s"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.02075v1 Announce Type: new Abstract: Near-term quantum devices are limited by noise and hardware constraints, motivating algorithmic approaches that trade circuit complexity for increased sampling overhead. Quasi-probability decompositions (QPDs), for example, allow replacing non-local operations by multiple circuits with local operations, but the associated sampling overhead generally scales exponentially and limits their practicality. In this work, we introduce a reweighting strategy for QPDs for circuits with the same variational structure across parameter settings, reusing samples and thereby reducing the sampling overhead. We first demonstrate this approach by estimating fidelities between parameterized quantum states, a key primitive in variational time evolution and quantum kernel methods. Importantly, this setup allows controlling the exponential QPD sampling overhead while preserving the structure of the state-encoding ansatz. We then apply the method to estimate the real part of the quantum geometric tensor using the simultaneous perturbation stochastic approximation and find that, in the presence of realistic hardware noise, our method outperforms other standard estimation techniques. These results highlight the potential of reweighting strategies to extend the applicability of QPD-based methods in variational quantum algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02075) | 2026-08-04
