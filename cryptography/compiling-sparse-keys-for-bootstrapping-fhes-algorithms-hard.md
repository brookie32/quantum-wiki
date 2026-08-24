---
title: "Compiling Sparse Keys for Bootstrapping FHEs: Algorithms, Hardware Acceleration, and Beyond"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1783"
summary: "Blind rotation is the dominant computational bottleneck in bootstrapping for bitwise FHE schemes such as TFHE. Existing constructions typically evaluate O(n) sequential external products for an LWE se"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Blind rotation is the dominant computational bottleneck in bootstrapping for bitwise FHE schemes such as TFHE. Existing constructions typically evaluate O(n) sequential external products for an LWE secret of dimension n, incurring substantial latency and a large number of NTT/iNTT operations. In this work, we present a new framework for NTRU-based bootstrapping that reduces the sequential complexity of blind rotation for sparse binary LWE secrets. Inspired by Jain et al. (CRYPTO 2026), we use Cuckoo hashing to transform an n-dimensional binary LWE secret of Hamming weight h into extended buckets of one-hot representation. This structured representation reduces the sequential external products from O(n) to O(h) in blind rotation. We also design a modulus-switching method tailored to sparse secrets. We further explore an NTT-free variant that eliminates all online NTT/iNTT operations during blind rotation while supporting gate bootstrapping with lower parallel depth, offering a potentially useful building block for hardware-friendly FHE implementations. Empirically, we achieve state-of-the-art bootstrapping performance on both CPUs and GPUs. At comparable decryption failure rates and on a single CPU thread with AVX-512, our implementation executes Boolean gate, 4-bit, and 6-bit bootstrapping in 0.83, 1.75, and 2.65,ms, outperforming TFHE-rs by 3.31imes, 4.18imes, and 20.47imes, respectively. On an RTX~4090 GPU, we attain a throughput of 154{,}739 gate bootstraps per second, corresponding to an amortized time of 6.46,mus, and speedups of 86.7imes over our CPU result and 13.6imes over VeloFHE (Shen et al., TCHES 2025). As a concrete application, we develop the first NTRU-based 8-bit FHE instruction set, achieving up to over 10imes speedup over Trama et al. (TCHES 2025) with over 100imes smaller key size.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1783) | 2026-08-23
