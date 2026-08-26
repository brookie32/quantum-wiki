---
title: "Trotterization with Many-body Coulomb Interactions: Convergence for General Initial Conditions and State-Dependent Improvements"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.07704"
summary: "arXiv:2604.07704v2 Announce Type: replace Abstract: Efficiently simulating many-body quantum systems with Coulomb interactions is a fundamental question in quantum physics, quantum chemistry, and quan"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2604.07704v2 Announce Type: replace Abstract: Efficiently simulating many-body quantum systems with Coulomb interactions is a fundamental question in quantum physics, quantum chemistry, and quantum computing, yet it presents unique challenges: the Hamiltonian is an unbounded operator; its Hilbert space dimension grows exponentially with particle number; and the Coulomb potential is singular, long-ranged, and non-smooth, violating the regularity assumptions of many prior state-of-the-art many-body simulation analyses. In this work, we establish rigorous error bounds for Trotter formulas applied to these systems. Our first main result shows that for general initial conditions in the domain of the Hamiltonian, second-order Trotter achieves a 1/4 convergence rate with explicit polynomial dependence of the error prefactor on the particle number. The polynomial dependence on system size suggests that the algorithm remains quantumly efficient, even without introducing any regularization of the Coulomb singularity. Such a worst-case rate has been observed in prior work for the hydrogen ground state, demonstrating its physical relevance. We further establish one-step local error lower bounds of order 5/4 for both formulas, showing that the local exponent is sharp. Our second main result identifies a set of physically meaningful conditions on the initial state under which the convergence rates improve, with the full first-order and second-order rates recovered at sufficiently high angular momentum. Our theoretical findings are consistent with prior numerical observations. Our third main result establishes improved convergence rates for many-body fermionic Coulomb systems with initial data of different Sobolev regularity. In particular, even without imposing any additional regularity beyond the natural domain of the Hamiltonian, both the first- and second-order Trotter formulas converge with rate 1/2, rather than the general 1/4 rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.07704) | 2026-08-26
