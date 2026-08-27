---
title: "Polylogarithmic-Weight Dicke States in QAC^0 and Arbitrary Symmetric States in QAC^0_f"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.15298"
summary: "arXiv:2604.15298v3 Announce Type: replace Abstract: An n-qubit Dicke state of weight k, is the uniform superposition over all n-bit strings of Hamming weight k. Dicke states are central to quantum alg"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2604.15298v3 Announce Type: replace Abstract: An n-qubit Dicke state of weight k, is the uniform superposition over all n-bit strings of Hamming weight k. Dicke states are central to quantum algorithms exhibiting speedups, such as Decoded Quantum Interferometry (Jordan et al., Nature, 2025). In the NISQ era, quantum hardware is constrained by both depth and locality, motivating the question of which global operations suffice to prepare such states. QAC^0, the quantum analogue of AC^0, minimally extends local O(1)-depth quantum circuits by allowing arbitrary-width Toffoli (reversible AND) gates. We show that Dicke states of polylog(n) weight can be prepared in QAC^0. This gives the first QAC^0 construction of any super-constant-weight n-qubit Dicke state, since previous constructions relied on the much more powerful FANOUT_n gate. In general, we show that any weight-k Dicke state can be constructed using FANOUT_{min(k,n-k)} gates. Combined with recent hardness results, this yields a tight characterization: for k leq n/2, a n-qubit weight-k Dicke state can be prepared in QAC^0 if and only if FANOUT_k in QAC^0. We develop a limited-fanout state-synthesis toolkit for QAC^0 that yields further constant-depth, poly(n)-ancilla constructions: 1. Every n-qubit symmetric state supported on Hamming weight leq k can be prepared using FANOUT_k gates. 2. Every O(log n)-qubit state can be prepared using quantum random-access memory (QRAM_n), which refers to a coherent indexing gate. QRAM_n is a potentially weaker resource than FANOUT_n and can be implemented in QAC^0_f.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.15298) | 2026-08-27
