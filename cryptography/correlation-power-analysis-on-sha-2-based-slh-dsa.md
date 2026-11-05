---
title: "Correlation Power Analysis on SHA-2-Based SLH-DSA"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2753"
summary: "The stateless hash-based digital signature algorithm (SLH-DSA) repeatedly processes a fixed secret seed with varying public addresses. This paper presents non-profiled correlation power analysis of th"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The stateless hash-based digital signature algorithm (SLH-DSA) repeatedly processes a fixed secret seed with varying public addresses. This paper presents non-profiled correlation power analysis of the address-based pseudorandom function for all six SHA-2 parameter sets, using separate recovery paths through SHA-256 compression rounds and message-schedule expansion. The procedures account for the input layout in which a 22-byte compressed address precedes the secret seed. For the 256-bit sets, a two-stage joint procedure recovers two 16-bit secret portions. We evaluate an STM32F303 ARM Cortex-M4 implementation using 30 secret seeds and 5,000 measured power traces per seed for each evaluated condition. Each recovery stage is evaluated with the required preceding secret values supplied correctly; the reported rates are therefore conditional stage-wise results, not end-to-end seed recovery rates. Compression-round stages achieve 100% success under both forest-of-random-subsets and Winternitz one-time-signature-plus address conditions. Under forest-of-random-subsets addresses, all message-schedule stages achieve 100% success for the 128- and 192-bit sets. For both 256-bit variants, joint recovery achieves 100%, whereas recovery of message word W_{12} achieves 66.7%; recovery of W_7 achieves 70.0% and 80.0% for the fast and small variants, respectively. An alternative first stage is also provided for 128-bit Winternitz one-time-signature-plus addresses. These results show that side-channel protection must cover both compression rounds and message-schedule expansion.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2753) | 2026-11-04
