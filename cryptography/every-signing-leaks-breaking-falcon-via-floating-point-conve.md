---
title: "Every Signing Leaks: Breaking Falcon via Floating-Point Conversion Leakage"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2124"
summary: "Falcon offers compact signatures and well-studied mathematical security, but its side-channel security remains a critical challenge. In particular, its floating-point Gaussian sampler constitutes a ma"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Falcon offers compact signatures and well-studied mathematical security, but its side-channel security remains a critical challenge. In particular, its floating-point Gaussian sampler constitutes a major source of side-channel leakage, while protecting it efficiently is difficult because of its reliance on floating-point arithmetic. However, existing attacks targeting the sampler under realistic noisy-leakage conditions typically require thousands of traces and are evaluated on unoptimized implementations. In this paper, we present a new attack on Falcon's sampler, which reduces the number of required traces by more than two orders of magnitude compared with prior attacks under realistic noisy-leakage conditions and works on both unoptimized (exttt{-O0}) and highly optimized (exttt{-O3}) builds. Our attack targets the floating-point Gaussian centers mu used by the sampler at the recursion leaves of the exttt{ffSampling} procedure. Specifically, it exploits signed-exponent leakage arising when lfloormurfloor is converted from an integer back to floating-point representation, as well as the weaker sign-only leakage. Signed-exponent leakage places the integer part lfloormurfloor of each center in one of 17 signed power-of-two intervals, whereas sign-only leakage divides it into two intervals according to its sign. We propose CB-MLE, which uses gradient descent to obtain an estimate f^star whose computed Gaussian-center classifications are consistent with the observed classifications under the profiled confusion matrix. An ISD-style search tests subsets of the more reliable coefficients in f^star with LLL/BKZ on the corresponding reduced NTRU lattices to recover the full key. We collect power traces from the Falcon implementation in the PQClean library running on an ARM Cortex-M4 microprocessor. Our Gaussian-center classifier achieves single-trace classification accuracies of 0.9997 and 0.884 at the exttt{-O0} and exttt{-O3} optimization levels, respectively, confirming exploitable signed-exponent leakage from the Gaussian centers. Using these classification results, the full attack recovers Falcon-512 keys with success rates of 100% from 20 signatures at exttt{-O0} and 100% from 56 signatures at exttt{-O3}. For Falcon-1024, it reaches 100% from 21 signatures at exttt{-O0} and 100% from 100 signatures at exttt{-O3}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2124) | 2026-09-20
