---
title: "Heterogeneous CPU–NPU Implementation of the AIMer Post-Quantum Signature for Low Latency on a Mobile SoC"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2486"
summary: "Signatures in the MPC-in-the-head paradigm rest only on a symmetric primitive, but their signing is slow, because it computes hash functions and a linear map for every simulated party of every repetit"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Signatures in the MPC-in-the-head paradigm rest only on a symmetric primitive, but their signing is slow, because it computes hash functions and a linear map for every simulated party of every repetition. We show that the Hexagon NPU of Snapdragon SoCs shortens one complete signing operation of AIMer, the MPC-in- the-head signature that the Korean post-quantum cryptography competition selected. Prior work speeds up such signatures on one CPU core, accelerates post-quantum arithmetic on GPUs for batches of operations, and reports only single post-quantum functions for mobile NPUs. Our implementation divides each signing operation along its dependency graph. The NPU computes the hashing and the per-party linear map of the last repetitions, which need no secret key, and the CPU keeps the secret key and the two hashes that absorb the repetitions in index order. A fast AArch64 implementation serves both as the CPU part and as the baseline, and it signs 4.5 to 6.1 times faster than the reference implementation on one core. On a Snapdragon 8 Gen 3 tablet, one core with the NPU signs 1.30 to 1.42 times faster than two cores and 1.74 to 1.97 times faster than one core for the three short-signature parameter sets. The same configuration uses 13 to 27 % less energy per signing operation than two cores. On Snapdragon 8 Elite and 8 Gen 2 phones, one core with the NPU signs 1.28 to 1.35 and 1.74 to 1.82 times faster than two cores.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2486) | 2026-10-14
