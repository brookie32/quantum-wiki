---
title: "Efficient Block Encoding of Structured Hamiltonians by Separating Where and What"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03686"
summary: "arXiv:2610.03686v1 Announce Type: new Abstract: Fault-tolerant block encodings of structured Hamiltonians can reduce their non-Clifford cost in SELECT by selecting where an operator acts separately fr"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03686v1 Announce Type: new Abstract: Fault-tolerant block encodings of structured Hamiltonians can reduce their non-Clifford cost in SELECT by selecting where an operator acts separately from what is applied. We construct permute-act-unpermute circuits whose CSWAP networks exploit the support geometry: a selected support is brought to a fixed target register, a shared local circuit acts there, and the permutation is undone. For supports of fixed size, the T count of SELECT then grows with the system size rather than with the number of terms, without requiring translational symmetry or factorised coefficients. For two-site supports, we establish and attain the minimum CSWAP count within address-controlled networks of site transpositions. Compiled for Pauli terms, these circuits use 8SN+O(log N) T gates with O(log N) permutation work qubits, where N is the number of system qubits and S is determined by the support geometry, with S=1 for nearest-neighbour interactions and S=3/2 for all-to-all pairs. We also introduce a bridged CSWAP that retains and repairs a temporary AND across the target action. When the repair is Clifford, it halves the T count of a matched forward-inverse CSWAP pair at the cost of one retained work qubit. For a Heisenberg ring, the complete block-encoding query reduces the T count by a factor approaching 3 as the system size grows. For a five-orbital Anderson impurity model, which combines nearest-neighbour and all-to-all support geometries, the reduction is about 1.7 at large bath sizes. Both comparisons use the lowest-cost compiled baselines considered, at unchanged block-encoding normalisation and comparable peak ancilla counts.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03686) | 2026-10-05
