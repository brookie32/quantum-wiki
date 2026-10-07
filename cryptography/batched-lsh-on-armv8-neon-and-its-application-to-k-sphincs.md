---
title: "Batched LSH on ARMv8 NEON and Its Application to K-SPHINCS+"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2351"
summary: "With FIPS 205 standardizing post-quantum signatures and ARMv8 spanning mobile, embedded, and server platforms, fast hash-based signing on ARM has become a pressing need. Since these schemes are domina"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

With FIPS 205 standardizing post-quantum signatures and ARMv8 spanning mobile, embedded, and server platforms, fast hash-based signing on ARM has become a pressing need. Since these schemes are dominated by hash calls, hash optimization largely determines performance. K-SPHINCS+ replaces the internal hash of stateless SPHINCS+ with LSH, a Korean standard hash family. However, prior K-SPHINCS+ work provides only reference C code, and existing ARMv8 LSH implementations mainly optimize single-call latency. We present two results on ARMv8-A. First, we reimplement three published LSH optimizations in hand-written AArch64 NEON assembly: the 2019 word-permutation technique; the 2023 ARMv8 P-domain placement and LSH-256 2-way approach; and the 2024 AVX-512 word-parallel and GPU lane-batching designs. We also test whether NEON scheduling guidance from a 2022 AArch64 Keccak/SPHINCS+ paper transfers to LSH. Every variant must pass 2,063 public known-answer test vectors and a differential test suite before benchmarking. No single-message NEON implementation beats the KISA portable C code compiled with clang -O3 (0.75–0.90×). Only message-parallel batching wins: for LSH-256, hashing two or four independent messages across NEON lanes reaches 1.53–1.66× and about 2.0× the throughput of sequential C. Second, we build, to our knowledge, the first optimized K-SPHINCS+ by integrating a four-message LSH batch core into the WOTS+ chain, FORS leaf, and Merkle tree computations of the SPHINCS+ reference framework. All six parameter sets pass the framework’s tests, and all three hash backends (reference C, single-message NEON, four-message NEON) produce byte-identical signatures. On the same machine, batched K-SPHINCS+ signs 2.5–2.6× faster than K-SPHINCS+ with reference C LSH and, for the 128-bit parameter sets, 2.9–3.2× faster than the SHA-256/SHAKE256 SPHINCS+ reference implementations. All code and raw measurements are public.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2351) | 2026-10-05
