---
title: "Homomorphic Functional Encryption: Trustless Key Derivation for Functional Encryption"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1921"
summary: "In this paper, we study the trust assumptions underlying key generation in functional encryption (FE) schemes, as well as the information leakage that can arise from the use of functional decryption k"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

In this paper, we study the trust assumptions underlying key generation in functional encryption (FE) schemes, as well as the information leakage that can arise from the use of functional decryption keys. FE schemes typically rely on a trusted key curator who holds the master secret key and derives functional decryption keys. This requirement makes the curator a central point of trust and a particularly sensitive target for compromise. We show how homomorphic encryption (HE) can be used to mitigate this problem by allowing FE key-derivation algorithms to be evaluated homomorphically. Building on prior work on function-blind key derivation [CHL20], we extend this approach to a three-party deployment in which the key curator does not hold the FE master secret key in the clear. The resulting construction preserves function blindness while protecting the master secret key from the curator, thereby reducing the trust assumptions associated with conventional FE key management. Additionally, to test the applicability of our approach, we made a proof-of-concept implementation and ran a series of benchmarks. Finally, as a way to support open science and reproducible research, we make our code publicly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1921) | 2026-09-08
