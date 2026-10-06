---
title: "Optimizing Montgomery Arithmetic for RSA on Cortex-M0+ and Cortex-M3"
date: "2026-10-05"
updated: "2026-10-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2340"
summary: "Cryptographic tokens that retain RSA credentials for compatibility with existing authentication systems require efficient private-key operations on small processors. Cortex-M0+ (M0+) lacks native wide"
last_verified: "2026-10-06"
review_by: "2027-01-04"
stale: false
---

Cryptographic tokens that retain RSA credentials for compatibility with existing authentication systems require efficient private-key operations on small processors. Cortex-M0+ (M0+) lacks native widening multiplication, whereas Cortex-M3 (M3) provides it with operand-dependent latency. We optimize Montgomery multiplication and squaring using 15-bit limbs and integrate the kernels into RSA-2048 and RSA-3072 private operations based on the Chinese remainder theorem (CRT). On M0+, a wrapped sum and accumulated block quotients enable exact carry recovery. The squaring schedule integrates square and reduction columns without storing the complete square. On M3, we retain the established half-diagonal representation and double each buffer limb when it is first incorporated into Montgomery reduction, eliminating a separate buffer traversal. We establish accumulator bounds for exact Montgomery digit and carry recovery in both schedules. At operand widths of 1024 and 1536 bits, the M0+ representation and register mapping reduce Montgomery multiplication and squaring cycles by 12.60% to 13.11% against blocked two-word controls. The M3 schedule reduces Montgomery squaring cycles by 2.12% to 3.08% with half-diagonal initialization and triangular accumulation held fixed. Kernel replacement in otherwise unchanged RSA implementations reduces warm CRT cycles by 12.59% to 12.80% on M0+ and by 1.69% to 2.39% on M3. Our M3 Montgomery multiplication also uses 31.47% fewer cycles than a reproduced number-theoretic transform (NTT) implementation for 2048-bit operands with matched integers and canonical outputs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2340) | 2026-10-05
