---
title: "When Elliptic-Curve Semiprimality Certificates Reveal Factors"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2620"
summary: "Public certificates of semiprimality could support cryptographic modulus generation by proving that an integer has exactly two prime factors without revealing them. Their usefulness in this setting de"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Public certificates of semiprimality could support cryptographic modulus generation by proving that an integer has exactly two prime factors without revealing them. Their usefulness in this setting depends on whether the certificate preserves the difficulty of factoring. Motivated by the examples of Reble and Broadhurst, we formalize semiprimality certificates by adapting the Goldwasser-Kilian primality criterion. For certificates with a prime point order, our semiprimality theorem uses public data (N,S,E,P) comprising a composite nonsquare integer N, an elliptic curve E over Z/NZ, a certified prime S>(N^{1/6}+1)^2, and a point Pin E(Z/NZ) of order S modulo every prime divisor of N. Hasse's bound forces each prime divisor above N^{1/3}, proving that N has exactly two prime factors. For such semiprimality certificates constructed using complex multiplication (CM), we show that a norm-lattice reconstruction factors N from (N,S,D) alone in expected polynomial time when the Frobenius at every prime divisor lies in a known imaginary quadratic field of fundamental discriminant D or has trace zero, and gcd(S,2DN)=1. Applying this reconstruction and complementary public-point and quadratic-twist attacks, we factor Reble's 1084-digit and Broadhurst's 5061-digit moduli. These attacks also defeat proposed repairs based on hidden cofactors, withheld CM maps, or private isogeny descent within a known field under the stated hypotheses. We leave open whether one can efficiently produce a public Goldwasser-Kilian-based certificate for a fixed modulus, using its privately known factors, while preserving its factoring difficulty relative to the General Number Field Sieve.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2620) | 2026-10-24
