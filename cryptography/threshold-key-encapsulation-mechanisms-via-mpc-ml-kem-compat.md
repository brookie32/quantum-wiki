---
title: "Threshold Key Encapsulation Mechanisms via MPC: ML-KEM Compatibility and Optimization"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2220"
summary: "There is currently a strong interest in designing standard-compatible threshold cryptographic primitives, a trend bolstered by NIST's Call for Multi-Party Threshold Schemes (NIST IR 8214C). While Mult"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

There is currently a strong interest in designing standard-compatible threshold cryptographic primitives, a trend bolstered by NIST's Call for Multi-Party Threshold Schemes (NIST IR 8214C). While Multi-Party Computation (MPC) can be applied to the construction of threshold Key Encapsulation Mechanism (KEM) from NIST standard ML-KEM scheme to preserve the compatibility with ML-KEM, such a direct construction yields a high number of threshold decapsulation rounds as many as 384 for MK-KEM-512. In this paper, we optimise the round complexity of MPC-based threshold ML-KEM decapsulation. Our first construction (Scheme A) uses masked predicates, parallel coin expansion and global scheduling methods to improve the round complexity of MPC-based ML-KEM decapsulation, while maintaining ML-KEM encapsulation, public key and ciphertext formats. For ML-KEM-512, 768 and 1024, our construction improves the round complexity to 145, 218, and 290, respectively. We also introduce a variant (Scheme B) that uses an MPC-friendly variant of Kyber KEM and KangarooTwelve hash to further improve the round complexity to 35 at the security level of ML-KEM-512, without full ML-KEM compatibility. In the semi-honest MPC model, we prove Scheme A security by exact composition with ML-KEM, and Scheme B IND-CCA security in the QROM from Module-LWE and negligible decryption failure.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2220) | 2026-09-25
