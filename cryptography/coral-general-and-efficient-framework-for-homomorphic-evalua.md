---
title: "Coral: General and Efficient Framework for Homomorphic Evaluation of Symmetric Ciphers"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1917"
summary: "Fully homomorphic encryption (FHE) enables computation directly on encrypted data, but encrypting data under FHE imposes client-side computational costs and produces large ciphertexts. Transciphering "
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Fully homomorphic encryption (FHE) enables computation directly on encrypted data, but encrypting data under FHE imposes client-side computational costs and produces large ciphertexts. Transciphering addresses these costs by allowing the client to upload symmetric ciphertexts while the server homomorphically evaluates symmetric decryption to obtain FHE ciphertexts. However, transciphering itself can become a performance bottleneck, and a general framework for efficiently supporting structurally diverse symmetric ciphers is still lacking. To fill this gap, we present Coral, a general and efficient transciphering framework built on TFHE. Rather than mapping an entire decryption circuit to a uniform evaluation strategy, Coral decomposes it at operation boundaries and provides optimized procedures for four recurring computational modules: linear Boolean operations, sparse low-degree Boolean functions, modular additions, and small-domain substitutions. These procedures share compatible ciphertext interfaces, allowing them to be reused and composed across different ciphers. Together, these optimized procedures enable Coral to achieve high efficiency without sacrificing generality. We instantiate Coral for Trivium, AES, ChaCha20, and ZUC, covering both individual and combined nonlinear structures. Compared with the corresponding baselines, our implementations achieve speedups of up to 4.055imes for ZUC under single-threaded execution and up to 5.517imes for ChaCha20 under fully parallel execution.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1917) | 2026-09-08
