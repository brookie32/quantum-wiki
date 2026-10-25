---
title: "High-Precision Bootstrapping for GCKKS"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2600"
summary: "Generalized CKKS (GCKKS) trades slot count for reduced modulus consumption in high-precision approximate arithmetic. However, designing a GCKKS bootstrapping algorithm with reduced modulus consumption"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Generalized CKKS (GCKKS) trades slot count for reduced modulus consumption in high-precision approximate arithmetic. However, designing a GCKKS bootstrapping algorithm with reduced modulus consumption throughout its computation remains a challenging problem. We construct high-precision bootstrapping for GCKKS using low-precision overflow extraction followed by iterative precision enhancement. Our main ingredient is a ciphertext-conversion framework for changing the decryption factor and slot count without requiring the factors to be units. A slot-aware analysis bounds unused-slot magnitudes proportionally to the corresponding evaluations of the decryption factor, which is essential to ensure the unused-slot values remain well-bounded after conversion. We combine precision doubling with ciphertext splitting and develop a joint evaluation procedure that produces two error-cleaned outputs at the cost of only one evaluation of the cleaning polynomial. We also give a useful-slot-preserving conversion from CKKS to GCKKS that simultaneously resets unused slots through component-wise re-encoding. Underlying these constructions, we also improve the construction of the decryption factors by searching directly in the canonical embedding and obtain depth-free conjugation with non-unit factors. For target encoding precision p and 2N/k useful slots in a ring of dimension N, the precision-dependent stages of the bootstrapping use O(k) homomorphic operations and consume O((p/k)log k) modulus bits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2600) | 2026-10-22
