---
title: "DKG: A Dual-Layer Knowledge Graph and LLM Co-Driven Framework for Fully Automated Side-Channel Analysis of Cryptosystems"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2838"
summary: "Cryptographic algorithms underpin billions of devices, from payment smartcards to smartphone secure enclaves and industrial controllers. Yet their physical implementations risk leaking secret keys. No"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Cryptographic algorithms underpin billions of devices, from payment smartcards to smartphone secure enclaves and industrial controllers. Yet their physical implementations risk leaking secret keys. Non-profiled side-channel analysis (SCA) evaluates whether such leakage enables key recovery, but executing it end-to-end remains expert-intensive. Large language model (LLM) agents now automate complex workflows across many domains, yet reliable key recovery requires specialized SCA knowledge that must be extracted and organized from scattered technical literature. In this paper, we propose DKG, a dual-layer knowledge graph and LLM co-driven key-recovery agent framework. We introduce the first graph schema designed specifically for SCA: an upper layer of configuration components and a lower layer of diagnostic strategies, joined by cross-layer relationships. An LLM-driven three-step extraction pipeline (Locate & Rewrite, Triple Extraction, and Knowledge Fusion) builds the graph from raw technical documents without manual annotation, and at runtime the retrieved knowledge drives a closed-loop autonomous attack workflow. Built from a corpus of 166 technical documents, the graph contains 1,334 entities and 1,813 relationships. On eight datasets covering AES, DES, and SM4 across smartcards, FPGAs, and MCUs, DKG with DeepSeek-V3.2 achieves a 97.5% end-to-end key-recovery success rate. By comparison, ReAct-RAG, a text-retrieval-augmented agent, achieves only 68.8%. Across the open-weights backbones DeepSeek-V3.2, GLM-5, and Qwen3.5, DKG achieves an average success rate of 93.3%. To the best of our knowledge, DKG is the first framework to achieve consistent end-to-end automated key recovery across diverse implementations. Its automated pipeline lets the graph grow with new literature, and its dual-layer organization provides a basis for extending DKG to additional SCA techniques.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2838) | 2026-11-09
