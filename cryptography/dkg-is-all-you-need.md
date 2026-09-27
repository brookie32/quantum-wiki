---
title: "DKG Is All You Need"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2205"
summary: "We construct the first Batched Threshold Encryption scheme with a transparent setup where public parameters are independent of the batch size. As a result batches of arbitrary sizes can be decrypted, "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We construct the first Batched Threshold Encryption scheme with a transparent setup where public parameters are independent of the batch size. As a result batches of arbitrary sizes can be decrypted, without imposing an a priori fixed bound. We prove security under a constant size assumption -- the decisional bilinear square Diffie-Hellman assumption. Setup is just a distributed key generation protocol to sample secret shares of a random value. Ciphertexts consist of two G1 elements, one G2 element and the encrypted message, plus a NIZK for CCA security (two F elements with a sigma protocol). Partial decryptions are a single G1 element, computed with one scalar multiplication. Decrypting a batch of B ciphertexts costs O(B) pairings and O(B log^2 B) group operations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2205) | 2026-09-24
