---
title: "Pseudorandom Codes from LWE"
date: "2026-10-05"
updated: "2026-10-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2339"
summary: "A pseudorandom code (PRC), introduced by Christ and Gunn (Crypto 2024), is an error-correcting code whose codewords look uniformly random to anyone without the secret key. PRCs not only are natural cr"
last_verified: "2026-10-06"
review_by: "2027-01-04"
stale: false
---

A pseudorandom code (PRC), introduced by Christ and Gunn (Crypto 2024), is an error-correcting code whose codewords look uniformly random to anyone without the secret key. PRCs not only are natural cryptographic objects to study in their own right, but also have interesting applications such as undetectable watermarking of AI-generated content. Previous PRC constructions have centered on Learning Parity with Noise (LPN), often combined with additional assumptions. In particular, the original PRC of Christ and Gunn is based either on standard LPN together with the planted XOR assumption of Agrawal et al. (Crypto 2024), or on subexponential LPN. In this work, we construct PRCs from Learning with Errors (LWE), providing an alternative foundation for PRCs. Our construction is simple: a codeword is the one-bit rounding of an LWE sample, masked by a random string. The construction can be easily understood as an LWE analogue of the PRC of Christ and Gunn. Indeed, like theirs, it is based either on standard LWE together with the hardness of the planted t-SUM problem of Agrawal et al., or on subexponential LWE. However, as the rounding is not linear, its robustness is less straightforward, and we prove it using Fourier analysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2339) | 2026-10-05
