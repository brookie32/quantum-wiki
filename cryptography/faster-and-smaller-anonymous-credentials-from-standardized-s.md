---
title: "Faster and Smaller Anonymous Credentials from Standardized Signatures"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2615"
summary: "We present GordieHowe, a system comprising a language, a certifying compiler, and a zero-knowledge proof protocol. GordieHowe is especially suitable for building anonymous credentials on top of standa"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

We present GordieHowe, a system comprising a language, a certifying compiler, and a zero-knowledge proof protocol. GordieHowe is especially suitable for building anonymous credentials on top of standardized signature schemes like ECDSA, RSA, and ML-DSA. GordieHowe is the first system to achieve the following three properties simultaneously: provable security against quantum attackers, efficiency for statements spanning multiple fields—including proving and verifying in parallel—and automatic batching of structured computations. GordieHowe is high-assurance by design. The language is designed to enable static checking of bounds safety, preventing integer overflows. Its compiler emits a Lean certificate that its optimization decisions are semantics-preserving for the input program. The proof system's security theorems are machine-checked in Lean. GordieHowe is faster and has smaller proofs than comparable prior work. It proves, in parallel on four cores, an ECDSA-signed mobile driving license presentation in 64.8 ms with a 276 KiB proof, 10.1× faster and 22% smaller than Google's Longfellow. With at least 101 bits of knowledge soundness in the random oracle model, GordieHowe proves knowledge of a 1 KiB SHA3-256 preimage in 5.0 ms with a 60 KiB proof, and of an RSA-2048 signature on a private 2 KiB message in 25.9 ms with a 210 KiB proof. With at least 116 bits against quantum adversaries, GordieHowe proves knowledge of an ML-DSA-44 signature on a private message in 87.3 ms with a 549 KiB proof, 70.2× faster and 29% smaller than an optimized Longfellow circuit. In building GordieHowe we make a number of contributions of independent interest. We define a new notion of an interactive oracle proof (IOP) whose messages are partially ordered, which we call a series-parallel IOP. We extend the BCS transformation to series-parallel IOPs, and give knowledge soundness and ZK proofs in the QROM. We also show our BCS extension satisfies a form of simulation extractability in the QROM; we believe this is the first simulation extractability result of any kind for BCS in the QROM.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2615) | 2026-10-23
