---
title: "A shorter-width post-selected circuit for a truncated-Taylor Hamiltonian-evolution segment"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.09461"
summary: "arXiv:2511.09461v2 Announce Type: replace Abstract: We present an ancilla-efficient, post-selected circuit construction for a truncated-Taylor approximation to short-time Hamiltonian evolution. The co"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2511.09461v2 Announce Type: replace Abstract: We present an ancilla-efficient, post-selected circuit construction for a truncated-Taylor approximation to short-time Hamiltonian evolution. The construction combines a binary Taylor-order register with mid-circuit measurement, reset, and reuse of the Hamiltonian-index register. Conditioned on the prescribed all-zero outcomes, the circuit implements the truncated Taylor approximation while maintaining coherence among the Taylor-order branches while permitting early termination after a failed post-selection. For Taylor cutoff K, a Hamiltonian containing L terms, and an n-qubit system, the circuit uses leftlceillog {(K+1)}rightrceil +leftlceillog Lrightrceil+n qubits, and executes O(K) controlled Hamiltonian blocks in a complete segment. We analyze its post-selection probability and expected per-segment cost, and implement and evaluate the construction in Guppy[1,2]. The present work focuses on the low-width implementation of individual short-time propagation segments; coherent composition into a deterministic long-time simulation requires an additional amplification or compression mechanism and is left for future work.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.09461) | 2026-11-19
