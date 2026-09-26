---
title: "Revisiting Fuzzy Password-Authenticated Key Exchange: Unified Leakage and Improved Efficiency"
date: "2026-09-24"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2196"
summary: "Fuzzy Password-Authenticated Key Exchange (fuzzy PAKE) was introduced at Eurocrypt'18, enabling two parties to securely establish a shared cryptographic key using passwords that are close and potentia"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Fuzzy Password-Authenticated Key Exchange (fuzzy PAKE) was introduced at Eurocrypt'18, enabling two parties to securely establish a shared cryptographic key using passwords that are close and potentially low-entropy. This is a generalization of standard PAKE and is particularly useful for handling mistyped passwords or inherently “noisy” samples such as biometrics. While this primitive sounds promising, existing definitions and protocols face several challenges: they may suffer from gapped leakage (namely, leakage of a small amount of information from failed authentications), or they may be restricted to Hamming distance. We review the functionality and describe our contributions below: 1. Leakage under Reuse. We show that, when a password may be reused across multiple sessions, any leakage from the functionality has the same eventual compromise consequence under repeated use. Concretely, we construct an efficient ideal-world adversary that recovers an n-character password within O(n) active sessions, assuming it starts from a password not too far from the target. Our attack applies to both Hamming distance and Minkowski (L_p) distance under reasonable parameter choices. This implies that, for common distance metrics in practical settings, several notions of leakage are effectively unified when passwords are reused, thereby resolving an open question from Eurocrypt'18. 2. Supporting L_p Distances. We propose substantially more efficient protocols for generalized Minkowski (L_p) and Hamming distances in the random oracle model. As a key technical step, we show how to achieve malicious security using only a semi-honestly secure oblivious key-value store, while addressing several subtleties in the proof. Concretely, compared with existing approaches for L_2 distance, our protocol reduces runtime by about 86% and bandwidth by about 99%.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2196) | 2026-09-24
