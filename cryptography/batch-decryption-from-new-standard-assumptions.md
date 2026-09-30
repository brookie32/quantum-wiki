---
title: "Batch Decryption from New Standard Assumptions"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2252"
summary: "Batch decryption allows an authority to release a short key that enables public decryption of a selected batch of ciphertexts. Motivated by encrypted mempools, we study this capability through two con"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Batch decryption allows an authority to release a short key that enables public decryption of a selected batch of ciphertexts. Motivated by encrypted mempools, we study this capability through two constructions with different authorization semantics and assumptions. First, we provide a simple and compact epochless construction in an RSA group based on Fiat's Batch RSA [CRYPTO'89]. Its batch-decryption hint is just one group element, and its keys and ciphertexts have size independent of the batch size, with no batch bound fixed at setup. We prove adaptive security under the strong RSA assumption in the random-oracle model. The scheme permits repeated releases for overlapping batches, with each release authorizing decryption of the selected ciphertexts. Second, we give an adaptively secure generic construction of identity-based encryption with batch decryption in the epoch-based model, which permits at most one batch-key query for the challenge epoch. The construction combines deferred encryption via garbled circuits, non-inclusion secure registration-based encryption, and weak receiver non-committing IBE. We construct the latter primitive from ordinary IBE and pseudorandom functions, obtaining an instantiation of the epoch-based construction from the computational Diffie--Hellman assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2252) | 2026-09-28
