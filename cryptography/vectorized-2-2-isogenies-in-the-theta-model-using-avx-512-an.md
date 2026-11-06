---
title: "Vectorized (2, 2)-Isogenies in the Theta Model Using AVX-512 and Applications to SQIsign"
date: "2026-11-04"
updated: "2026-11-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2773"
summary: "Higher-dimensional isogenies have emerged as a powerful building block for isogeny-based cryptography, with recent protocols such as SQIsign relying on the efficient evaluation of (2^n, 2^n)-isogenies"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

Higher-dimensional isogenies have emerged as a powerful building block for isogeny-based cryptography, with recent protocols such as SQIsign relying on the efficient evaluation of (2^n, 2^n)-isogenies. Despite their attractive security and compactness properties, these schemes remain computationally expensive and improving their performance is an important step for their real-world use. In this work, we present a high-performance AVX-512 implementation of two-dimensional isogenies that effectively exploits their data-level parallelism. We develop a code generator that produces efficient AVX-512 implementations of arithmetic over F_p and F_{p^2} for Montgomery-friendly primes of the form p=cdot 2^e-1 with eapprox log_2(p), covering the family of primes used by several protocols based on two-dimensional isogenies, including SQIsign. Building on this arithmetic, we vectorize the (2^n, 2^n)-isogeny formulas by Dartois et al. (ASIACRYPT 2024), achieving significant speedups over the corresponding, highly-optimized scalar implementation that uses x86-64 assembly. As an application, we accelerate the Round 2 version of SQIsign verification and obtain speedups of 2.5imes at NIST security level I and 3.2imes and 3.3imes at levels III and V, respectively. Our code generator also readily supports the larger primes of Round 3 SQIsign, for which we obtain verification speedups between 3.1imes and 3.4imes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2773) | 2026-11-04
