---
title: "BMRaccoon: Blind Multi-Signatures from Lattices"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2870"
summary: "Blind multi-signatures (BMS) allow a user to obtain a compact signature on a hidden message through the joint participation of multiple signers, providing a basis for decentralized issuance of anonymo"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

Blind multi-signatures (BMS) allow a user to obtain a compact signature on a hidden message through the joint participation of multiple signers, providing a basis for decentralized issuance of anonymous tokens.We present BMRaccoon, the first lattice-based post-quantum BMS construction, with a two-round signing protocol secure under concurrent sessions and signatures syntactically compatible with Raccoon under the sum of the signers' verification keys. As a building block, we introduce MRaccoon, the first Raccoon-based multi-signature and prove its strong unforgeability under the Algebraic One-More MISIS (AOM-MISIS) and MSIS assumptions in the random oracle and and knowledge-of-secret-key (KOSK) model. Our modular security analysis establishes one-more unforgeability of BMRaccoon via a straight-line reduction to the strong unforgeability of MRaccoon, modelling the user's blinding contribution as an auxiliary signer with a zero verification key. We additionally prove blindness against malicious, colluding signers. For up to q_s = 2^{32} signing sessions and n = 32 signers, our concrete instantiation yields signatures of approximately 67 KB and verification keys of approximately 15 KB.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2870) | 2026-11-11
