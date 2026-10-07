---
title: "Simple Extremely Lossy Functions from Small-Exponent Hashing"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2367"
summary: "Extremely Lossy Functions (ELFs) are a standard model primitive that captures many useful properties of random oracles (Zhandry, Crypto 2016). While there are many variations of ELFs with additional p"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Extremely Lossy Functions (ELFs) are a standard model primitive that captures many useful properties of random oracles (Zhandry, Crypto 2016). While there are many variations of ELFs with additional properties, every construction (excluding obfuscation) has followed essentially the same template of bootstrapping from a sequence of ELFs secure only against fixed-size adversaries, and every construction was based on only the exponential hardness of DDH (or k-Lin), an assumption that is only reasonable over elliptic curves. We introduce and construct Extremely Lossy Trapdoor Hashing (ELTDH), a stronger notion that implies all known variations of ELFs. Our construction achieves ELTDH in one go, without bootstrapping from schemes secure for only fixed-size adversaries, which makes it simpler and more efficient than existing ELFs. We assume exponential security of the small-exponent discrete logarithm, together with polynomial security of decisional composite residuosity (DCR). Exponential security is only required in the size of the secret exponent, not the size of the group, so the assumption plausibly holds for multiplication modulo N^2 (and for many other cryptographic groups), despite the subexponential-time discrete logarithm attacks from index calculus. Our results diversify the assumptions underlying ELFs, while also giving a simpler construction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2367) | 2026-10-05
