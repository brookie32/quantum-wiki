---
title: "Locally Acting Grover Mixers for Constraint-Preserving QAOA"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.11530"
summary: "arXiv:2606.11530v2 Announce Type: replace Abstract: The Grover mixer quantum alternating operator ansatz (GM-QAOA) employs the Grover mixer to confine the quantum evolution to the feasible subspace de"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2606.11530v2 Announce Type: replace Abstract: The Grover mixer quantum alternating operator ansatz (GM-QAOA) employs the Grover mixer to confine the quantum evolution to the feasible subspace defined by the problem. Its mixing unitary, however, requires a global multi-controlled phase-shift gate acting on all qubits, resulting in substantial circuit overhead on near-term quantum devices. In this work, we propose locally acting Grover mixers with independent variational parameters, tailored to initial states that admit a product structure over disjoint qubit subsystems, which may be obtained by encoding only a subset of problem constraints into the initial state preparation. The proposed method preserves the search space defined by the initial state while reducing the mixing-circuit gate count and depth relative to the global Grover mixer, as the global multi-controlled phase-shift gate is replaced with local operations on disjoint subsystems. Numerical simulations on the exact-cover problem and the traveling salesman problem (TSP) demonstrate that the proposed method achieves solution probabilities comparable to those of the original GM-QAOA, while using shallower circuits with fewer gates. Comparisons with shared-angle local Grover and partitioned XY-ring mixers characterize the trade-offs between solution quality, circuit complexity, and optimization overhead. We further compare two constraint encoding strategies for the TSP, encoding only a subset of constraints versus all constraints into the initial state preparation, and show that the former combined with the proposed mixer can yield markedly more compact circuits at the point where comparable solution quality is achieved.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.11530) | 2026-11-26
