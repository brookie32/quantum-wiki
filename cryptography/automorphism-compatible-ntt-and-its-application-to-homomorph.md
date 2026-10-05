---
title: "Automorphism-Compatible NTT and its Application to Homomorphic Encryption"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2328"
summary: "For N a power of 2, the negacyclic number-theoretic transform (NTT) maps a degree N-1 polynomial to its evaluations at the N primitive 2Nth roots of unity. In-place butterfly algorithms such as Cooley"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

For N a power of 2, the negacyclic number-theoretic transform (NTT) maps a degree N-1 polynomial to its evaluations at the N primitive 2Nth roots of unity. In-place butterfly algorithms such as Cooley-Tukey and Gentleman-Sande compute the negacyclic NTT in O(Nlog N) time and output the evaluations in a specific, standard order. We give in-place butterfly algorithms for the negacyclic NTT and its inverse that instead output the evaluations in an automorphism-compatible order. These algorithms have the same structure as Cooley-Tukey and Gentleman-Sande, differing only in their precomputed twiddle factors. Our automorphism-compatible butterfly algorithms are applicable to the packed fully homomorphic encryption (FHE) schemes CKKS and BGV/BFV, where the negacyclic NTT is a major component of ciphertext arithmetic. Using our automorphism-compatible butterfly algorithms, Galois automorphisms can be applied to ciphertexts stored in double-CRT format via a simple cyclic shift or adjacent-pair swap of the data. This is contrast to butterfly algorithms currently used that output in the standard order, where applying an automorphism requires performing an arbitrary-looking permutation of the stored data. Our automorphism-compatible butterfly algorithms remove the need for a dedicated automorphism functional unit used in FHE hardware accelerators.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2328) | 2026-10-04
