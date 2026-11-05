---
title: "Efficient Classical Simulation of Low-Rank-Width Quantum Circuits Using ZX-Calculus"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.06764"
summary: "arXiv:2603.06764v2 Announce Type: replace Abstract: In this paper, we introduce an algorithm for contracting (i.e. numerically evaluating) ZX-diagrams whose computational complexity is governed by ran"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2603.06764v2 Announce Type: replace Abstract: In this paper, we introduce an algorithm for contracting (i.e. numerically evaluating) ZX-diagrams whose computational complexity is governed by rank-width, a structural graph parameter that behaves nicely under ZX rewrite rules. Our method evaluates a graph-like ZX-diagram in ~O(4^R) time, given its rank-decomposition of width R. By constructing suitable rank-decompositions, we provide a classical simulation algorithm for quantum circuits whose runtime is bounded by both ~O(2^n) and ~O(2^(t/2)), where n is the number of qubits and t is the number of non-Clifford phase gates. Thus, our method is no slower than either the naive state-vector simulation or the elementary stabiliser decomposition baseline, and in practice can be even faster when the reduced ZX-diagram has low rank-width. We benchmark our simulation algorithm against Quimb, a popular tensor contraction library, and observe substantial reductions in floating-point operations, often by several orders of magnitude, for random and structured non-Clifford circuits and for random ZX-diagrams.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.06764) | 2026-11-05
