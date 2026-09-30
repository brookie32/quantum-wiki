---
title: "PQMZ: Formally Verified Falcon-PKR for Post-Quantum Cryptographic Migration in Zcash"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2260"
summary: "Migrating blockchain systems to Post-Quantum Cryptography (PQC) requires not only replacing classical primitives, but also analysing transformations that change how signatures are represented and veri"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Migrating blockchain systems to Post-Quantum Cryptography (PQC) requires not only replacing classical primitives, but also analysing transformations that change how signatures are represented and verified. We study Falcon-PKR, a public-key-recovery variant of Falcon, motivated by Zcash-like transparent transaction workflows. Falcon-PKR replaces explicit storage of the full Falcon public key with a compact stored digest and reconstructs a candidate public key from the signature during verification. In our construction, this reduces the combined representation size of public key and signature by approximately 15%, but it also introduces a distinct security case in which verification depends on a reconstructed key derived from adversarially supplied signature data. We address this with a machine-checked EasyCrypt formalisation in the Random Oracle Model (ROM). We mechanically verify an EUF-CMA reduction showing that the security of Falcon-PKR is bounded by the security of standard Falcon together with collision resistance of a domain-separated public-key hash. The analysis therefore treats both assumptions explicitly and does not claim a proof of Falcon itself. We also machine-check correctness for honest signing under an abstract Falcon signing interface. We implement Falcon-PKR for Falcon-512 and Falcon-1024 in Python and C, and evaluate runtime and size against ECDSA and selected Post-Quantum (PQ) alternatives, exposing explicit verification and storage trade-offs. As a complementary case study, we implement and analyse an extended SECUER-based Multi-Party Computation (MPC) ceremony architecture. Together, the two case studies address both transaction-signature and ceremony-infrastructure layers of PQ blockchain migration.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2260) | 2026-09-29
