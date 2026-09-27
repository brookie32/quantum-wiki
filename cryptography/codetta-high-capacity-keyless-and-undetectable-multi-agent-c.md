---
title: "Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2218"
summary: "Multi-agent systems built on large language models (LLMs) are increasingly being deployed in high-stakes settings such as finance, healthcare, and software engineering, where agents coordinate through"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Multi-agent systems built on large language models (LLMs) are increasingly being deployed in high-stakes settings such as finance, healthcare, and software engineering, where agents coordinate through natural-language messages. These same communication channels, however, can also enable colluding agents to exfiltrate confidential information or coordinate unauthorized actions. Steganography makes such behavior particularly difficult to detect by hiding covert communication within outputs that appear ordinary to an auditor reading the transcript. Existing provably undetectable LLM steganography protocols, however, are not suited to realistic deployments. High-capacity schemes typically assume a symmetric setting where the receiver can reproduce the sender's output distribution. The state-of-the-art practical protocol for asymmetric agents has very low capacity. Additionally, most existing approaches rely on a pre-shared secret key. In this paper, we make the systematic threat of undetectable agent collusion concrete by proposing Codetta, a high-capacity steganographic protocol for independently deployed agents under realistic asymmetric settings. Codetta combines a shared public model for estimating the communication channel, a sampling mechanism that preserves the sender's output distribution, and an adaptive error-correcting code for high-capacity communication. It further removes the need for a pre-shared secret key through a steganographic key-exchange protocol, enabling independently deployed agents to establish a shared key while keeping their communication transcript computationally indistinguishable from ordinary model outputs. Across three agent workloads and three sender models, Codetta achieves up to 94imes the capacity of the state-of-the-art asymmetric protocol. Its key exchange establishes a shared key using approximately 80k visible tokens, with an empirically certified failure probability of at most 4.1imes10^{-3} across all three workloads. These results show that effectively undetectable collusion is becoming feasible even between independently deployed agents, and we suggest that auditing mechanisms must be amended with complementary techniques beyond simply inspecting agents' communication transcripts.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2218) | 2026-09-25
