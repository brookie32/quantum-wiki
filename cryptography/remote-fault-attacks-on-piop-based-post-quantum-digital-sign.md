---
title: "Remote Fault Attacks on PIOP-based Post-Quantum Digital Signatures using Statistical Ineffective Fault Analysis"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3019"
summary: "The threat posed by quantum computing has necessitated the replacement of existing public-key cryptographic algorithms. NIST is currently running the third round of a competition to identify additiona"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The threat posed by quantum computing has necessitated the replacement of existing public-key cryptographic algorithms. NIST is currently running the third round of a competition to identify additional post-quantum digital signature schemes beyond the ML-DSA and SLH-DSA standards. Among the competition's remaining candidates are MQOM, FAEST, and SDitH, based on Polynomial Interactive Oracle Proof (PIOP) protocols. They are favoured for standardisation due to their conservative security assumptions. In this paper, we present a remote fault attack that recovers the secret key of these schemes by targeting the polynomials underlying the PIOP protocol. The attack employs Statistical Ineffective Fault Analysis (SIFA), a powerful method introduced in 2018 in the context of AES. We demonstrate the attack end-to-end using Rowhammer. To the best of our knowledge, this is the first remote attack on a post-quantum cryptographic signature scheme capable of bypassing fault detection countermeasures. Previous attacks relied on fault models impractical for remote exploitation. In addition, we present a novel approach to bypass Address Space Layout Randomisation (ASLR) that reliably determines the ASLR-induced intra-page offset from a single set of stack accesses during libc initialisation. Furthermore, we refine existing approaches for acquiring physically contiguous memory and propose countermeasures against the presented attack.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3019) | 2026-11-24
