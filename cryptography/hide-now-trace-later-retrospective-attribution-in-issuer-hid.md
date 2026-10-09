---
title: "Hide Now, Trace Later: Retrospective Attribution in Issuer-Hiding Credentials"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2396"
summary: "Attribute-based credentials (ABCs) enable privacy-preserving authentication by allowing users to prove statements about certified attributes without revealing unnecessary information. However, while A"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Attribute-based credentials (ABCs) enable privacy-preserving authentication by allowing users to prove statements about certified attributes without revealing unnecessary information. However, while ABCs hide undisclosed attributes, the credential verification process inherently reveals the issuer's identity, which can leak contextual information such as a user's nationality or residency. Issuer-hiding ABCs address this by concealing the issuer during verification, but introduce a critical accountability problem: if an issuer is compromised or acts maliciously, previously accepted presentations originating from that issuer cannot be singled out without significant privacy violation and high burden on the central authority performing the inspection. We propose an issuer-inspection mechanism that enables retrospective attribution while preserving privacy. An inspection authority can release keys allowing verifiers to locally identify presentations originating from a specific compromised issuer and a defined time period, without affecting other issuers or earlier time periods. Concretely, we formalize the syntax and security requirements of issuer inspection and provide a generic construction from standard cryptographic building blocks; we further present a concrete pairing-based instantiation using Groth's randomizable structure-preserving signatures, Schnorr-style proofs and an adaptation of Gentry's anonymous identity-based encryption. Our analysis of computational and communication costs indicates that the proposed functionality remains practical for realistic parameter choices.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2396) | 2026-10-07
