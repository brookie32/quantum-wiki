---
title: "AVX-512 Acceleration of SQIsign 3.0 Verification"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2505"
summary: "SQIsign is a compact isogeny-based signature scheme. We present a low-latency AVX-512 implementation of complete SQIsign 3.0 verification at security levels I, III, and V. Our implementation provides "
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

SQIsign is a compact isogeny-based signature scheme. We present a low-latency AVX-512 implementation of complete SQIsign 3.0 verification at security levels I, III, and V. Our implementation provides vectorized curve-side verification, including the Superglue transition, and introduces dynamic-programming strategies for the degree-2^ell and theta-model (2,2)-isogeny chains. The strategies account for batched point evaluation and the preparation of SIMD data. On an Intel Core i7-11800H running native Ubuntu 24.04, the complete verifiers achieve 2.14imes, 2.08imes, and 2.34imes speedups, respectively, over the SQIsign 3.0 Broadwell reference verifiers (the optimized 64-bit assembly implementation).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2505) | 2026-10-16
