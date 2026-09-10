---
title: "A RAM-Efficient Implementation of Falcon"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1915"
summary: "We present a RAM-efficient implementation of Falcon: RAM usage has shrunk to about 11 kB, down from about 31 kB in the previous implementation of Falcon-512. This code is furthermore faster on Arm Cor"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

We present a RAM-efficient implementation of Falcon: RAM usage has shrunk to about 11 kB, down from about 31 kB in the previous implementation of Falcon-512. This code is furthermore faster on Arm Cortex M4, with average signature generation cost down to 13.45 million cycles. Optimization techniques include a novel variant of the FFT, replacement of some floating-point operations with modular integer computations, delayed addition of input within the Fast Fourier sampling process, and an alternate signature reassembly process. More than half of the floating-point operations have been removed. The resulting implementation is now small enough to allow use in small embedded systems such as smart cards.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1915) | 2026-09-07
