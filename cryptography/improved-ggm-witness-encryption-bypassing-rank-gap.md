---
title: "Improved GGM Witness-Encryption Bypassing Rank Gap"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2995"
summary: "Hair and Sahai construct witness encryption in the classical prime-order generic-group model using a designed matrix space with a growing rank gap. We retain their encryption mechanism while replacing"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Hair and Sahai construct witness encryption in the classical prime-order generic-group model using a designed matrix space with a growing rank gap. We retain their encryption mechanism while replacing the minimum-rank requirement with a lower bound on the min-entropy of Mr for nonzero matrices M that do not permit witness extraction, where r is the short random vector used in encryption. A matrix with substantial concentration has a column factorization from a finite family of short rational patterns. One list of linear forms evaluated at powers of a public random seed preserves all these patterns simultaneously, except with exponentially small probability, and therefore suffices in place of their multiple folded lists. For a quadratic verifier encoding with N Boolean variables, using t=lceillog Nrceil forms gives one-bit ciphertexts of widetilde O(N^5) bits and optimized decryption using widetilde O(N^4) group queries. For sufficiently large N, distinguishing advantage on false instances is at most N^{-log N} against classical generic adversaries making at most N^{log N} group queries. Correctness error is 2^{-Omega(N)}, simultaneously for all valid witnesses of a ciphertext. At these same security and correctness guarantees, a beneficial reparameterization of Hair--Sahai's deterministic construction gives ciphertexts of widetilde O(N^6) bits and, with the same decryption optimizations, widetilde O(N^5) group queries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2995) | 2026-11-23
