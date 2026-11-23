---
title: "Chosen-Ciphertext Security for Nested Proxy Re-Encryption with Restricted Key Exposure"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2979"
summary: "Proxy re-encryption (PRE) allows an authorised proxy to re-encrypt ciphertexts for another recipient without learning their plaintexts. We construct a single-hop PRE scheme with restricted chosen-ciph"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Proxy re-encryption (PRE) allows an authorised proxy to re-encrypt ciphertexts for another recipient without learning their plaintexts. We construct a single-hop PRE scheme with restricted chosen-ciphertext security (rCCA2). For a given honest delegator, an adversary that obtains an outgoing re-encryption key cannot also obtain re-encryptions to corrupted recipients. We revisit the nested encryption of Ivan and Dodis (NDSS 2003) with the encrypted delivery of the inner secret key described by Ateniese et al. (ACM TISSEC 2006). A recipient can recover this key from one authorised delivery and use it to decrypt inner ciphertexts sent to others. Encrypting each inner ciphertext under an independent public key of its intended recipient gives a scheme secure against restricted honest re-encryption attacks (rHRA). To obtain rCCA2, we use CCA2-secure public-key encryption, authenticate source ciphertexts and encrypted inner secret keys with strongly unforgeable signatures, and protect inner ciphertexts with deterministic authenticated encryption during re-encryption. We instantiate rCCA2 using hybrid public-key encryption with ML-KEM, ML-DSA signatures, and AES-SIV, and give key and ciphertext sizes. A packet-level OpenPGP prototype forwards the session key in a separate envelope and verifies decryption of the same encrypted body by the original and forwarding recipients.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2979) | 2026-11-22
