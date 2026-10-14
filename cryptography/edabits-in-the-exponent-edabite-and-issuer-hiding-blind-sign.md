---
title: "edaBits in the Exponent (edaBitE) and Issuer-Hiding Blind Signatures from ML-DSA and VOLE-in-the-Head"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2473"
summary: "Blind signatures let a user obtain a signature by interacting with an issuer that controls the signing key, while the issuer never sees the message. They form the basis of anonymous credentials, which"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Blind signatures let a user obtain a signature by interacting with an issuer that controls the signing key, while the issuer never sees the message. They form the basis of anonymous credentials, which are the centerpiece of privacy-preserving digital identification to be deployed widely in the coming years. Existing plausibly quantum-secure blind signatures rely on bespoke cryptographic constructions, instead of standardized ones. This is dissatisfying from a cryptographic perspective, and also leads to practical issues: secret signing keys are often stored in secure elements, in which case only signature algorithms supported by certified secure elements can be the basis for deployed protocols. We give the first blind signature whose issuer runs a NIST-standardized post-quantum signature scheme unmodified. Issuance is just an ML-DSA signature on a commitment, and the blind signature is a zero-knowledge proof of knowledge, using the VOLE-in-the-head zero-knowledge proof system, of the ML-DSA signature. Security reduces to the EUF-CMA security of ML-DSA and to the proof system, with no new assumptions. A blind signature is about 1 MB and takes under a second to produce and half a second to verify. Issuer-hiding and selective disclosure of signed attributes can easily be added on top for a few tens of kilobytes, at a proof size essentially independent of how many issuers the list names. Underlying the construction is edaBitE, a novel batch consistency check between binary and prime-field commitments. In a non-interactive proof, the existing edaBits checks it replaces would be the single largest item in the blind signature. We believe that edaBitE is of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2473) | 2026-10-14
