---
title: "Orbital-Rotation Shadow Tomography Reduces the Classical Cost of Quantum-Classical Auxiliary-Field Quantum Monte Carlo"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03103"
summary: "arXiv:2610.03103v1 Announce Type: new Abstract: Quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) is a promising route to using quantum computers for strongly correlated electronic stru"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03103v1 Announce Type: new Abstract: Quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) is a promising route to using quantum computers for strongly correlated electronic structure problems, but its scalability is limited by a classical post-processing bottleneck: the measured quantum trial state must be used to evaluate overlaps, force biases, and local energies for many walkers throughout the AFQMC propagation. Existing matchgate-shadow approaches avoid the exponential cost of generic classical shadows, but their post-processing remains expensive for large systems. In this work, we show that particle-number-preserving fermionic shadows, implemented as orbital-rotation shadows, are able to drastically reduce QC-AFQMC post-processing costs. We derive efficient estimators for overlaps and their derivatives, giving O(N^3) scaling for overlaps and force biases and O(N^4) scaling for local energies per shadow and walker and with O(N) Cholesky vector. For fixed normalized target determinants, we also prove that the overlap estimator is unbiased with variance upper bounded by O(eta), where eta is the particle number, yielding a sufficient budget of O(eta/epsilon^2) ideal independent measurements for additive overlap error epsilon. We combine these estimators with a novel virtual-correlation-energy treatment and a GPU implementation and demonstrate QC-AFQMC using orbital-rotation shadows. Performance projections for pi-conjugated molecules up to pentacene with a (22e, 22o) active space and 356 total orbitals show that the full classical post-processing workflow can be completed in slightly more than two days on 8imesA100 graphics processing units (GPUs). These results significantly reduce classical post-processing costs for QC-AFQMC and motivate further improvements in preparation and measurement of the trial state on quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03103) | 2026-10-05
