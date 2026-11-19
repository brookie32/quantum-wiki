---
title: "Hurst Exponent Estimation with Quantum Wavelets"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24882"
summary: "arXiv:2611.24882v1 Announce Type: new Abstract: How accurately can the Hurst exponent H of fractional Brownian motion be estimated from repeated preparations of a single amplitude-encoded path, when e"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24882v1 Announce Type: new Abstract: How accurately can the Hurst exponent H of fractional Brownian motion be estimated from repeated preparations of a single amplitude-encoded path, when every measurement interrogates the same realization? We extend the epsilon-decimated quantum nondecimated wavelet transform in three directions: we remove the endpoint jump of circular filtering, derive the sampling distribution of the estimator, and compare readouts at equal query budgets. A one-qubit mirror extension removes the jump and keeps every coefficient that straddles a fold of the same order as an interior coefficient, for any compactly supported filter and circular shift. The transform for any such filter is compiled from the paraunitary lattice of its filter bank, and the energy share of a level is the success probability of one multiply-controlled reflection, which is both the controlled unitary of a Hadamard test and the oracle of amplitude estimation. For filters with at least two vanishing moments we prove a root-N central limit theorem for the log-energy contrasts, independent of the limiting path norm, so the studentized estimator is asymptotically standard normal for deterministic query budgets under which the success count at every level diverges. For sparse counts we give a working multinomial--lognormal likelihood, exact in its readout model for direct measurement, and check its coverage by simulation. For paths of length 512, mirroring reduces RMSE by a factor of 3--10 for Hge0.5, and with exact shares the nondecimated db2 estimator is 6--14% above the root Cramer--Rao bound. Hadamard level tests are less accurate than direct measurement of the leading qubits at every budget. At H=0.9 and 2^{20} queries, maximum-likelihood amplitude estimation attains RMSE 0.0347, against 0.0451 for direct measurement and 0.0295 with exact shares.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24882) | 2026-11-19
