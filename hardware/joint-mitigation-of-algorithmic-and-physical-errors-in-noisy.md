---
title: "Joint Mitigation of Algorithmic and Physical Errors in Noisy Hamiltonian Simulation"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11508"
summary: "arXiv:2609.11508v1 Announce Type: new Abstract: Product-formula Hamiltonian simulation is naturally suited to near-term quantum processors, but its accuracy is set by two competing errors: finite-step"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11508v1 Announce Type: new Abstract: Product-formula Hamiltonian simulation is naturally suited to near-term quantum processors, but its accuracy is set by two competing errors: finite-step Trotter bias and physical hardware noise. We introduce a joint extrapolation strategy that ties the tunable per-layer noise strength to the Trotter step size, lambda(s)=c(sT)^{p+1} for a p-th order product formula. Along this one-dimensional path, the leading physical-noise and Trotter corrections over the full evolution both enter at order s^p and can be canceled by a single Richardson extrapolation. Building on a previously established finite-order Baker--Campbell--Hausdorff truncation bound, we derive a provably commutator-scaling resource guarantee for the joint extrapolation. For local Hamiltonians with local Lindbladian noise, the protocol mitigates physical noise together with Trotter error with only a constant asymptotic overhead relative to noiseless Trotter extrapolation, provided the required noise strengths lie above the intrinsic device-noise floor. We experimentally demonstrate the protocol for Ising dynamics on a superconducting quantum computer using learned noise amplification. Complementary 100-qubit Sparse Pauli Dynamics (SPD) simulations achieve comparable accuracy to two-dimensional Richardson extrapolation with fewer circuit settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11508) | 2026-09-11
