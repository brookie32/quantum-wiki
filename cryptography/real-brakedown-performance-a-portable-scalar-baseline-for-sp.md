---
title: "Real Brakedown Performance: A Portable Scalar Baseline for Spielman-Code Polynomial Commitments"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2996"
summary: "Brakedown-style polynomial commitment schemes encode the rows of a coefficient matrix with a linear-time Spielman code and Merkle-commit the columns. New schemes are typically compared against the uno"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Brakedown-style polynomial commitment schemes encode the rows of a coefficient matrix with a linear-time Spielman code and Merkle-commit the columns. New schemes are typically compared against the unoptimized LCPC and PolyCommit libraries. Conversely, the reported speedups of the AVX-512 encoder SIMD-Spielman over LCPC combine vector arithmetic with portable algorithmic and memory optimizations. We present RBP-LCPC, an optimized implementation of LCPC in portable stable Rust that integrates column-major batched encoding, right-to-left graph evaluation, lazy modular reduction and cache-aware slicing. Its incremental structure isolates the contribution of each optimization. On both x86-64 and AArch64, its compiled hot kernels contain no vector arithmetic. With LCPC's code and prime, its encodings, Merkle roots and proofs match those of LCPC bit-for-bit. On an AMD Zen 5 server with one thread and N = 2^16 to 2^28 coefficients, RBP-LCPC encodes 8.14-9.06x faster than LCPC under its default build configuration. SIMD-Spielman, measured on the same server, remains 1.59-4.44x faster up to N = 2^26. Commit achieves a smaller speedup of 5.21-5.95x over the default LCPC configuration (4.48-5.95x across both default and tuned configurations), because column hashing then accounts for over a third of single-threaded commit time. Prove and verify are 1.83-7.61x and 2.65-5.36x faster than under the default LCPC configuration across thread counts and sizes, and single-threaded PCS setup is 1.31-1.44x faster. The accompanying artifact reproduces all baselines and measurements from fixed source revisions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2996) | 2026-11-23
