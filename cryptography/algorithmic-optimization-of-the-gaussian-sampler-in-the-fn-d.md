---
title: "Algorithmic Optimization of the Gaussian Sampler in the FN-DSA Post-Quantum Signature Scheme"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1610"
summary: "The post-quantum signature scheme Falcon (FN-DSA), currently being standardized by NIST as FIPS 206 (Initial Public Draft submitted August 2025, final standard expected 2026-2027), relies on a discret"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

The post-quantum signature scheme Falcon (FN-DSA), currently being standardized by NIST as FIPS 206 (Initial Public Draft submitted August 2025, final standard expected 2026-2027), relies on a discrete Gaussian sampler whose critical bottleneck is the function fpr_expm_p63, computing lfloor exp(-x) dot 2^{63} rfloor for x in [0, ln 2). While the reference implementation already employs a degree-12 fixed-point polynomial (FACCT), no segmented approximation has been studied for this specific function, nor has empirical timing security been published on ARM Cortex-M3 (emulated or physical). This paper presents a systematic study of piecewise polynomial approximation applied to fpr_expm_p63, combining the Remez exchange algorithm (computed with 50 decimal digits of precision via mpmath), fixed-point arithmetic, and Horner evaluation. Two configurations are implemented and evaluated: a 32-segment degree-6 approximation at scale 2^{62} targeting x86-64, and a 16-segment degree-3 approximation at scale 2^{31} (256-byte LUT) targeting ARM Cortex-M3 IoT devices without hardware floating-point unit (FPU). Against the authentic FACCT reference from Falcon's fpr.c, ported verbatim to ARM Cortex-M3 (emulated via QEMU user-mode with arm-linux-gnueabi -mfloat-abi=soft), our implementation achieves a 1.28imes median speedup across 30 independent runs (range 1.24imes to 1.33imes), measured with a rigorous anti-noise protocol combining batch measurement, aggressive warm-up, ref/opt interleaving, and percentile filtering (P5-P95). DUDECT timing leakage tests confirm that both the FACCT reference (t-score in [0.05, 2.51]) and our implementation (t-score in [1.99, 5.24]) remain within statistical safety thresholds in the vast majority of runs (FACCT: 30/30; optimized: 27/30). Static instruction-level analysis via objdump disassembly provides deterministic constant-time evidence: zero data-dependent conditional branches, zero FPU instructions, and zero soft-float calls, yielding a branchless fixed-point Horner core; however, the full constant-time claim is limited to the tested compilation target and memory model. To the best of our knowledge, this constitutes the first comparative study of segmented versus global polynomial approximation for fpr_expm_p63 in the FN-DSA context, and the first empirical DUDECT measurement of this function on emulated ARM Cortex-M3 against the authentic FACCT reference. Physical hardware validation on STM32F103 is identified as future work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1610) | 2026-08-04
