---
title: "Shared Lookups and Lazy Residues: Fewer Toffoli Gates for Factoring RSA-2048"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08907"
summary: "arXiv:2611.08907v1 Announce Type: new Abstract: Gidney's 2025 construction for factoring RSA-2048 with few logical qubits spends most of its Toffoli gates on discrete-log table lookups and residue unc"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08907v1 Announce Type: new Abstract: Gidney's 2025 construction for factoring RSA-2048 with few logical qubits spends most of its Toffoli gates on discrete-log table lookups and residue uncomputation. We reduce both costs. Shared lookups return entries for several primes of a residue number system at once because they have the same address. Retained intermediate residues remove recomputation during cleanup and enable lazy arithmetic with a single final modular reduction. We prove output preservation and estimate resources with an open benchmark built on the reference simulator. Against the best reference setting within the same logical-qubit budget, using the published model for the reference and benchmark counts for our circuits, we obtain 15% fewer Toffolis at 1{,}461 qubits (5.08 imes 10^{9} per factoring) and 46% fewer at 1{,}806 qubits (2.55 imes 10^{9}). A matched ablation finds 28.8% fewer Toffolis from three-prime sharing at fixed window and checkpoint settings. Architecture-specific timing determines how much becomes a runtime saving.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08907) | 2026-11-09
