---
title: "Physics-Constrained Compressed Sensing for Quantum Sensing in the Data-Starved Regime"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11092"
summary: "arXiv:2608.11092v1 Announce Type: new Abstract: Quantum sensors promise measurement sensitivities that can scale at the Heisenberg limit, but in practice their performance is often degraded by noise, "
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2608.11092v1 Announce Type: new Abstract: Quantum sensors promise measurement sensitivities that can scale at the Heisenberg limit, but in practice their performance is often degraded by noise, finite sampling, and implementation imperfections. In this work we present a general framework for improving parameter estimation in such settings by exploiting intrinsic structural constraints of time-domain correlation functions. Our approach builds on the observation of Kemper et al. [PRL 132, 160403 (2024)] that two-time correlation functions of Hermitian observables generate Gram matrices that are positive semidefinite, a property that can be violated in experimentally acquired data. We formulate signal reconstruction as a convex optimization problem that enforces positive semidefiniteness, Toeplitz structure, and low-rank priors motivated by the underlying dynamics. We show analytically that, under suitable conditions, the ground-truth signal can be uniquely identified in the noiseless case and recovered stably in the presence of noise. We further demonstrate numerically, in a GHZ-based magnetometry protocol, that enforcing these physical constraints can significantly improve frequency estimation from sparse and noisy data. In particular, we observe a clear advantage in the data-starved regime, where only a small number of time samples are available and standard spectral estimation methods, including matrix pencil techniques, provide limited or unstable improvement over direct fitting. While the reconstructed signals do not in general reach the shot-noise-limited performance, the proposed approach consistently reduces estimation error and recovers much of the underlying structure of the signal. These results indicate that incorporating universal physical constraints into data analysis can enhance the practical performance of quantum sensing protocols without requiring additional hardware resources or calibration.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11092) | 2026-08-12
