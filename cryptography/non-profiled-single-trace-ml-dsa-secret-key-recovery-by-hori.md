---
title: "Non-profiled Single-Trace ML-DSA Secret Key Recovery by Horizontal Distribution Analysis"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2643"
summary: "During the last decade, single-trace side-channel attacks on cryptographic implementations have largely focused on profiled methods, which typically assume that the attacker has a clone device and imp"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

During the last decade, single-trace side-channel attacks on cryptographic implementations have largely focused on profiled methods, which typically assume that the attacker has a clone device and implementation knowledge to build a leakage model for the target before launching the attack. In this paper, we demonstrate that a much weaker adversary, without the ability to profile, can also mount powerful single-trace attacks. The presented method compares the observed sample distribution with the expected Hamming weight leakage distribution using a Gaussian mixture model as a distinguisher. The horizontal nature of the attack allows us to obtain multiple observations per execution by partitioning and stacking the trace. We show how to select optimal parameters for trace preprocessing and configure the measurement setup so that the noise floor is lowered, enabling the exploitation of weak leakage. We also prove that imperfect classifications can be efficiently corrected using information-set decoding algorithms. The new method is evaluated on an optimized implementation of ML-DSA-65 on ARM Cortex-M4 using the secret key unpacking procedure as an attack point. With an enumeration budget of 2^{70} operations in mathbb Z_q, the full secret key is recovered from a single trace in 99% of attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2643) | 2026-10-26
