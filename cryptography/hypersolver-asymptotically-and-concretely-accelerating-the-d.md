---
title: "HyperSolver: Asymptotically and Concretely Accelerating the Delfs–Galbraith Attack using Isogeny Ladders"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1823"
summary: "We present a new variant of the memoryless Delfs-Galbraith algorithm for finding an isogeny path from any given supersingular elliptic curve to a curve with known endomorphism ring. Through existing p"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

We present a new variant of the memoryless Delfs-Galbraith algorithm for finding an isogeny path from any given supersingular elliptic curve to a curve with known endomorphism ring. Through existing polynomial-time reductions, our algorithm allows one to solve the supersingular endomorphism-ring problem which lies at the heart of isogeny-based cryptography. For arbitrary characteristics p our algorithm asymptotically outperforms the previous best Delfs-Galbraith variant by a logarithmic factor; and matches the best previous asymptotic for characteristics with favourable structure. In addition to the asymptotic analysis, we also calculate a concrete cost estimate for our algorithm in terms of finite-field operations, which indicates that our expected cost is lower than all previous Delfs-Galbraith variants, even concretely. By substituting bit-operation counts for the cost of arithmetic, we can deduce concrete bit-security estimates for isogeny-based cryptographic primitives, including (but not limited to) SQIsign. As part of the calculation of the expected cost, we also provide a novel analysis of the probability of encountering "distinguished" subgraphs in an expander graph when relying various modes of graph exploration, whose potentially counterintuitive behaviour had apparently remained unnoticed thus far. Finally, we provide a complete implementation of our algorithm(s), with the asymptotic bottleneck being attacked on GPUs, and the easier post-processing done on CPU using C++ as well as SageMath. Preliminary experimental results suggest that we can solve 100-bit instances of the problem within less than 100 GPU hours. For comparison, the current cryptanalytic record for ECDLP (which has a comparable classical attack complexity) stands at 114 bits, achieved using significantly more hardware and time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1823) | 2026-08-27
