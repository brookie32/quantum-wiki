---
title: "Non-Committing Attribute and Identity-Based Encryption: Constructions and Applications"
date: "2026-11-20"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2963"
summary: "A receiver non-committing encryption (RNCE) scheme [Canetti et al., STOC 1996; Canetti et al., TCC 2005] allows one to sample a public key pk and (dummy) ciphertext ct without knowing the message m. L"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

A receiver non-committing encryption (RNCE) scheme [Canetti et al., STOC 1996; Canetti et al., TCC 2005] allows one to sample a public key pk and (dummy) ciphertext ct without knowing the message m. Later, when the message is known, one can sample a secret key sk that looks like the secret key corresponding to pk, and decryption of ct produces m. In this work, we study receiver non-committing attribute-based encryption (RNC-ABE) and identity-based encryption (RNC-IBE). We give constructions based on standard assumptions on bilinear groups (prior works [Hiroka et al., ASIACRYPT 2021] require indistinguishability obfuscation). Our RNC-ABE and RNC-IBE constructions have important implications for incompressible attribute- and identity-based encryption. These notions were recently introduced by Goyal et al., ITCS 2025. However, there were no constructions for the strongest security definitions in Goyal et al., ITCS 2025. Our RNC-ABE and RNC-IBE schemes also lead to the first incompressible ABE and IBE schemes with optimal ciphertext size, which was another open question in Goyal et al., ITCS 2025. We also give constructions for relaxed RNC-IBE (where the identity space is polynomial in the security parameter, but the public key is compact) that are based on mathsf{DDH} or mathsf{LWE}. This leads to a relaxed incompressible IBE scheme with strong security under the same assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2963) | 2026-11-20
