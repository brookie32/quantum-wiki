---
title: "Information-Calibrated Quantum Diffusion: Aligning Forward Noise with Reverse Recoverability"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14083"
summary: "arXiv:2608.14083v1 Announce Type: new Abstract: Quantum diffusion models typically parameterize forward corruption by raw channel strength, even though equal parameter increments need not erase equal "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14083v1 Announce Type: new Abstract: Quantum diffusion models typically parameterize forward corruption by raw channel strength, even though equal parameter increments need not erase equal information or induce comparable inverse problems. We introduce the classical--quantum information decrement Delta_t=I(X{:}Q_{t-1})-I(X{:}Q_t) as an intrinsic diffusion coordinate for labeled quantum ensembles. Along depolarization, equalizing Delta_t yields the unique minimax discretization of the forward path, while universal recoverability gives the same quantity an operational reverse interpretation as an attainable expected log-fidelity budget for a label-independent CPTP recovery channel. Complementary continuity and pairwise-geometric converses lower-bound the optimal common-channel recovery error. We further show that local calibration is fundamentally insufficient for stochastic generation: even in a fixed noncommuting two-qubit system, identical local-fidelity laws and budget-feasible risks can coexist with macroscopically different output distributions. This motivates a stochastic learner combining theorem-scaled recovery constraints with distribution matching, for which we establish finite-sample calibration and compositional trace-Wasserstein control. On four-qubit TFIM, a controlled capacity extension reduces endpoint Wtr from .622 to .424 on all ten matched seeds and achieves lower Wtr than official QuDDPM (.498) with fewer trainable parameters.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14083) | 2026-08-17
