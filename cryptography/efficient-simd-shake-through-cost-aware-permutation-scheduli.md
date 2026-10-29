---
title: "Efficient SIMD SHAKE through Cost-Aware Permutation Scheduling"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2666"
summary: "Lattice-based cryptography uses SHAKE to expand seeds into byte strings for matrix generation and sampling. SIMD Keccak implementations process multiple hash streams in parallel. Differences in stream"
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

Lattice-based cryptography uses SHAKE to expand seeds into byte strings for matrix generation and sampling. SIMD Keccak implementations process multiple hash streams in parallel. Differences in stream lengths and input dependencies can prevent full SIMD utilization. We present a cost-aware method for scheduling Keccak permutations across hash streams during a single execution of a cryptographic algorithm. The method groups ready streams and divides long streams into segments for regrouping. A model of permutation calls, state movement, initialization, and input preparation guides the selection of stream groups, segment lengths, and state placements. We evaluate ML-KEM and HAETAE on an Apple M5, a Cortex-A72, and an Intel Core i5-11500, using Keccak kernels that process two, four, or eight streams per call. ML-KEM achieves speedups of up to 1.31imes for encapsulation and 1.44imes for decapsulation, while HAETAE achieves up to 1.28imes for signing and 1.26imes for verification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2666) | 2026-10-28
