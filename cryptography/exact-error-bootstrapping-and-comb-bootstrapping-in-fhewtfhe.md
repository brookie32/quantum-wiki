---
title: "Exact Error Bootstrapping and Comb Bootstrapping in FHEW/TFHE"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2630"
summary: "In FHEW and TFHE, bootstrapping evaluates the decryption function via a blind rotation, whose resolution limits the message space. We propose instead to bootstrap the error. By rounding the ciphertext"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

In FHEW and TFHE, bootstrapping evaluates the decryption function via a blind rotation, whose resolution limits the message space. We propose instead to bootstrap the error. By rounding the ciphertext at a resolution that is a multiple of the message modulus, we preserve the message exactly. Reduction modulo a small integer then yields a noise-free encryption of the error, which a single blind rotation lifts exactly before it is subtracted. The message modulus is thus constrained solely by the noise and can be much larger than in standard TFHE. Since the error takes far fewer distinct values than the ring degree, a single blind rotation can also refresh several ciphertexts simultaneously. We call this procedure the comb bootstrap. Between refreshes, an integer remains encrypted in a single ciphertext, allowing additions modulo the message modulus and multiplications without programmable bootstrapping. Built on TFHE-rs, for 8-bit integers on a single thread, our refresh is 3.5 times faster than that of TFHE-rs, and 9.1 times faster with the comb bootstrap; multiplication is 6.5 times faster. In a residue number system, multiplication of integers modulo widehat Pge 2^{32} is 19 times faster than in TFHE-rs. The error bootstrap serves exclusively to refresh ciphertexts; evaluating any other function still requires programmable bootstrapping.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2630) | 2026-10-24
