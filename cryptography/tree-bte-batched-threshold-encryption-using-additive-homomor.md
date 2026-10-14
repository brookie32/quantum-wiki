---
title: "Tree-BTE: Batched Threshold Encryption using Additive Homomorphism"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2463"
summary: "Batched threshold encryption (BTE) enables a committee of servers to jointly decrypt any chosen subset of ciphertexts from a large pool, while all remaining ciphertexts stay private. BTE is a key buil"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Batched threshold encryption (BTE) enables a committee of servers to jointly decrypt any chosen subset of ciphertexts from a large pool, while all remaining ciphertexts stay private. BTE is a key building block for encrypted mempools, where transactions are encrypted until block inclusion to mitigate maximal extractable value (MEV). We give a new tree-based BTE construction from two simple building blocks which support additive homomorphism: a symmetric-key encryption scheme that is homomorphic over key and message space, and a thresholdizable public-key encryption scheme that is homomorphic over message space. These building blocks can be instantiated under a wide variety of assumptions including DDH, DCR, LWR and even LWE for post-quantum security. In our scheme, each ciphertext is associated with an index from an appropriate index space. We implement the DDH-based instantiation. Given an aggregated batch of 1,000 messages over a small 1024 sized index space, each server performs about 41~ms of single-thread computation, including a 100-of-300 threshold decryption. We also partially implement an RLWE-based post-quantum instantiation over a (2^{128}) sized index space for negligible collision probability among indices. A batch of 1024 messages uses approximately 0.89 MB per ciphertext and 20 seconds of single-thread decryption per server.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2463) | 2026-10-13
