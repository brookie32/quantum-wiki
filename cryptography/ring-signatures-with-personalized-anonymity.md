---
title: "Ring Signatures with Personalized Anonymity"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1709"
summary: "Ring signatures have long struggled to balance absolute anonymity with traceability. While various extensions, such as traceable and accountable ring signatures, have been proposed, they typically app"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

Ring signatures have long struggled to balance absolute anonymity with traceability. While various extensions, such as traceable and accountable ring signatures, have been proposed, they typically apply a uniform anonymity or traceability rule to all potential signers. This paper introduces personalized-anonymity ring signatures (PARS), a novel primitive in which users are certified with different anonymity rights according to their roles or authority. Unlike ordinary ring signatures, PARS involves a group manager at key issuance; however, the group manager does not determine a fixed signing group. Instead, signers retain the ring-signature feature of choosing the ring at signing time, while the manager certifies whether each user's key permits fully anonymous signing or only traceable signing. This model is particularly suited for organizational governance, where ordinary members may require strong anonymity for internal reporting or expressing dissenting opinions, while users with institutional authority must remain accountable for official approvals or authorizations. We provide a formal syntax and rigorous security definitions for PARS, capturing both standard ring-signature requirements and traceability-related guarantees. We then present a generic construction from standard cryptographic primitives, including digital signatures, one-time signatures, public-key encryption, and non-interactive zero-knowledge proofs of knowledge.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1709) | 2026-08-17
