---
title: "Auditable Continuous Group Key Agreement"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1710"
summary: "Continuous group key agreement (CGKA), the cryptographic core of Messaging Layer Security (MLS, RFC 9420), provides key management for large end-to-end encrypted group chats. It refreshes the group's "
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

Continuous group key agreement (CGKA), the cryptographic core of Messaging Layer Security (MLS, RFC 9420), provides key management for large end-to-end encrypted group chats. It refreshes the group's keys as members join and leave, but offers no way for a designated auditor to recover past epoch keys, and no way to check that such recovery remains possible. Regulated deployments in finance, healthcare, and government therefore resort to plaintext server logging, abandoning end-to-end encryption entirely. Simply adding a key escrow admits a silent escrow failure: the group accepts an epoch whose escrow holds unrecoverable material, with no visible anomaly until a later audit. Addressing this, we introduce auditable CGKA (Au-CGKA), an MLS-shaped protocol in which every admitted epoch carries a proof. The proof binds that epoch's key material to a well-defined secret recoverable by a threshold auditor committee. Every member checks that binding against the epoch secret it derives and refuses the commit if the two disagree, so auditability guarantees that the secret of every epoch an honest member accepts is threshold-recoverable. We give a post-quantum protocol, Π_A, realizing this property with STARK proofs. The committer escrows the epoch secret to an auditor committee, and the escrow ciphertext is a STARK-friendly encryption of Shamir shares. Its well-formedness is proven in-circuit at MLS commit time. We prototype Au-CGKA in Rust with the proofs on a zero-knowledge, post-quantum custom multi-stage STARK. On an Apple M5 Pro, an auditability proof takes 1.38 s with proof-size 15.31 MB and verifies in 0.17 s, at every group size; the relation it proves is independent of the group size. The proof is checked at admission and then discarded, so it costs bandwidth on the commit and nothing in storage; the only persistent overhead is the fixed-size escrow. Adaptive post-quantum security holds in the secure-erasure model with straight-line reductions in the quantum random-oracle model, and carries to the implemented backend under a stated assumption; privacy and escrow soundness follow as game-based guarantees.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1710) | 2026-08-17
