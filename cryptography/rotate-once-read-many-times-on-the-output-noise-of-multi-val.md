---
title: "Rotate Once, Read Many Times: on the Output Noise of Multi-Value Bootstrapping"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2332"
summary: "In FHEW/TFHE, a programmable bootstrap evaluates an arbitrary function of the encrypted message, encoded as the test polynomial of a blind rotation. We work in a prime-power cyclotomic ring whose prim"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

In FHEW/TFHE, a programmable bootstrap evaluates an arbitrary function of the encrypted message, encoded as the test polynomial of a blind rotation. We work in a prime-power cyclotomic ring whose prime is the plaintext modulus p (a design choice that leaves the ring degree free as a security parameter) and compare the Single-Value Mode (SVM), one rotation per function, with the Multi-Value Mode (MVM), one function-independent rotation shared by all. Factoring the test polynomial as v^*_f = mathfrak B^*_fdot mathfrak w, the function carried by the dual module and the rotated factor by the torus, lets a single hypothesis (a centered accumulator error of arbitrary covariance G) cover both modes: the two variances are values of one G-form, and their ratio is the exact amplification. The f-independent factorizations are then parametrized by a non-zero ring element, the cofactor, and by the integer lift of the table: at a random lift the cofactor is chosen by a shortest-vector problem for an explicit quadratic form, then the lift by a closest-vector problem of rank p-1. In the spherical model that form is a trace norm and two designs compete: the canonical cofactor, of noise cost p(p+1)/6, and the pivot, which reads the integer table itself at noise cost 2p, at a random lift; the optimized lift then favours the canonical cofactor on the generic tables. Under the other natural covariance, the block Laplacian, it is optimal for every p. Both cofactors are measured, in the key-noise regime, on a complete implementation, publicly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2332) | 2026-10-04
