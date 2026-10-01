---
title: "Accelerating Quantum Dense-Output Simulation through Locality"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40094"
summary: "arXiv:2609.40094v1 Announce Type: new Abstract: Estimating time-accumulated observables, or dense outputs, is central to extracting classical information from quantum simulations. Whereas most quantum"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40094v1 Announce Type: new Abstract: Estimating time-accumulated observables, or dense outputs, is central to extracting classical information from quantum simulations. Whereas most quantum-simulation algorithms aim to reproduce a final state or a single-time expectation value, many applications require the integrated signal J_H(O)=int_0^T langle psi(t)|O(t)|psi(t)rangle,dt. Previous Hamiltonian-simulation-based dense-output algorithms have query costs that depend on the norm of the full Hamiltonian, which can grow with system size. However, one can naturally optimize the simulation algorithm when the system structure is known. Consequently, we develop a locality-based truncation framework for the dense-output problem on lattice Hamiltonians. By truncating the Hamiltonian and tightening the resulting error with Lieb-Robinson bounds, we show that a local simulation can recover the dense output. We bound the quantum simulation error from spatial truncation and translate it into local-simulation query bounds. Our analysis includes free and interacting systems for both fermions and bosons, as well as open quantum systems governed by Lindbladians. The improvement from our truncation algorithm varies from constant to unbounded as the system size grows. We also give example applications and conduct relevant numerical experiments to support our findings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40094) | 2026-10-01
