---
title: "ROSETTA: Efficient and Accurate Privacy-Preserving LLM Decoding via Hybrid CKKS/TFHE Evaluation"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2047"
summary: "Generative large language models (LLMs) have achieved state-of-the-art performance on many real-world tasks such as code generation and question answering. These models predominantly rely on an autore"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Generative large language models (LLMs) have achieved state-of-the-art performance on many real-world tasks such as code generation and question answering. These models predominantly rely on an autoregressive decoding strategy that generates output tokens sequentially. However, their pervasive deployment raises serious privacy concerns, motivating private inference frameworks based on fully homomorphic encryption (FHE). A major limitation of existing FHE frameworks is their inefficiency in evaluating nonlinear operations, which incur substantial overhead and dominate the decode stage. In this paper, we propose ROSETTA, a hybrid CKKS/TFHE framework that overcomes this limitation. We first observe that nonlinear operations in the decode stage exhibit heterogeneous workload patterns, which can be handled effectively via a hybrid approach. We then realize this with two key contributions: 1) an adaptive segmented lookup-table protocol based on TFHE that enables efficient and accurate evaluation of nonlinear operations; and 2) a scheme-aware operator-selection framework that automatically assigns each nonlinear operator to CKKS or TFHE to minimize end-to-end decoding latency. We demonstrate that ROSETTA achieves up to 4.8x Softmax speedup and 1.5--2.1x end-to-end speedup over the SOTA framework CacheMir.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2047) | 2026-09-15
