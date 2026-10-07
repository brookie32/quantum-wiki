---
title: "Multiplying Not-So-Big Integers with FFTs: Finding and Pushing the Crossover on Large Modern OoO ARM CPUs"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2366"
summary: "Established multiple-precision software generally reserves Fast-Fourier Transform (FFT) multiplication for very large operands; for example, GMP reports full-product FFT thresholds of roughly 3000--10"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Established multiple-precision software generally reserves Fast-Fourier Transform (FFT) multiplication for very large operands; for example, GMP reports full-product FFT thresholds of roughly 3000--10000 limbs. Becker et al. showed that Number-Theoretic Transform (NTT) multiplication can become advantageous much earlier on Cortex-M microcontrollers. It thus becomes an interesting engineering question to check where the crossover actually takes place on a big modern CPU. Our first-generation implementation on Cortex-A76 and Neoverse-N1 shows that the crossover point is around 10k bits when using ARMv8+ with Neon, using optimized and verified code. Motivated by the tighter Barrett bound of Becker, we developed the Second implementation, which eliminates additional reductions and pushes the crossover below 5.6k bits. We integrate our multipliers into OpenSSL RSA, resulting in end-to-end speedup for the public-key operations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2366) | 2026-10-05
