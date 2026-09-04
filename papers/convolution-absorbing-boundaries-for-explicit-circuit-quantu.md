---
title: "Convolution absorbing boundaries for explicit-circuit quantum simulation of the wave equation"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03440"
summary: "arXiv:2609.03440v1 Announce Type: new Abstract: Explicit quantum circuits for the wave equation, built by Hamiltonian simulation, are restricted to closed domains, in which outgoing waves reflect off "
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03440v1 Announce Type: new Abstract: Explicit quantum circuits for the wave equation, built by Hamiltonian simulation, are restricted to closed domains, in which outgoing waves reflect off the edge of the computational region and return. We lift that restriction with absorbing boundaries of the convolution type - a complex-frequency-shifted perfectly matched layer realised through exponential-kernel memory variables - and make the resulting non-unitary dynamics quantum-implementable by Schrodingerisation. We obtain three results. First, explicit gate-level circuits for the absorbing evolution, obtained by extending a Bell- basis term-evolution circuit to projector-valued operator strings and Trotterising to second order; these run end to end on seventeen to twenty-one qubits and agree with exact references to within a tenth of a percent to a percent. Second, a structural obstruction: the memory form of the absorbing generator carries an irreducibly indefinite Hermitian part, whose largest eigenvalue grows as the square root of the absorption strength divided by the grid spacing and survives any diagonal rescaling of the memory fields. The known recovery threshold for Schrodingerisation then makes the post-selection cost grow exponentially in the simulated time. Third, a remedy: a Lyapunov symmetrizer, precomputed classically, renders the transformed generator dissipative and replaces that time-dependent penalty with a time-independent conditioning factor of several hundred, measured on grids of up to four thousand unknowns and saturating under mesh refinement. The crossover is early: past it the symmetrized recovery is cheaper by four to twenty-six orders of magnitude in post-selection cost, and at the longest horizons tested it is the only recovery that works.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03440) | 2026-09-04
