---
title: "What Output-Equivalence Oracles Miss: An Empirical Study of Equivalence-Invisible Bug Fixes in Quantum Transpilers (Qiskit, tket, Cirq)"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13839"
summary: "arXiv:2609.13839v1 Announce Type: new Abstract: Quantum compilers are judged correct by an output-equivalence oracle: the compiled circuit must compute the same unitary as the original, modulo global "
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13839v1 Announce Type: new Abstract: Quantum compilers are judged correct by an output-equivalence oracle: the compiled circuit must compute the same unitary as the original, modulo global phase and a qubit-layout permutation. This oracle, by construction, checks only that semantic map, not the circuit's own layout, permutation, or phase records: a defect there, or in a fixed-seed run's determinism, can pass unseen though the record is public. We measure how often this happens in real merged compiler fixes: a systematically identified corpus of Qiskit transpiler bug-fixes, classified by an independently dual-coded, source-validated manifestation taxonomy. Nineteen of 68 fixes (28%, 95% Wilson CI 19-40%) repair faults that this equivalence screen does not catch, even one augmented with compilation-validity, circuit-quality, and performance checks. A secondary wider-window robustness sample produced a nearly identical fraction (29/104, 27.9%, CI 20-37%). A conservative floor remains even restricted to the one unconditionally equivalence-invisible channel (a corrupted layout or permutation record): 10 of 68 fixes (15%, CI 8-25%) beneath the 28% headline. The gap is not Qiskit-specific: it replicates in tket (7 of 21, 33%), with Cirq smaller but consistent. We detected no systematic differences on five inexpensive PR-level characteristics (19 vs 49, underpowered to rule out a modest true difference). This class dominates the invisible set, concentrating at representation-boundary crossings. We release the corpus, codebook, and coding artifacts. Here we only measure it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13839) | 2026-09-15
