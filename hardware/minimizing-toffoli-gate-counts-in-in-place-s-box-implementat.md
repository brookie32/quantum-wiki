---
title: "Minimizing Toffoli Gate Counts in In-Place S-Box Implementations"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3026"
summary: "In this paper, we study ancilla-free in-place quantum implementations of the Ascon S-box and the 5-bit Keccak hi_5 mapping. We develop a complete synthesis method that treats NOT and CNOT gates as aff"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

In this paper, we study ancilla-free in-place quantum implementations of the Ascon S-box and the 5-bit Keccak hi_5 mapping. We develop a complete synthesis method that treats NOT and CNOT gates as affine operations and uses canonical state representation together with a proven lower bound to prune the search space. Using this method, we settle the previously unresolved minimum Toffoli count for the Ascon S-box at exactly seven, extend the same minimum to Keccak hi_5 via affine equivalence, and establish a minimum Toffoli depth of seven for both functions. We further optimize Clifford+T realizations of these minimum-Toffoli circuits by resynthesizing the decomposed circuits across Toffoli-decomposition boundaries. For both targets, the resulting implementations achieve either 33 T gates with T-depth 8 or 29 T gates with T-depth 10. To the best of our knowledge, these achieve the lowest reported T-depth and T-count, respectively, among existing 5-qubit ancilla-free in-place implementations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3026) | 2026-11-24
