---
title: "When One Bit Is (Almost) Enough: A Low Leakage Chosen Plaintext Side Channel Attack on AES"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2857"
summary: "In order to thwart Side Channel Attacks (SCA) and keep secret safe, countermeasures such as masking can be implemented to hide information. However, when a defect occurs in software or in hardware, a "
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

In order to thwart Side Channel Attacks (SCA) and keep secret safe, countermeasures such as masking can be implemented to hide information. However, when a defect occurs in software or in hardware, a portion of the information may still leak. If the leak is sufficient, the state-of-the-art techniques can still be performed up to a potential brute force search to cover a missing part. However, if only a short portion of the information leaks, the completion of the attack can be hard, and considered as failed. In this paper, we describe a new chosen plaintext strategy on AES algorithm to recover the secret key even in very low leakage condition. As an example, but not limited to, we describe the methodology adapted to one of the worst case scenario: only one bit position leaks over the 128-bit output of SubBytes AES sub-operation along rounds. As a drawback, a heavier cost in terms of number of traces is required due to the chosen plaintext approach.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2857) | 2026-11-10
