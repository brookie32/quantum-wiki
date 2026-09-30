---
title: "Fast Hamiltonian engineering from cut polytope geometry"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36006"
summary: "arXiv:2609.36006v1 Announce Type: new Abstract: Hamiltonian engineering (HE) simulates quantum dynamics under a target Hamiltonian using a native entangling system Hamiltonian and restricted control, "
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36006v1 Announce Type: new Abstract: Hamiltonian engineering (HE) simulates quantum dynamics under a target Hamiltonian using a native entangling system Hamiltonian and restricted control, with applications from quantum gate design to analog quantum simulation. Observing that, for many systems, formulating HE as a linear program only requires specific commutation relations between the control pulses and the system Hamiltonian, we provide a unified framework for broad classes of 2-local qubit, qudit, and fermionic systems. We reformulate time-optimal HE as a complex k-cut polytope problem, with k the number of distinct phases in these commutation relations, and prove it NP-complete for every finite k. We therefore relax the polytope to the elliptope and apply a Krivine-type rounding, yielding pulses informed by the system and target Hamiltonians, which we then use in a linear program. We derive how many informed pulses are necessary and sufficient for the linear program to be reliably feasible. Additionally mixing in uniformly sampled pulses guarantees a solution close to the relaxation value from O(m) pulses, with m the number of interaction terms. Together with upper and lower bounds on the optimal quantum run time, this yields an O(sqrt{m}) approximation ratio. In benchmarks on a fully connected Ising model, a chiral clock model for qudits, and the fermionic Harper-Hofstadter model, our approach attains near-optimal quantum run times wherever the optimum is computable, reaches run times that saturate with the lattice size in the fermionic case, and outperforms state-of-the-art methods with O(m) pulses. This establishes a unified approach with provable guarantees to the automatic programming of analog quantum simulators.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36006) | 2026-09-30
