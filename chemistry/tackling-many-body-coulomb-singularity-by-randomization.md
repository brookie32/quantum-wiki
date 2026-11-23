---
title: "Tackling Many-Body Coulomb Singularity by Randomization"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27851"
summary: "arXiv:2611.27851v1 Announce Type: new Abstract: Many-body Coulomb dynamics is central to quantum chemistry and molecular simulation, yet the Coulomb singularity undermines both the standard error anal"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27851v1 Announce Type: new Abstract: Many-body Coulomb dynamics is central to quantum chemistry and molecular simulation, yet the Coulomb singularity undermines both the standard error analysis and performance of product formulas. Even for the simple hydrogen ground state, the celebrated Trotter formulas converge more slowly than their nominal order, and going to higher order does not help. Randomization by itself does not resolve this. We show that conventional qDRIFT suffers the same loss of accuracy, and that for general initial states, the errors of both Trotter formulas and qDRIFT can decrease more slowly than any power of the number of time steps (logarithmically). To overcome these limitations, we introduce supersmoothing qDRIFT, a randomized product formula that turns a physical property of free particle propagation into an algorithmic resource. Our algorithm achieves an error bound that decreases linearly with the time step, uniformly over extit{all} initial states and without any smoothness or energy assumptions. Combined with spatial discretization analysis, the resulting end-to-end gate count improves on those of qubitization and high-order Trotter formulas applied directly to the discretized Hamiltonian, despite first-order convergence in time. This work demonstrates new ways of utilizing continuum dynamics to achieve algorithmic advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27851) | 2026-11-23
