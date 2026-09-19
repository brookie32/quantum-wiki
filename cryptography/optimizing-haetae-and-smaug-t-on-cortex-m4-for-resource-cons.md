---
title: "Optimizing HAETAE and SMAUG-T on Cortex-M4 for Resource-Constrained IoT Devices"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2066"
summary: "The practicality of post-quantum cryptography (PQC) on IoT devices depends on both operation cycle counts and communication costs from public values (public keys, ciphertexts, and signatures). The DSA"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

The practicality of post-quantum cryptography (PQC) on IoT devices depends on both operation cycle counts and communication costs from public values (public keys, ciphertexts, and signatures). The DSA HAETAE and the KEM SMAUG-T, both selected in the KpqC competition, provide smaller public values than ML-DSA and ML-KEM; however, the lack of platform-specific optimization leaves their operation cycle counts high, which can offset this advantage. In this paper, we optimize HAETAE and SMAUG-T on the Cortex-M4, a representative 32-bit embedded MCU, and conduct a multi-faceted evaluation. We fix two bugs in the existing implementation of the HAETAE N(mathbf{s}) evaluation and propose Autocorrelation-based Spectral-Norm Evaluation (ASNE), which replaces the per-polynomial FFTs with a single autocorrelation FFT. Together with further optimizations, we achieve improvements of up to 309.1%, 4.8%, and 6.0% in KeyGen, Sign, and Verify, respectively, over the state-of-the-art implementation. For SMAUG-T, we analyze the coefficient ranges of the polynomial multiplication operands to select an auxiliary NTT-friendly modulus q', and count the number of operations per layer to apply the optimal NTT. As a result, we achieve improvements of up to 266.7%, 348.9%, and 341.0% in KeyGen, Encaps, and Decaps, respectively, over the reference C implementation. Furthermore, we apply static analysis and dudect measurements to the optimized kernels and observe no evidence of timing leakage. Using models anchored to prior IoT protocol measurements, we estimate the transmission-unit count, end-to-end latency, and energy, showing that HAETAE and SMAUG-T can be competitive PQC alternatives in constrained wireless environments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2066) | 2026-09-17
