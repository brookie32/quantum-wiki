---
title: "On Post-Quantum Multi-Key Security of GCM"
date: "2026-08-18"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1718"
summary: "This paper studies the post-quantum multi-key security of Galois/Counter Mode (GCM) in the Quantum Ideal Cipher Model (QICM). GCM is one of the most widely deployed AEAD schemes. In practice, widely d"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

This paper studies the post-quantum multi-key security of Galois/Counter Mode (GCM) in the Quantum Ideal Cipher Model (QICM). GCM is one of the most widely deployed AEAD schemes. In practice, widely deployed cryptosystems are often instantiated under many independent keys, making the multi-key setting practically relevant. A trivial extension of a single-key security bound to the multi-key setting incurs a security loss proportional to the number of keys. In particular, in the post-quantum setting, the term corresponding to exhaustive key search becomes up^2/2^k, where u is the number of keys and k is the key length. Here, u is the number of keys, k is the key length, and p is the number of quantum queries to the underlying block cipher E and its inverse, which serves as a coarse measure of the amount of offline (quantum) computation performed by the adversary. For example, when u=2^{32}, the trivial bound does not guarantee security for p geq 2^{48} when k=128, and even for k=192, it ceases to guarantee security for p geq 2^{80}. We show that, at the cost of some additional loss terms, the term up^2/2^k can be replaced by a term of order sqrt{dp^2/2^k}, where d denotes the maximum number of keys under which the same nonce appears in encryption queries. Thus, when d is much smaller than u (and the additional loss terms remain small), our bound improves upon the trivial multi-key bound. This can be viewed as a post-quantum counterpart of the classical result of Hoang et al. (CCS 2018). As in their work, we further show that, for randomized nonce-generation mechanisms that abstract patterns used in protocols such as TLS, the parameter d remains small even when u is large. Although our bounds are not tight and leave room for improvement, they yield a notable improvement over the trivial multi-key bound for several concrete parameter settings. To the best of our knowledge, this is the first non-trivial post-quantum multi-key security bound for an AEAD mode in the QICM. Our proof combines the reprogramming-and-resampling approach of Alagic et al. (EUROCRYPT 2022) with counting arguments used in the classical multi-user analysis of GCM by Hoang et al.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1718) | 2026-08-18
