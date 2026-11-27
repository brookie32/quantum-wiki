---
title: "FLoRA: LoRA Fine-Tuning for Language Models under Fully Homomorphic Encryption"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3033"
summary: "Deploying and fine-tuning Language Models (LMs) on cloud infrastructure introduces privacy risks when handling sensitive prompts and proprietary datasets. While Low-Rank Adaptation (LoRA) reduces fine"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Deploying and fine-tuning Language Models (LMs) on cloud infrastructure introduces privacy risks when handling sensitive prompts and proprietary datasets. While Low-Rank Adaptation (LoRA) reduces fine-tuning overhead, it requires processing data in plaintext, exposing sensitive data to curious cloud providers. To address these vulnerabilities, we introduce FLoRA, a privacy-preserving framework for encrypted LM fine-tuning and inference via Fully Homomorphic Encryption (FHE). FLoRA allows training low-rank adapters and performing inference entirely on encrypted data, guaranteeing data confidentiality against untrusted environments. We evaluate FLoRA by fine-tuning the SmolLM2-360M model on the SST-2 dataset, demonstrating stable performance and efficiency for privacy-preserving LM adaptation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3033) | 2026-11-25
