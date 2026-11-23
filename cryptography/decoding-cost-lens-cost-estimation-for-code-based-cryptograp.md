---
title: "Decoding Cost Lens: Cost Estimation for Code-Based Cryptography"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2994"
summary: "We present Decoding Cost Lens, a platform for evaluating the concrete decoding costs of code-based cryptographic schemes. It maps key- and message-recovery objectives to explicit attack instances, int"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

We present Decoding Cost Lens, a platform for evaluating the concrete decoding costs of code-based cryptographic schemes. It maps key- and message-recovery objectives to explicit attack instances, integrates classical Hamming- and rank-metric estimators, and provides quantum estimates for binary Hamming instances. The evaluation accounts for known block structure and applicable multiple-target effects under stated cost conventions. We apply the platform to 64 parameter sets from 15 first-round candidate schemes in the NGCC call for next-generation commercial cryptographic algorithms, comparing estimated work factors with the specifications' claims and security targets. Four schemes have classical decoding estimates below both the corresponding declared cost and the target for at least one parameter set. Zero-direction maximal minors (ZD-MM) replaces one guessed zero with a search over directions in a single block. For BAG-Loong, the lowest ZD-MM costs are 113.1, 212.3, 299.1 and 386.7 bits in increasing parameter order. ZD-MM also puts key recovery below target for BAG-Piglet-128 and -256 (114.6 and 254.0 bits), and for all three BRA sets (112.1, 161.8 and 316.8 bits) after block transposition. For NSS-HQC, key and baseline message decoding costs fall below the 256-, 384-, and 512-bit classical targets; the corresponding baseline message costs are 226.0, 332.5, and 440.9 bits. NSS-HQC-128 also falls below its declared key-recovery cost while remaining above its target. The estimated quantum baseline message cost for NSS-HQC-512 is 251.6 bits against a 256-bit target.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2994) | 2026-11-23
