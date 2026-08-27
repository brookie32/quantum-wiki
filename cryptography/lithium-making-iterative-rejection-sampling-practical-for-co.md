---
title: "Lithium: Making Iterative Rejection Sampling Practical for Compact Lattice Signatures"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1790"
summary: "Post-quantum deployments need signatures that are both fast and small. ML-DSA gives a practical Fiat-Shamir lattice-signature baseline, but its signatures remain large enough to make bandwidth, certif"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

Post-quantum deployments need signatures that are both fast and small. ML-DSA gives a practical Fiat-Shamir lattice-signature baseline, but its signatures remain large enough to make bandwidth, certificate size, and signed-log storage first-order costs. Gaertner's iterative rejection sampling construction (CRYPTO'25) shows that this design family can be made much more compact. The open question is whether this theoretical design can be turned into a concrete, implementation-oriented signature scheme, where the parameters, algorithms, encodings, and optimized software work together without giving up the promised compactness. We present Lithium, a compact Fiat-Shamir lattice signature that makes iterative rejection sampling practical. Lithium co-designs its parameters, discrete Gaussian sampler, ApproxExp evaluation, iterative rejection sampling, and rANS encoder so that compact signatures do not come at the cost of an impractical signer. For the core components, we introduce algorithmic and vectorized optimizations and provide a portable reference implementation together with vectorized AVX2 and AVX-512 implementations. Lithium-120 targets a security level close to ML-DSA-44. Our experiments show that our fastest implementation signs faster than ML-DSA-44, at 166k versus 191k cycles, while producing signatures about half as large: 1,187 bytes versus 2,420 bytes. Compared with HAETAE-120, Lithium-120 is more compact and signs about 7.5x faster.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1790) | 2026-08-24
