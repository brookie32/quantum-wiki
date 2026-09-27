---
title: "Provenance Proofs: Linkable Zero-Knowledge Derivation Relations for Hierarchical Deterministic Wallets"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2204"
summary: "ZKPoSP proves that a public key or address was honestly derived from a hidden wallet seed, without revealing the seed or the private derivation state. This paper studies relationships among several de"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

ZKPoSP proves that a public key or address was honestly derived from a hidden wallet seed, without revealing the seed or the private derivation state. This paper studies relationships among several derived values: whether public keys or addresses, possibly on different curves and different blockchains, share a hidden origin, which is the seed or an anchor of the wallet, and who else can recognize this relation. We give a model for such provenance proofs, with derivation proofs, which carry a link value, and provenance proofs, which show that several derivation statements share an origin. We define correctness, derivation soundness, provenance soundness, non-frameability and unlinkability. We give four constructions, which differ in who can link: only the user, with a joint proof or with commitments linked later; anyone within a linking context, with a deterministic tag, which can also act as a nullifier; or a designated authority, with an encryption of that tag. We prove, in sketch form, that the constructions satisfy the five properties under the security of the ZKPoSP derivation relations, the random oracle model, and the zero knowledge and simulation extractability of the proof system. We describe an application to cross-chain transfers from Bitcoin to Solana, in which the payout address must come from the same wallet as the source address, so that an attacker cannot substitute the destination. We report Plonky3 benchmarks of the derivation proofs on which the constructions are built.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2204) | 2026-09-24
