---
title: "Phase-Drift Limits and Adaptive Quadrature Readout in Programmable Photonic Processors"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02249"
summary: "arXiv:2608.02249v1 Announce Type: cross Abstract: Phase fluctuations between optical inputs limit programmable photonic processors because their output powers depend on coherent interference. We study"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.02249v1 Announce Type: cross Abstract: Phase fluctuations between optical inputs limit programmable photonic processors because their output powers depend on coherent interference. We study the phase-drift penalty that arises when sine and cosine quadratures are measured sequentially rather than simultaneously. The analysis is motivated by measurements from an eight-mode programmable photonic processor, including 35 free-running recordings of 300 s acquired at approximately 125 samples per second per channel. These recordings provide an empirical route for estimating the phase-increment variance at a selected reconfiguration interval. The estimate is defined at the time of the second measurement. For fixed quadrature order, perturbation of the atan2 reconstruction gives e_{Co S}=-elta_ausin^2phi_0+O(elta_au^2) and e_{So C}=-elta_auos^2phi_0+O(elta_au^2). Writing Q_au=operatorname{Var}(elta_au), uniform phase averaging gives the first-order drift mean-square error 3Q_au/8. A phase-predicted ordering rule measures the locally less informative quadrature first and the more informative quadrature second. Its uniform first-order penalty is (3/8-1/pi)Q_au, which is 84.9 percent below the fixed-order value. We also derive an increment-aware estimator from a local state-space model. Marginalizing the unknown phase increment increases the variance of a stale phase observation by Q_au, reducing its Fisher information from I to I/(1+IQ_au). For ideal balanced Poisson detection, the Fisher information of each quadrature equals its detected signal-photon number. This yields dimensionless architecture boundaries in spatial information and phase-increment variance. Nonlinear Monte Carlo simulations validate the perturbative laws, quantify robustness to prediction error, and compare simultaneous, fixed-order, increment-aware, and adaptive receivers under a common noise model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02249) | 2026-08-04
