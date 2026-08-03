---
title: "OpenLLM: Modular and Scalable zkSNARKs for Verifiable LLM  Inference"
date: "2026-08-02"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1578"
summary: "Large language model (LLM) is increasingly deployed as a remote service, where users rely on third-party servers to perform computation. However, such settings introduce critical integrity concerns, a"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Large language model (LLM) is increasingly deployed as a remote service, where users rely on third-party servers to perform computation. However, such settings introduce critical integrity concerns, as an untrusted server may deviate from the prescribed computation, skip expensive operations, or return incorrect results, while users lack practical approaches to verify execution correctness. Ensuring the correctness of LLM inference under untrusted execution remains a fundamental challenge. Zero-knowledge proofs (ZKPs) provide a principled approach verifying computation correctness, but applying them to LLM inference remains challenging. Modern LLMs involve a large number of non-linear operations and require modeling real-valued computation in finite fields, introducing substantial computational and memory overhead and potential loss of numerical precision. Moreover, the large scale of LLMs makes end-to-end verification difficult to scale, limiting the practicality of existing approaches. This paper presents OpenLLM, an efficient and modular system for verifiable LLM inference. Our key idea is to decompose large-scale LLM inference into a set of reusable atomic operators, each equipped with efficient ZKP protocols, enabling scalable verification at the operator level. Based on this abstraction, we design succinct non-interactive zero-knowledge proof constructions for representative non-linear functions, which can be composed into end-to-end inference pipelines independent of model architectures. We further evaluate OpenLLM across operator-level performance, end-to-end inference, layer-wise scaling, larger models, and approximation accuracy. The results show that OpenLLM achieves smaller proof sizes, lower verification cost, and improved numerical fidelity while scaling from individual operators to full-model inference. Compared with state-of-the-art interactive protocols, OpenLLM eliminates communication overhead through a fully non-interactive design while maintaining competitive efficiency. Building on this operator-level efficiency, it further enables a scalable and modular framework for end-to-end verifiable LLM inference, outperforming prior end-to-end approaches.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1578) | 2026-08-02
