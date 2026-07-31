---
title: "SymFT: Universal Fault-Tolerant Quantum Circuit Simulation via Symbolic Clifford--Pauli Frames and Stabilizer Coordinates"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28600"
summary: "arXiv:2607.28600v1 Announce Type: new Abstract: Fault-tolerant protocols often consist largely of stabilizer subcircuits, yet the non-Clifford operations required for universality make exact sampling "
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.28600v1 Announce Type: new Abstract: Fault-tolerant protocols often consist largely of stabilizer subcircuits, yet the non-Clifford operations required for universality make exact sampling costly. We present SymFT, a high-throughput simulator for Clifford-dominated circuits with Pauli rotations, stochastic Pauli noise, mid-circuit Pauli measurements, and measurement-record-controlled Pauli feedback. It combines two ideas. First, symbolic Clifford--Pauli frame factorization reduces branch-probability sampling to Pauli rotations and measurement projectors, with noise and feedback represented by symbolic signs. Since the residual Clifford and Pauli frames are unitary, they do not affect branch probabilities and need not be applied in every shot. Second, adaptive stabilizer-coordinate planning uses a shared stabilizer--destabilizer tableau to define the basis and stores only the active non-stabilizer degrees of freedom in a dynamically sized dense active-state vector. It resolves basis changes once and emits direct multi-coordinate sampling instructions, thereby avoiding per-shot tableau updates and localization-induced Clifford transformations of the dense vector. Across the tested pure-Clifford and near-Clifford circuits, SymFT achieves state-of-the-art sampling performance. On a single CPU core, it is 2.51ext{--}2.56imes faster than Stim for surface-code circuits and 1.86ext{--}3.51imes faster than Clifft for magic-state cultivation and distillation circuits. For the tested cultivation circuits, its sampling throughput also exceeds that of our previous simulator, SOFT, by more than two orders of magnitude.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28600) | 2026-07-31
