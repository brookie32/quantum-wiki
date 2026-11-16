---
title: "Efficient Iterative Symmetrization algorithm for quantum computing and hadron applications"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18091"
summary: "arXiv:2611.18091v1 Announce Type: new Abstract: Efficient algorithms for the (anti)symmetrization of quantum registers are necessary for upcoming few- and many-body physics applications, from atomic t"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18091v1 Announce Type: new Abstract: Efficient algorithms for the (anti)symmetrization of quantum registers are necessary for upcoming few- and many-body physics applications, from atomic to particle-physics scales. We propose a recursive algorithm (anti)symmetrizing the last particle added to memory, each time one is created or destroyed, respect to the rest of already (anti)symmetrized ones. Given a generalized Dicke state (GDS) of (j-1) quantum registers, each assigned to a particle, the algorithm produces another GDS of j registers (of n_{qb} qubits each) using a mere O(jlog_2^2 j + j n_{qb}) mathtt{CNOT} and single-qubit gates, and 3j+lceillog_2jrceil+O(max(n_{qb},log_2 j)) clean auxiliary qubits. The (anti)symmetrizing operator constructed for this purpose depends on the quantum numbers of the additional particle being introduced or ``created''. The algorithm improves upon the construction presented in Appendix A of ite{Galvez-Viruet:2024hry} by almost two powers of j and is on par with the most efficient methods to date, while ideally suited for dynamical memory management with variable particle number. We exemplify its applicability with a small selection of problems from hadron physics which are expected to be addressable with upcoming quantum computers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18091) | 2026-11-16
