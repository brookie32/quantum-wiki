---
title: "Characterizing Large Scale Quantum Systems with Error Per Circuit Layer"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.04132"
summary: "arXiv:2609.04132v1 Announce Type: new Abstract: Quantum benchmarks provide compact measures of performance that are important for evaluating and comparing quantum systems. Circuit-level benchmarks are"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.04132v1 Announce Type: new Abstract: Quantum benchmarks provide compact measures of performance that are important for evaluating and comparing quantum systems. Circuit-level benchmarks are particularly valuable because they capture the accumulated effects of noise across interacting operations, but existing approaches may require structured gate sets and costly compilation, classical simulation of reference outputs, or subsystem decompositions that do not capture full-register behavior. We introduce Error Per Circuit Layer (EPCL), an overlap-based circuit-level benchmark that estimates an effective layer polarization by applying identical random circuits to two disjoint quantum registers and measuring the overlap between their output states as a function of circuit depth. EPCL avoids classical simulation of ideal output distributions and recovery to a known reference state, and is compatible with arbitrary gate sets, including non-Clifford gates. We derive the expected overlap decay under an ensemble-averaged depolarizing model and identify the assumptions under which the fitted decay parameter represents an effective layer polarization. Numerical simulations show that EPCL recovers the predicted polarization under weak local stochastic noise and remains well described by a single-exponential decay at stronger stochastic noise levels. The simulations further show that coherent errors associated with fixed entangling layers may require Pauli twirling or randomized compiling to produce the expected decay, while inter-register correlations contribute an additional covariance term to the measured overlap. Finally, experiments on IBM quantum hardware demonstrate clear EPCL decay in 8- and 16-qubit implementations. These results support EPCL as a method for measuring aggregate register performance without requiring classical simulation of ideal circuit outputs or restriction to structured gate sets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.04132) | 2026-09-04
