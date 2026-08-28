---
title: "Graph-Structured Number-Conserving Variational Quantum Eigensolver for Fermionic Pairing Hamiltonians"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.00844"
summary: "arXiv:2604.00844v2 Announce Type: replace Abstract: Simulating strongly correlated fermionic pairing in the presence of rotational and pair-breaking fields requires deep quantum circuits. We present a"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2604.00844v2 Announce Type: replace Abstract: Simulating strongly correlated fermionic pairing in the presence of rotational and pair-breaking fields requires deep quantum circuits. We present a graph-structured variational quantum eigensolver whose pair-transfer and single-excitation rotations follow the nonzero pairing and one-body mixing edges of the Hamiltonian. The circuit conserves particle number exactly and uses one parameter per retained edge. We benchmark one layer against exact fixed-number diagonalization for 1500, M=8 Hamiltonians represented by 16 qubits. Its mean energy error rises from 0.86 keV without one-body driving to 691 keV at the strongest drive; the one-layer circuit loses accuracy as pair breaking strengthens. In a matched eight-qubit comparison, the graph circuit reaches the 0.42 keV high-drive error of a pair-plus-all-singles circuit with 8 instead of 34 parameters. Fixed-number Adaptive Derivative-Assembled Pseudo-Trotter VQE reaches 0.056 keV with 304 decomposed controlled-NOT gates and iterative pool screening, while a 52-parameter, single-repetition unitary coupled-cluster singles-and-doubles circuit gives 17.6 keV with 2752 such gates. At a separate twelve-qubit point, a second graph layer reduces the high-drive error from 378 to 35 keV. Across the exact grid, an off-diagonal pair-coherence scale tracks the leading pair-density eigenvalue, condensate fraction, and interaction energy. Cranked zirconium Hamiltonians provide the benchmark instances and tune the strength of one-body pair breaking.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.00844) | 2026-08-28
