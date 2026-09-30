---
title: "Optimized Randomized Hamiltonian Simulation via Average-Error Analysis"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36694"
summary: "arXiv:2609.36694v1 Announce Type: new Abstract: Hamiltonian simulation is a central application of quantum computing. Randomized Hamiltonian simulation approximates the target dynamics by sampling qua"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36694v1 Announce Type: new Abstract: Hamiltonian simulation is a central application of quantum computing. Randomized Hamiltonian simulation approximates the target dynamics by sampling quantum circuits and often allows simpler circuit implementations. We develop a framework for randomized Hamiltonian simulation in which Hamiltonian terms are sampled with arbitrary probabilities and the corresponding short-time evolutions are implemented sequentially. The leading channel error relative to ideal time evolution is governed by the variance of the sampled generators. Minimizing the variance-based upper bound on the worst-case error recovers qDRIFT, a leading randomized Hamiltonian simulation algorithm that samples terms in proportion to their operator norms. For typical input states, however, this sampling distribution need not be optimal. Minimizing Haar-averaged error bounds instead yields sampling probabilities proportional to the Hilbert-Schmidt norms of the terms. This choice can provide smaller average-error bounds than conventional qDRIFT. For Hamiltonians expressed as sums of Pauli strings, we combine this framework with commuting Pauli grouping to obtain smaller error bounds than conventional qDRIFT at fixed R_z depth. Numerical benchmarks for the Sachdev-Ye-Kitaev model show error-bound improvement factors consistent with linear scaling in the number of qubits. For the 108-qubit FeMoco Hamiltonian, the error bounds are reduced by a factor of about 5.65. These results establish average-error optimization as a practical design principle for randomized Hamiltonian simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36694) | 2026-09-30
