---
title: "A Polynomial-Time Attack on the McEliece Cryptosystem on Elliptic Codes with Arbitrary Divisors"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2050"
summary: "The McEliece cryptosystem based on algebraic geometry codes has been proposed as a way to reduce the key size of code-based cryptography, but several structural attacks have demonstrated the vulnerabi"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The McEliece cryptosystem based on algebraic geometry codes has been proposed as a way to reduce the key size of code-based cryptography, but several structural attacks have demonstrated the vulnerability of particular families of algebraic geometry codes. Despite this, until recently, there remained schemes and parameter sets that were not vulnerable to any known attack. We propose a new structural attack with ``hints'' that applies to elliptic codes with arbitrary effective divisors. In particular, we prove that, given the elliptic curve, the public generator matrix, and three points from the evaluation divisor, the entire divisor can be recovered in polynomial time, independently of the number of errors used in the cryptosystem. The attack requires O(k^2n^2+|E(F_q)|+n) operations in F_q and succeeds with overwhelming probability, after which the second divisor is recovered in O!left(k^2n^2 + (|E(F_q)|-n)n^2right) operations. We further propose an optimized version of the attack that requires no additional information at all. Exploiting the action of the automorphisms of the curve, the three known points are replaced by the enumeration of a single pair of field elements, which yields an equivalent key on the given public curve in O!left(k^2n^2 + q^2 + (|E(F_q)|-n)n^2right) operations on average.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2050) | 2026-09-15
