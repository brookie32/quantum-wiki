---
title: "Weighted Batch Threshold Encryption with Efficient DKG"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2053"
summary: "Batch threshold encryption allows a committee to decrypt a selected batch of ciphertexts using one short pre-decryption key per party, while ciphertexts outside the batch remain private. This makes ba"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Batch threshold encryption allows a committee to decrypt a selected batch of ciphertexts using one short pre-decryption key per party, while ciphertexts outside the batch remain private. This makes batch threshold encryption attractive for building encrypted mempools for blockchains, where validators reveal transactions selected for a block while pending transactions remain private. However, in proof-of-stake systems like Solana or Ethereum, authorization depends on each validator's stake, which motivates a weighted version of batch threshold encryption. Naive approaches to weighting existing batch threshold encryption schemes lead to communication costs proportional to the weight assigned to each party. Existing schemes that avoid this cost either associate every ciphertext with a batch label or an encryption-time index. We present the first weighted batch threshold encryption schemes that require neither batch/epoch labels nor encryption-time ciphertext indices, while keeping each party's communication independent of its weight. We obtain two constructions by virtualizing prior schemes: the BTX construction of Agarwal et al. and the partial-fraction construction of Boneh et al. In both schemes' decryption procedures, each party communicates a single group element for an entire batch, regardless of its assigned weight. We prove correctness, robustness, and security under weighted variants of the original schemes' assumptions, and analyze the assumptions in generic bilinear groups. For the BTX-based construction, we also give a specialized distributed key generation protocol that avoids the general purpose MPC-based setup required by the previous state-of-the-art schemes. Finally, we implement our schemes to demonstrate their practical performance at parameter sizes relevant to blockchains.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2053) | 2026-09-15
