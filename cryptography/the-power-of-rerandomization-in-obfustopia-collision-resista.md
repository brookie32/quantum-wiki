---
title: "The Power of Rerandomization in Obfustopia: Collision-Resistant Hash, Somewhere-Extractable BARGs, and More"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1785"
summary: "Indistinguishability obfuscation (iO) combined with one-way functions (OWFs) serves as a powerful foundation for constructing a vast array of cryptographic primitives. However, this combination faces "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Indistinguishability obfuscation (iO) combined with one-way functions (OWFs) serves as a powerful foundation for constructing a vast array of cryptographic primitives. However, this combination faces a known black-box barrier established by Asharov and Segev (FOCS '15), which proves the impossibility of constructing collision-resistant hash (CRH) functions. The Asharov-Segev barrier naturally extends to stronger primitives that imply CRH, such as fully homomorphic encryption (FHE) and somewhere-extractable non-interactive batch arguments (seBARGs). This work investigates the power of iO and rerandomizable primitives in constructing such "CRH-hard" primitives. First, we demonstrate the first direct and simple approach to building CRH from iO and rerandomizable OWFs. The only previously known construction was due to Arnon, Ben-David and Yogev (CRYPTO '25), and needed to go through the construction of the adaptively sound SNARG of Waters and Wu (STOC 24'). Using the same approach, we additionally construct a strictly stronger primitive than CRH, which we call perfectly partitionable hash (PPH), from iO and rerandomizable commitments. Second, we demonstrate the power of rerandomizability for building advanced non-interactive proof systems. Using iO and rerandomizable commitments, we provide a construction of seBARGs with statistical extraction, a security property not achieved by most existing seBARG schemes. By additionally relying on rate-1 fully-homomorphic encryption, we construct the first rate-1 seBARG with statistical extraction. Along the way, we introduce a SNARG that is "sometimes statistically sound", and construct it from iO and rerandomizable commitments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1785) | 2026-08-23
