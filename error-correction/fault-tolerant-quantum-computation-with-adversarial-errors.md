---
title: "Fault-Tolerant Quantum Computation with Adversarial Errors"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16857"
summary: "arXiv:2608.16857v1 Announce Type: new Abstract: We prove a fault-tolerance theorem for quantum computation against adversarial noise. For every quantum circuit on ar{N} logical qudits of depth ar{T}, "
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16857v1 Announce Type: new Abstract: We prove a fault-tolerance theorem for quantum computation against adversarial noise. For every quantum circuit on ar{N} logical qudits of depth ar{T}, we construct a fault-tolerant circuit on N=ext{poly}(ar{N}) physical qudits of depth ar{T}dotar{N}^{o(1)}, which is robust against an adversary who may arbitrarily choose and corrupt an almost-linear number N^{1-o(1)} of physical qudits at each time step. This robustness significantly improves upon prior fault-tolerance theorems, which assumed corruptions were either local and stochastic, or else only act on a polynomially vanishing fraction of qudits. Our fault-tolerance scheme addresses a key bottleneck towards constructing quantum PCPs via the circuit-to-Hamiltonian mapping of Anshu, Breuckmann, and Nguyen (STOC'24). More fundamentally, our result demonstrates that fault-tolerant quantum computation remains possible under noise models that are global, worst-case, and non-Markovian over the full duration of the computation, directly countering concerns that correlated noise could fundamentally undermine quantum fault tolerance. Our construction is based on a new family of subsystem product codes we develop, which have large dimension and distance along with low-weight parity-checks, and which support transversal non-Clifford gates. We show how to perform single-shot fault-tolerant error correction on these codes using a Floquet-like procedure based on the local testability of classical tensor codes. We then obtain a universal fault-tolerance scheme using repeated code switching in a hypercubic qudit architecture. Finally, we recursively compose our scheme with itself to reduce an initially exponential qudit dimension down to a constant.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16857) | 2026-08-18
