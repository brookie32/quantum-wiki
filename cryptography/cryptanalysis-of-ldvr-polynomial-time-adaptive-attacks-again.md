---
title: "Cryptanalysis of LDVR: Polynomial-Time Adaptive Attacks against Threshold Schnorr Signatures"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2126"
summary: "We present the first polynomial-time attacks against certain parameter choices of the low-dimensional vector representation (LDVR) problem, introduced by Crites, Katz, Komlo, Tessaro, and Zhu (CRYPTO "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We present the first polynomial-time attacks against certain parameter choices of the low-dimensional vector representation (LDVR) problem, introduced by Crites, Katz, Komlo, Tessaro, and Zhu (CRYPTO '25) to prove the adaptive security of FROST in the Algebraic Group Model. Building on work by Crites and Stewart (CRYPTO '25), they also show that every attack against LDVR directly yields an adaptive attack—i.e., one leveraging adaptive corruptions—against any threshold Schnorr signature that exposes to the attacker the values g^{sk_i} for the secret-key shares sk_i held by the signers, where g is a generator of the underlying group. This class of protocols includes FROST (Komlo and Goldberg, SAC '20), Sparkle (Crites, Komlo, and Maller, CRYPTO '23), Lindell's three-round protocol (CiC '24), along with other masking-free protocols. Consequently, our results give the first polynomial-time adaptive attacks against a class of practical threshold signatures. Our attacks require a large, but still polynomial, number of signers: asymptotically, we require n = Theta(log^2 p) signers and corrupt t_c = Theta(log p) of them. For the prime-order subgroup of Curve25519, concrete and optimized instantiations of our attack require n=5020 signers and corrupt 204 of them. This exceeds the signer counts commonly encountered in practice, but falls within the scenarios considered by NIST's call for threshold signatures. At the theoretical level, our results also yield a non-artificial separation between static and adaptive security based on a real-world multi-party protocol. Our results arise from a new reduction from LDVR to structured subset-sum problems determined by the evaluation points of the polynomial used to secret-share the signing key. We further show that allowing these evaluation points to be chosen adversarially can lead to substantially more efficient attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2126) | 2026-09-20
