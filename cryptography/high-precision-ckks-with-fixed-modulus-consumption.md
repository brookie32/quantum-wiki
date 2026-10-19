---
title: "High-Precision CKKS with fixed Modulus Consumption"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2531"
summary: "In CKKS, higher precision requires a larger scaling factor, increasing modulus consumption during homomorphic arithmetic and leaving less modulus available after bootstrapping under the same modulus b"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

In CKKS, higher precision requires a larger scaling factor, increasing modulus consumption during homomorphic arithmetic and leaving less modulus available after bootstrapping under the same modulus budget. We introduce Focused CKKS, which trades unused SIMD slots for precision through focused rescaling and key-switching based on cyclotomic units. These units reduce error in selected focus slots while allowing larger error in the background slots. Using only a 1/n fraction of the slots provides approximately n times as many bits of precision at the same scaling factor and CKKS parameter setting. Such a high-precision multiplication requires only a single homomorphic multiplication, with each focus slot supported by n-1 background slots. More generally, the construction supports different precision requirements across slots. We also construct a bootstrapping procedure tailored to Focused CKKS. Only the base modulus at the bottom level needs to grow with the target precision; the remaining bootstrapping computation maintains approximately the same modulus consumption by using fewer slots.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2531) | 2026-10-18
