---
title: "Decay versus dephasing in Rydberg analog optimization: exchange rate, mechanism, and schedule design"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.29858"
summary: "arXiv:2608.29858v1 Announce Type: new Abstract: Numerical studies of noisy Rydberg-atom optimization almost universally compress decoherence into a single scalar, silently pricing spontaneous decay (G"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.29858v1 Announce Type: new Abstract: Numerical studies of noisy Rydberg-atom optimization almost universally compress decoherence into a single scalar, silently pricing spontaneous decay (Gamma) and dephasing (gamma) alike. We treat the two as independent axes, mapping a quantum-annealing heuristic for unit-disk maximum independent set on 20 random N=10 graphs across the (Gamma,gamma) plane, with the annealing time re-optimized at every point. The mean approximation ratio does collapse onto one scalar, but onto u=kappaGamma+gamma with kappa=8.05pm0.5 (stat) pm1.1 (syst); the isotropic Gamma+gamma fails by a factor of 30 in residual. First-order perturbation theory reproduces kappa from noiseless propagation alone and gives the mechanism: the objective is diagonal in the basis of the dephasing operator, so dephasing cannot change the answer once the drive is off, and a single driven atom already has kappasimeq8.5. The exchange rate is thus a property of the protocol as much as of the platform: the ramp-down fraction moves it between 2.3 and 16.3. At a fixed schedule it is stable across system sizes, interaction strengths, and estimators. Because the whole cost model is noiseless, a schedule can be tuned to a device's channel mixture without any noisy simulation: jointly tuning the drive ramp-down and the sweep's detuning ramp recovers about a third of the Markovian damage at no hardware cost, and the ramp the noise-aware objective selects is not the one noiseless optimization would choose. Per unit rate decay is eightfold the dearer channel, but the measured T_1 enters weighted by its branching ratio to the ground state (bapprox0.4 for the calibrated device), which leaves the two Lindblad channels comparably costly at a present-day operating point. One-parameter noise models remain serviceable, provided the parameter is u.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.29858) | 2026-09-01
