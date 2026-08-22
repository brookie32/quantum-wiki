---
title: "L-BAS: A Lattice-Based Blind Adaptor Signature Scheme"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1752"
summary: "Lattice-based blind signatures have attracted significant attention in recent years due to the rapid growth of digital currencies, the increasing demand for privacy-preserving digital interactions, an"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Lattice-based blind signatures have attracted significant attention in recent years due to the rapid growth of digital currencies, the increasing demand for privacy-preserving digital interactions, and the ongoing transition toward quantum-resistant cryptographic primitives. While blind signatures provide anonymity guarantees, achieving fairness without compromising privacy to a third party remains a challenging problem. Blind adaptor signatures (BAS) address this limitation by enriching blind signatures with conditional-execution functionality, enabling fair exchange while preserving user anonymity. In particular, a BAS scheme allows a user to engage in an atomic swap with a verifier using an adapted blind signature obtained from a signer, thereby maintaining privacy against the signer while ensuring fairness between the user and the verifier. In this work, we observe that the ABDLOP commit-and-prove framework (CRYPTO 2022) exhibits a dichotomic structure that can be leveraged to realize adaptor functionality. Building on this, we propose a lattice-based blind adaptor signature (L-BAS) scheme that simultaneously achieves fairness along with the privacy guarantees of blind signing. Compared with the underlying lattice-based blind signature scheme, our construction incurs only a modest overhead, increasing the signature size by approximately 5.2 KB while largely preserving the efficiency of the original system. We formally analyze the security of the proposed construction and prove that it satisfies extractability, unique extractability, computational pre-verification soundness, one-more unforgeability, and blindness under standard lattice-based assumptions. Our results demonstrate that fairness can be incorporated into lattice-based blind signatures with minimal performance degradation, making the proposed scheme a practical candidate for privacy-preserving and quantum-resistant fair exchange applications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1752) | 2026-08-20
