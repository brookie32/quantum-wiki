---
title: "Adaptively UC-Secure Oblivious Transfer from Group Actions"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2251"
summary: "Oblivious Transfer (OT) is a fundamental building block for secure computation, in which a sender holds two messages and a receiver learns exactly one of them, without revealing which one was chosen a"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Oblivious Transfer (OT) is a fundamental building block for secure computation, in which a sender holds two messages and a receiver learns exactly one of them, without revealing which one was chosen and without learning the other. While generic constructions for Universally Composable (UC) OT exist, instantiating them from post-quantum assumptions remains challenging, particularly under adaptive corruption. In this work, we present the first adaptively UC-secure OT protocol based on Group Actions, specifically assuming weakly pseudorandom Effective Group Actions (EGA) like CSIDH. We adhere to the framework of [BC15], which derives an adaptively UC-secure OT protocol from SPHF-friendly extractable and equivocable (E²) commitment schemes. The central challenge in instantiating this construction from group actions is the lack of SPHF-friendly IND-CCA encryption. Classical CCA transformations such as Fujisaki-Okamoto destroy the algebraic structure required for building SPHFs over ciphertexts, while known group action-based schemes offer no native mechanism to prove ciphertext validity. To overcome this obstacle, we construct from group actions an IND-CCA encryption scheme with enough algebraic structure to efficiently recognize valid ciphertexts. Our contributions are threefold: (1) a verifiable chameleon hash function with perfect soundness in the standard model, (2) an SPHF-friendly, publicly verifiable IND-CCA encryption scheme in the random oracle model, and (3) we combine these to build an SPHF-friendly E² commitment scheme and derive a fully adaptively secure OT protocol in the UC framework. This is the first construction of its kind under group action assumptions, enabling post-quantum secure OT with adaptive security guarantees. These building blocks may also be of independent interest e.g., to obtain digital signatures, non-malleable commitment schemes, or verifiable encryption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2251) | 2026-09-28
