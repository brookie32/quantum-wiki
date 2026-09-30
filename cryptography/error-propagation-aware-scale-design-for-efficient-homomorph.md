---
title: "Error Propagation-Aware Scale Design for Efficient Homomorphic Encryption-Based LLM Inference"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2242"
summary: "Homomorphic encryption (HE) enables privacy-preserving inference by allowing neural networks to operate directly on encrypted data, but its computational cost remains a major obstacle to deploying lar"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Homomorphic encryption (HE) enables privacy-preserving inference by allowing neural networks to operate directly on encrypted data, but its computational cost remains a major obstacle to deploying large language models in practice. In particular, CKKS-based inference consumes ciphertext modulus through homomorphic multiplications and requires costly bootstrapping when the available modulus is exhausted. In this work, we propose an error-propagation-aware scale design for efficient CKKS-based privacy-preserving LLM inference. We characterize the numerical errors introduced by individual homomorphic operations and analyze how they propagate through subsequent Transformer computations. Based on this analysis, we quantify the contribution of each local error to the final inference error and determine the precision required for individual operations. We then allocate operation-wise scales and modulus levels accordingly, avoiding unnecessarily conservative precision while maintaining the target inference accuracy. As a result, more computation can be performed within a given modulus chain, reducing the frequency of costly bootstrapping operations and improving overall inference efficiency. Compared with THOR, our method reduces modulus consumption by 30.0% and the number of bootstrapping operations by 83.6% for the standard Transformer. For the HE-friendly Transformer, our method reduces modulus consumption by 33.6% and the number of bootstrapping operations by 80% compared with PowerFormer.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2242) | 2026-09-28
