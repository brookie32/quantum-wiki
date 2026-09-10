---
title: "When Module Lattice Leaks: Horizontal Fusion Attacks on ML-DSA Implementation"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1904"
summary: "The standardization of ML-DSA has shifted the cryptographic community's focus toward its practical security. While profiled attacks against its implementations are well studied with a few traces, non-"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

The standardization of ML-DSA has shifted the cryptographic community's focus toward its practical security. While profiled attacks against its implementations are well studied with a few traces, non-profiling attacks are widely assumed to require large trace complexity. We challenge this by introducing horizontal fusion attacks, demonstrating that non-profiling, few-trace key recovery is highly practical against ML-DSA, even against masked implementations. We expose a structural vulnerability in the module lattice from a side-channel perspective. In particular, in ML-DSA's matrix-vector multiplication (hat{mathbf{A}} irc hat{mathbf{y}}), the row-wise reuse of the ephemeral secret vector hat{mathbf{y}} indicates that one single signature generation exposes k (the row-wise size of hat{mathbf{A}}) leakage instances of the same secret-dependent intermediate value, each with a distinct and known coefficient of hat{mathbf{A}}. However, exploiting this in practice is highly non-trivial due to noise and/or compiler optimizations. To overcome this, we propose a variance-based weighted fusion strategy. This approach weights each operation by how far its leading candidate is separated from the runner-up candidates, and the signing relation (mathbf{y} = mathbf{z} - c dot mathbf{s}_1) lets us extract the signed coefficients of the secret key. Moreover, we introduce a fast, INTT-based algebraic sieve that further increases the success rate of key recovery. Putting together, we achieve full key recovery using merely 4 traces against ML-DSA-87 (the highest security parameter set) with non-profiling correlation analysis. On the state-of-the-art first-order masked ML-DSA implementation, our attack extracts the secret key using no more than 90 traces. To the best of our knowledge, these non-profiling results establish a new record in trace complexity for both unprotected and first-order masked ML-DSA implementations, even comparable to these profiling-based attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1904) | 2026-09-07
