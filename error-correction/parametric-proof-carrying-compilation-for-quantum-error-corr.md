---
title: "Parametric Proof-Carrying Compilation for Quantum Error-Correction"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.12985"
summary: "arXiv:2611.12985v1 Announce Type: cross Abstract: We present PC-QEC, a proof-carrying compilation framework for quantum error correction parameterized by both code distance and syndrome-extraction sch"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.12985v1 Announce Type: cross Abstract: We present PC-QEC, a proof-carrying compilation framework for quantum error correction parameterized by both code distance and syndrome-extraction scheme. It covers all four schemes---Standard, Flag, Shor and Knill---with circuit-level distance guarantees for every legal code distance in each proved family under the declared fault and readout contracts. The circuit-level model permits single-wire Pauli faults at every operation's qubit operands, capturing data errors, readout errors and ancilla faults that propagate into multi-qubit hook errors. For each family and scheme, code-algebra proofs and fault-aware Hoare proofs compose into a finite symbolic certificate whose size is independent of code distance. We demonstrate family-wide guarantees for five code families across all four schemes. For rotated Surface code, one Standard Scheme certificate proves a distance lower bound d for every odd dge3 and checks in 214,s on average. Lean 4 mechanizes the metatheory and exact circuit-level distances for canonical Surface, hypergraph-product (HGP) and Toric code families.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.12985) | 2026-11-11
