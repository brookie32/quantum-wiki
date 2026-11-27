---
title: "Lightning-fast Two-Party Secure Sampling Protocol for Arbitrary Public Discrete Distributions"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3075"
summary: "Secure sampling enables randomized mechanisms to be executed within secure computation without revealing the generated randomness. Existing approaches, however, are often specialized to particular dis"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Secure sampling enables randomized mechanisms to be executed within secure computation without revealing the generated randomness. Existing approaches, however, are often specialized to particular distributions or incur substantial costs when supporting general discrete distributions. We present a two-party protocol for securely sampling from arbitrary public discrete distributions. Our approach compiles a target distribution into a representation based on table-representable mixtures and deterministic transformations. The protocol then generates arithmetic shares of a sample from the represented approximation; all approximation error arises during representation construction. We prove security against a static semi-honest adversary who corrupts one party. We evaluate our approach on five families of discrete distributions used in randomized algorithms and differential privacy (DP). For most evaluated distributions, our method achieves high approximation accuracy with low sampling cost. For the three general-purpose distributions, the total variation distance (TVD) between each target distribution and its represented approximation is at most 2^{-60}, and the per-sample runtime is below 0.16 ms in the localhost setting. For discrete Laplace noise yielding (1.0,10^{-10})-DP at sensitivity Delta=1, our protocol takes 0.0616 ms per sample in the LAN setting and requires 2.690 KiB of communication, making it approximately 706imes faster than the fastest baseline and reducing communication by a factor of approximately 128 compared with the baseline with the lowest communication.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3075) | 2026-11-27
