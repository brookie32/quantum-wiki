---
title: "Efficient expectation value estimation for quantum circuits via extended stabilizer frameworks and adaptive variance estimation"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14252"
summary: "arXiv:2609.14252v1 Announce Type: new Abstract: Classical simulability of quantum circuits plays a central role in characterizing and quantifying quantum computational advantage. Typically, the presen"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14252v1 Announce Type: new Abstract: Classical simulability of quantum circuits plays a central role in characterizing and quantifying quantum computational advantage. Typically, the presence of non-Clifford gates introduces an exponential runtime overhead for classically estimating expectation values of observables. In this work, we introduce an efficient simulation framework that integrates the sum-over-Clifford method with quasi-probability-based stabilizer simulation to directly estimate expectation values. To optimize efficiency, we incorporate a circuit-adaptive reduction via variance estimation protocol, which terminates simulations once an empirical confidence bound is sufficient to guarantee the prescribed error tolerance. Our method circumvents overly conservative Hoeffding's inequality, thereby reducing the dependence on the gate-wise stabilizer extent from quadratic to linear in the low-variance regime, while maintaining the same space complexity as previous approaches. We explicitly prove the sample-complexity reduction for random quantum circuits and T-doped Clifford circuits and also empirically validate these advantages in the quantum approximate optimization algorithm and quantum kernel method.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14252) | 2026-09-15
