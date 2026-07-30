---
title: "Falcon Verify on AVX-512: Speed Records"
date: "2026-07-27"
updated: "2026-07-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1539"
summary: "We present a fast implementation of Falcon (FN-DSA) signature verification with AVX-512. On a modern AMD Zen5 core, it completes a Falcon-512 verification in 3.6 microseconds, 2.6 times faster than an"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

We present a fast implementation of Falcon (FN-DSA) signature verification with AVX-512. On a modern AMD Zen5 core, it completes a Falcon-512 verification in 3.6 microseconds, 2.6 times faster than an already optimized baseline, with comparable gains on Zen4, and consistent results across clang 21 and gcc 15. The speedup comes from rewriting the Number-Theoretic Transform (NTT) and from vectorising all other stages of the verification algorithm. The novelty is to use a 32-bit Barrett-style representation, instead of the reference 16-bit Montgomery, and adopt Shoup-Harvey precomputed multipliers for twiddle reduction. With all optimizations applied, hash-to-point (and specifically Keccak) is the dominant cost. We therefore propose a non-standard Falcon variant that replaces SHAKE256 with KTP256, an XOF based on KangarooTwelve with parallel squeeze. It cuts verification to 2.2 microseconds on Zen5, yielding 4.2 times over the baseline, and is of independent interest for any post-quantum scheme that uses a Keccak sponge to sample large amounts of data from a fixed seed. All code is open source.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1539) | 2026-07-27
