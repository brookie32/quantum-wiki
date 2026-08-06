---
title: "Z-SCAPE: Zero-Knowledge Self-Custodial Credential Operation for Privacy-Preserving Asset Protection under Entropy-Source Failure"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1621"
summary: "Motivated by the 2026 COLDCARD incident, this paper studies cryptographic asset recovery after self-custodial seed-generation failures. Self-custodial hardware wallets depend on secure entropy sources"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Motivated by the 2026 COLDCARD incident, this paper studies cryptographic asset recovery after self-custodial seed-generation failures. Self-custodial hardware wallets depend on secure entropy sources for seed generation. If an RNG implementation or design failure reduces seed entropy, an adversary may reconstruct wallet signing keys through offline search. Such weaknesses may also be discovered long after wallet creation, placing existing self-custodial assets at risk. To prevent large-scale exploitation after such a failure is identified, a hardware manufacturer or security response team may perform a protective sweep of affected assets into a protected recovery treasury. Asset redistribution then creates a fundamental authentication problem: once the signing key can be reconstructed by both the legitimate owner and an adversary, possession of that key no longer uniquely identifies the legitimate controller. We propose Z-SCAPE, a zero-knowledge recovery-credential protocol for privacy-preserving asset recovery after seed-generation failures and protective sweeps. Before compromise, the user commits to a recovery credential consisting of an independently generated 256-bit recovery secret r and an RNG-independent personal record P. After an incident, the prover proves knowledge of (P,r) in zero knowledge while binding the proof to the incident, a fresh verifier nonce, an expiry value and a fresh destination address. The protocol enables recovery claims without revealing P, r or the compromised wallet private keys, while preventing replay and destination substitution. Z-SCAPE provides concrete integration mechanisms for Bitcoin and Ethereum and enables protected assets to be returned only to the fresh destination bound to an accepted recovery proof.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1621) | 2026-08-05
