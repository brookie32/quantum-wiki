---
title: "Order-Four Symmetry in BGV Bootstrapping: Faster Digit Extraction for Large Primes"
date: "2026-08-31"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1847"
summary: "Bootstrapping is the computational bottleneck of BGV/BFV fully homomorphic encryption, scaling particularly poorly with large plaintext primes. Its two dominant stages: digit extraction and linear tra"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Bootstrapping is the computational bottleneck of BGV/BFV fully homomorphic encryption, scaling particularly poorly with large plaintext primes. Its two dominant stages: digit extraction and linear transforms. Recent work has reduced the digit-extraction polynomial degree via null-polynomial lattices and bounded-support constructions, but both evaluate the reduced polynomial via generic Paterson--Stockmeyer at cost O(sqrt{d}) . We present two algebraic optimizations that address both stages simultaneously. For digit extraction, we prove that choosing the auxiliary radix A with A^2equiv -1pmod{p} induces an order-four character filter, forcing the canonical digit-extraction polynomial to satisfy P_A(AX)+AP_A(X)=AX and eliminating all monomials X^k with knotequiv 1,3pmod{4}. The resulting structured decompositionP_A(X)=frac{1}{2}X+X^3Q(X^4) reduces non-scalar multiplications from O(sqrt{d}) to O(sqrt{d/r}). For linear transforms, we provide first concrete instantiation of a Galois-structured mixed-radix butterfly decomposition for non-power-of-two cyclotomics, reducing the automorphism count from O(sqrt{D}) to O(log D). On the standard NTT-friendly large-prime set (p=65537, m=2^{16}, 32768 slots), our single-threaded Elib{} implementation achieves a 1.85imes digit-extraction speedup (20.06s to 10.81s) and a 1.27imes total thin-bootstrapping speedup (42.3s to 33.3s) over the state-of-the-art Ma et al. baseline, the three stages the method does not touch moving by at most one per cent. All comparisons are made against the Ma et al. baselines, run in the identical pipeline at the same auxiliary radix; across nineteen encrypted parameter sets with 1297le ple 65537, the digit-extraction speedup is 1.72--1.88imes on general cyclotomic rings (37637le mle 65047) and 1.84--2.13imes on the power-of-two ring m=2^{16}. Every set we recommend is quoted with concrete bit security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1847) | 2026-08-31
