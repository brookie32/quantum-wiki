---
title: "Quantum-walk transport oracles and amplitude estimation of a scalar range statistic in proton therapy"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13475"
summary: "arXiv:2611.13475v1 Announce Type: cross Abstract: Quantum amplitude estimation (QAE) promises a quadratic reduction in the sampling cost of Monte Carlo (MC) particle transport, but two obstacles have "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13475v1 Announce Type: cross Abstract: Quantum amplitude estimation (QAE) promises a quadratic reduction in the sampling cost of Monte Carlo (MC) particle transport, but two obstacles have kept it from radiotherapy physics: the lack of an efficient unitary encoding of charged-particle transport, and the mismatch between QAE's single-scalar output and the per-voxel structure of dose calculation. We address both. We construct a discrete-time quantum-walk transport oracle for protons in which an energy register is driven by an energy-dependent coin encoding a continuous-slowing-down surrogate of the stopping power, so that stochastic energy loss and range straggling follow from the circuit dynamics. The oracle is unitary, with one fresh coin qubit per step, and its gate count grows linearly in the number of energy levels. On it we formulate a scalar range statistic, the probability that a proton penetrates beyond a distal depth threshold, as a directly marked amplitude, and estimate it by maximum-likelihood amplitude estimation (MLQAE) with Grover iterations and finite shots. The oracle reproduces a Bragg-shaped depth-deposit profile agreeing with a classical MC of identical rules to within 0.27%, and Grover amplification matches sin^2((2k+1)heta) to machine precision up to k=32. At matched budget the MLQAE error falls as N^{-0.93} against N^{-0.49} for sampling, 4.8 times smaller at the largest budget. A three-gate resource analysis (output structure, amortization, error-corrected wall-clock) finds full dose maps structurally unfavourable irrespective of hardware, and the scalar statistic short of a wall-clock crossover at clinical scale: the oracle's derived cost of 1.0 imes 10^6 logical gates per call (3.5 imes 10^7 with rotation synthesis), dominated by the multiplexed coin, is 160 to 5400 times the permitted budget. We report the reduction that would be required and identify the term responsible for it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13475) | 2026-11-11
