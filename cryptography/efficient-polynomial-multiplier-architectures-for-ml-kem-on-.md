---
title: "Efficient Polynomial Multiplier Architectures for ML-KEM on Resource-Constrained FPGAs"
date: "2026-11-02"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2726"
summary: "The Number Theoretic Transform (NTT) is a key component of polynomial multiplication in Kyber, making its efficient hardware implementation essential for post-quantum cryptographic applications. This "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The Number Theoretic Transform (NTT) is a key component of polynomial multiplication in Kyber, making its efficient hardware implementation essential for post-quantum cryptographic applications. This paper presents two hardware architectures for Kyber polynomial arithmetic, supporting the NTT, inverse NTT (INTT) and point-wise multiplication (PWM) operations. The first architecture employs a single processing element (PE) to reduce hardware area, while the second uses two PEs to achieve higher throughput and efficiency. Both architectures incorporate a low-complexity modular multiplication and reduction method tailored to the Kyber modulus q = 3329, a unified butterfly unit supporting NTT, INTT, and PWM, and constant-geometry data access with dedicated address-generation algorithms. The dual-PE architecture is implemented without dedicated DSP blocks or BRAMs. FPGA implementation results demonstrate that the dual-PE architecture achieves the lowest area-time product and highest frequency among the evaluated state-of-the-art designs, while providing an effective trade-off between hardware area and execution time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2726) | 2026-11-02
