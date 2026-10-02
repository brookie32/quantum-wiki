---
title: "Exact T-counts of Toffoli layers from an isotropy bound"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01024"
summary: "arXiv:2610.01024v1 Announce Type: new Abstract: The T-count is the dominant cost of fault-tolerant Clifford+T computation. We prove that a layer of m disjoint CCZ gates, the diagonal core of a paralle"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01024v1 Announce Type: new Abstract: The T-count is the dominant cost of fault-tolerant Clifford+T computation. We prove that a layer of m disjoint CCZ gates, the diagonal core of a parallel Toffoli layer, needs exactly 6m+1 T gates in every Hadamard-free Clifford+T circuit with clean ancillas. Campbell and Howard gave the matching construction. To our knowledge this is the first proof that it is optimal for general m (for m=1 the value 7 is classical, and Campbell and Howard state the value 13 at m=2). On every controlled unitary the same floor comes within one of their exact count, and it recovers their 4m+3 for a fan-out of m Toffolis from one control. The proof rests on an isotropy constraint: for a pure-cubic phase, the vectors recording which T gates touch each qubit span a totally isotropic subspace. In general the constraint gives the isotropy floor eltage2(n-d^{ast})-r for every diagonal level-three gate, computed from the phase polynomial in polynomial time. The floor is never below stabilizer nullity nu, which equals n-d^{ast} on this class, and a separate parity argument raises it to 2nu+1 on non-Clifford pure-cubic gates. On the output of the TODD optimizer for the 24 benchmark circuits it completes, the floor certifies 193 of its 311 merged phase-polynomial blocks optimal for their Hadamard layering (186 to 193 across five optimizer seeds), against 113 for nullity. The floor also holds, under stated conditions, for circuits whose only internal Hadamards form unitarily uncomputed temporary AND blocks, while under adaptive feedforward only tgenu is proved.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01024) | 2026-10-02
