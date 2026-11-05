---
title: "Perseus: A Full-Stack System for Homomorphic Model Inference"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2735"
summary: "Large Language Models (LLMs) have made it exceptionally convenient for users to send their private data to model providers, which process them in plaintext. Fully Homomorphic Encryption (FHE) promises"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Large Language Models (LLMs) have made it exceptionally convenient for users to send their private data to model providers, which process them in plaintext. Fully Homomorphic Encryption (FHE) promises to secure remote inference by computing directly on encrypted data, yet it has remained prohibitively slow. The effort to make it practical remains fragmented, with most existing frameworks being closed-source, which keeps progress from compounding. We present Perseus, a free and open Python software library that supports the full stack of encrypted model inference, from the cryptographic backend and data packing, to encrypted nonlinearities and end-to-end model execution. Perseus ships with built-in novel optimizations, one at each level of the stack: in-kernel regeneration of key-switching keys at the (i) backend level, a complex variant of Cachemir packing at the (ii) data level, and a state-of-the-art bootstrap placer that is both packing- and magnitude-aware at the (iii) model level. Perseus achieves state-of-the-art latency across multiple models and modalities, within 3% of the plaintext models' accuracy and perplexity. Remarkably, it is 3.96imes faster at single-token decoding than any other implementation on Llama-3-8B. We initiate, for the first time, a public speedrun on encrypted GPT-2, so that progress can compound.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2735) | 2026-11-03
