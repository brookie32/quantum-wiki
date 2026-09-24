---
title: "Certifying fermionic Gaussian states (and a little more) with optimal precision dependence"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28233"
summary: "arXiv:2609.28233v1 Announce Type: new Abstract: Fermionic Gaussian states are the workhorse reference states for qubit-based quantum simulation of fermionic systems, yet existing certification protoco"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28233v1 Announce Type: new Abstract: Fermionic Gaussian states are the workhorse reference states for qubit-based quantum simulation of fermionic systems, yet existing certification protocols either proceed via fidelity estimation, leading to suboptimal sample complexity in the target precision epsilon, only apply to Haar-typical states, or require adaptive measurements on a large fraction of qubits. We give an adaptive protocol that certifies any d-mode pure fermionic Gaussian state using O(d^2epsilon^{-1}) copies, single-qubit measurements with only one qubit measured adaptively per copy, and O(d^3) classical processing time per copy. The epsilon^{-1} dependence is optimal for the certification problem, even among strategies using entangled measurements. The sample complexity is controlled by the spectral gap of a dleftrightarrow d-2 down-up walk---a Markov chain studied in the theory of high-dimensional expanders, equivalent to a two-site Glauber dynamics in statistical physics---relating certification efficiency to relaxation time to equilibrium. The worst-case bound is tight for this protocol and is attained by physically relevant states, including ground states of the fully dimerized Su-Schrieffer-Heeger (SSH) chain and BCS pair states. In contrast, numerics up to d=14 suggest that O(d epsilon^{-1}) copies suffice to certify Haar-typical Gaussian states, a factor of d improvement over the worst-case bound. Finally, because the bound depends only on the target's computational-basis distribution, the protocol extends to efficiently phase-dressed states---states obtained by injecting an efficiently computable diagonal phase to Gaussian states---with the same sample complexity. The class includes a continuous family of four-mode non-Gaussian magic states for matchgate computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28233) | 2026-09-24
