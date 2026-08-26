---
title: "Scalable Lindblad Noise Learning via Stochastic Tensor-Network Simulation"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.24668"
summary: "arXiv:2608.24668v1 Announce Type: new Abstract: Learning dissipation rates in large-scale open quantum systems is a major obstacle for near-term quantum technologies, as existing Lindblad estimation m"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.24668v1 Announce Type: new Abstract: Learning dissipation rates in large-scale open quantum systems is a major obstacle for near-term quantum technologies, as existing Lindblad estimation methods are typically limited to small system sizes due to the computational complexity of repeatedly solving the Lindblad equation during optimization. Here, we propose a scalable noise-learning framework for Lindblad dissipation rates that combines a stochastic simulation method, the Tensor Jump Method (TJM), with gradient-free optimization of a least-squares cost-function defined on time series of local-observable expectation values. We demonstrate the approach on two noise models in the Ising model: a site-resolved (local) model, in which independent dissipation rates are learned for each site up to N_{site}=16, and a spatially homogeneous (global) model with only seven parameters, scaled to N_{site}=160 sites.We complement these numerical results with a series of exact, provable guarantees: the Frobenius variance of the TJM density-matrix estimator is shown to equal (1-Tr[rho^2])/N_{traj}, an exact purity-based characterization of the stochastic estimation error; the corresponding purity evolution is proven to be monotonically non-increasing for Hermitian jump operators; and, under a finite covariance distance assumption, the standard deviation of the cost-function is shown to decrease with system size, so that fewer trajectories are needed to reach a fixed target accuracy as the system grows. Together, this combination of scalable numerics and rigorous theoretical guarantees positions TJM-based noise learning as a practical foundation for characterizing dissipation in large quantum devices and for guiding future work on error mitigation and quantum error correction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.24668) | 2026-08-26
