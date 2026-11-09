---
title: "Sign-hedged Beam QAOA:Scaling Quantum Optimization Algorithms"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08646"
summary: "arXiv:2611.08646v1 Announce Type: new Abstract: Quantum Approximate Optimization Algorithm (QAOA) encodes a combinatorial objective as an Ising Hamiltonian and alternates cost and mixer operations for"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08646v1 Announce Type: new Abstract: Quantum Approximate Optimization Algorithm (QAOA) encodes a combinatorial objective as an Ising Hamiltonian and alternates cost and mixer operations for p rounds. Recursive QAOA (RQAOA) scales further by using the resulting correlations, whether variables tend to agree or disagree, to eliminate variables one at a time. But each inferred sign is accepted irrevocably, so a single early mistake propagates through every later reduction and can discard the global optimum. As elimination proceeds, residuals shrink while effective edge density typically rises, so later decisions face denser Ising problems, a regime that fully connected Sherrington Kirkpatrick (SK) instances stress test directly. This paper proposes sign-hedged beam RQAOA, which retains the variable or pair selected by standard RQAOA, explores both possible sign assignments, keeps the best B residual problems according to a classical score, and completes each survivor with ordinary RQAOA. On frustrated SK instances, where standard recursion collapses to AR 0.474, beam recovers near-optimal AR 0.998 at the same p. We evaluate the workflow on 50+ instances from HamLib and QOBLIB, spanning 4 and 5 regular and Erdos Renyi MaxCut graphs, Sherrington Kirkpatrick (SK) spin glasses, and cardinality-constrained portfolio optimization, with up to 60 qubits and hardware runs on ibm kingston and ibm marrakesh. Matched simulator and device cells show consistent beam rankings: simulation and hardware agree that beam recovers near-optimal approximation ratio (AR) where standard recursion fails. These gains come from additional residual-circuit evaluations, classical pruning, and exact solution of a small core, rather than from increasing p, beam is a decision-side optimization atop fixed-p QAOA/RQAOA, not a claim that quantum circuits alone scale with qubit count.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08646) | 2026-11-09
