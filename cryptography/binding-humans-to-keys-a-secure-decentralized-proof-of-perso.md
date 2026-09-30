---
title: "Binding Humans to Keys: A Secure Decentralized Proof of Personhood Protocol"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2246"
summary: "Decentralised proof of personhood, cryptographically binding a digital identity to a unique living human without a trusted central authority, is a foundational problem in permissionless networks. We p"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Decentralised proof of personhood, cryptographically binding a digital identity to a unique living human without a trusted central authority, is a foundational problem in permissionless networks. We present a novel protocol, Secure-GYID (S-GYID), resilient to Identity Theft Attack (i.e., adversarial authorities substitute a victim's biometric fingerprint under a malicious public key) and Ghost Key Attack (i.e., colluding authorities fabricate a registration for a non-existent user). Our protocol closes both vulnerabilities by replacing raw biometric transmission with an encryption-based digital fingerprint derivation F = E(pk_u, P_u) computed under a one-way, chosen-plaintext-secure, deterministic scheme, so that no authority can substitute or forge a binding pair without knowledge of the user's secret key. S-GYID further introduces a three-stratum generational authority hierarchy with bounded tenure and VRF-based session selection to limit long-term collusion structurally. We prove Identity Theft Resistance, Biometric Detectability, and Ghost Key Resistance under standard cryptographic assumptions, and provide a hypergeometric session-capture analysis that establishes concrete parameter design rules for both the key activation and authority promotion thresholds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2246) | 2026-09-28
