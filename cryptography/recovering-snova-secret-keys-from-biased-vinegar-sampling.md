---
title: "Recovering SNOVA Secret Keys from Biased Vinegar Sampling"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2154"
summary: "The Round-3 SNOVA signer samples vinegar variables, which are elements of F_q, by reducing uniform byte strings modulo a power of q. We show that the resulting bias leaks secret-key information for th"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The Round-3 SNOVA signer samples vinegar variables, which are elements of F_q, by reducing uniform byte strings modulo a power of q. We show that the resulting bias leaks secret-key information for the six odd-characteristic alternative parameter sets. Even though the leakage is small (the most leaky variables leak at most 0.086 bits of information), this still leads to efficient key-recovery attacks which we demonstrate in practice. Key recovery becomes a q-ary LPN problem of dimension oell with a known, full-support error distribution. A naive algorithm needs some ten thousand signatures and 2^{90} to 2^{130} operations, which is already far below the 170 to 331 bits claimed for the six affected sets. Using more signatures makes the attack practical: using standard LPN machinery - BKW reduction with Fourier hypothesis testing - we recover the secret key for four parameter sets in practice using between 9 and 180 million signatures, and at most 16 minutes of wall clock time. Fixing SNOVA to sample the vinegar variables uniformly would prevent the attack completely.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2154) | 2026-09-22
