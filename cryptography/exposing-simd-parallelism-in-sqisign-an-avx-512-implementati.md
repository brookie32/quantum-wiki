---
title: "Exposing SIMD Parallelism in SQIsign: An AVX-512 Implementation"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1713"
summary: "Modern isogeny-based cryptosystems spend much of their running time in finite-field, elliptic-curve, and higher-dimensional isogeny arithmetic. Exploiting SIMD parallelism in these computations is nev"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

Modern isogeny-based cryptosystems spend much of their running time in finite-field, elliptic-curve, and higher-dimensional isogeny arithmetic. Exploiting SIMD parallelism in these computations is nevertheless nontrivial: central routines such as Montgomery ladders contain loop-carried dependencies, while point, pairing, and theta-coordinate formulas expose only irregular fine-grained parallelism. We show that substantial SIMD parallelism can be recovered by reorganizing the arithmetic dependency graphs of these higher-level primitives rather than vectorizing field multiplication in isolation. We develop an end-to-end AVX-512IFMA implementation of SQIsign in which data remain in a radix-2^{51} vector representation across most of the curve-side computation. Our redesign includes projective xDBLADD schedules for Montgomery ladders, batched point doubling in several coordinate systems, a vectorized biscalar ladder, fused cubical-arithmetic pairing steps, and batched one- and two-dimensional isogeny evaluation. Relative to the reference C implementation, our implementation achieves end-to-end speedups of 1.76imes, 1.71imes, and 3.18imes for key generation, signing, and verification, respectively, at NIST security level~I; combining the same implementation with Qlapoti increases the key-generation and signing speedups to 2.90imes and 2.69imes. To test whether these techniques are specific to SQIsign, we further apply the same AVX-512IFMA backend and higher-dimensional vectorization methodology to CORAL, a recent isogeny group action for post-quantum non-interactive key exchange based on two-dimensional 2-isogenies. Across the five parameter sets in our experiments, this yields 1.28--1.40imes speedups for key generation and 1.92--2.46imes speedups for shared-key computation over the reference C implementation. These results provide cross-scheme evidence that algorithm-level SIMD scheduling is a reusable optimization dimension for higher-dimensional isogeny cryptography.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1713) | 2026-08-17
