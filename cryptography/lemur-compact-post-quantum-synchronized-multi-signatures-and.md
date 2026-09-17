---
title: "Lemur+: Compact Post-Quantum Synchronized Multi-Signatures and Multi-Hop Aggregation"
date: "2026-09-16"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2054"
summary: "In this work, we introduce Lemur+, a compact post-quantum synchronized multi-signature scheme based on standard lattice assumptions (namely, Module LWE and Module SIS). Lemur+ builds on Lemur (CCS 202"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

In this work, we introduce Lemur+, a compact post-quantum synchronized multi-signature scheme based on standard lattice assumptions (namely, Module LWE and Module SIS). Lemur+ builds on Lemur (CCS 2026) and targets large-scale, long-term distributed applications such as blockchain consensus while supporting non-interactive aggregation. Lemur+ maintains an almost constant signature size of about 56 KB even for one million signers and a 42-year key lifetime, compared to 491 KB in Lemur, yielding about 8.8imes reduction in communication/storage. Our end-to-end implementation demonstrates practical runtime performance: 7.75 s for signature aggregation and 0.29 s for verification with 2^{13} signers. These are roughly within 2imes of the corresponding Lemur runtimes. The key to Lemur+ is our proposed Homomorphic Vector Commitment with Succinct Opening Proof (HVC-SOP), a new primitive that augments standard HVC with succinct opening proofs. We show that HVC-SOP can be generically combined with key-homomorphic one-time signatures (KOTS) to construct non-interactive synchronized multi-signatures, and prove the security of the resulting construction against rogue-key attacks. We then instantiate HVC-SOP using the lattice-based LaBRADOR proof system (CRYPTO 2023), yielding Lemur+. Finally, we extend Lemur+ to support multi-hop aggregation, allowing signatures to be recursively aggregated across distributed network trees. Beyond Lemur+, our HVC-SOP may be broadly applicable and of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2054) | 2026-09-16
