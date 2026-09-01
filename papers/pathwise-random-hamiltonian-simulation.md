---
title: "Pathwise Random Hamiltonian Simulation"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.29756"
summary: "arXiv:2608.29756v1 Announce Type: new Abstract: Randomized product formulas such as qDrift offer a resource-efficient alternative to deterministic Trotter--Suzuki decompositions for Hamiltonian simula"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.29756v1 Announce Type: new Abstract: Randomized product formulas such as qDrift offer a resource-efficient alternative to deterministic Trotter--Suzuki decompositions for Hamiltonian simulation, removing their polynomial dependence on the number of Hamiltonian terms. qDrift, however, is intrinsically limited to first order in the evolution time, so its query complexity remains linear in the inverse of the target accuracy, 1/epsilon. We introduce Pathwise Random Hamiltonian Simulation (PRHS), which extends qDrift to arbitrary order by subdividing each time step into M correlated slices, each evolving under a term sampled from a quasi-probability distribution that we construct in closed form and prove unique, with a bias decaying factorially in M. Optimizing jointly over the number of slices M and the number of independent blocks N interpolates between the standard qDrift protocol at long times and a high-precision regime where the query cost grows slower than any power of 1/epsilon, without requiring ancillary qubits. Numerical simulations of five molecular Hamiltonians confirm this advantage, with PRHS achieving accuracies two to four orders of magnitude beyond qDrift at equal query cost.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.29756) | 2026-09-01
