---
title: "Threshold Batched Attribute-Based Encryption from Succinct LWE"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2822"
summary: "Batched identity-based encryption (BIBE) enables a single compact key to decrypt ciphertexts associated with a designated batch of identities. Batched attribute-based encryption (B-ABE) extends this f"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Batched identity-based encryption (BIBE) enables a single compact key to decrypt ciphertexts associated with a designated batch of identities. Batched attribute-based encryption (B-ABE) extends this functionality to attribute-based access control, while threshold batched attribute-based encryption (TB-ABE) further distributes the decryption capability among multiple parties. Existing constructions of TB-ABE rely on bilinear pairings, motivating post-quantum alternatives. In this work, we give, to the best of our knowledge, the first lattice-based candidate construction of TB-ABE. Our construction combines the succinct polynomial-digest mechanism underlying lattice-based BIBE with key-homomorphic evaluation for arithmetic-circuit policies and linear secret sharing. We prove security under the ℓ-succinct LWE assumption, assuming the required share-uniformity property of the underlying ramp threshold sharing scheme.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2822) | 2026-11-08
