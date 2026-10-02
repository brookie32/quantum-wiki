---
title: "Continuous-Process Randomized Compilation for Quantum Process Tensors"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01521"
summary: "arXiv:2610.01521v1 Announce Type: new Abstract: Traditional discrete randomized compiling (RC) tailors errors with random control frames at logical-gate boundaries, but fails to capture intra-instrume"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01521v1 Announce Type: new Abstract: Traditional discrete randomized compiling (RC) tailors errors with random control frames at logical-gate boundaries, but fails to capture intra-instrument control evolution or persistent system-environment coupling. In memory-bearing environments, errors correlate across times, not just single gates. We build continuous-process randomized compilation (CPRC) in the continuous process tensor (cPT) framework, unifying random unitary control trajectories, pointwise-covariant finite-duration instruments, and environmental dynamics on one time axis. We study four protocols: fixed Pauli refresh, bounded Cayley paths, unitary Brownian motion, Ornstein-Uhlenbeck driving. We obtain three key results: (1) Pointwise covariance ensures each trajectory exactly reproduces the target logic without system-environment coupling; a closed-frame counterexample proves endpoint-only compensation causes first-order instrument errors. (2) Independent Pauli conjugations over full intervals diagonalize error histories at boundaries, but classical labels retain environment-induced correlations, confirmed by an exact static-bath solution. (3) We derive a total-variation error bound for full adaptive output records under bounded centered coupling and mixing conditions. We prove convergence of trajectory-averaged cPT coefficients in fixed particle sectors for finite non-Gaussian environments and Gaussian baths with time-integrable covariance, including the uncut Drude spectrum. We numerically validate the theory in a qubit model via output probabilities, operator conditional mutual information, and all two-particle coefficients for both qubit and thermal Drude baths. This work extends RC from discrete circuits to continuous-time memory-bearing quantum processes, offering a unified framework, quantitative tools, implementable schemes, and benchmarks for non-Markovian error tailoring.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01521) | 2026-10-02
