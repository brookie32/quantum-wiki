---
title: "HERMES: High-Performance Private Decoding for Large Language Models"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2532"
summary: "Privacy-preserving inference (PI) enables users to query large language models (LLMs) without revealing their prompts, but incurs substantial computation and communication overhead. Prior PI systems p"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

Privacy-preserving inference (PI) enables users to query large language models (LLMs) without revealing their prompts, but incurs substantial computation and communication overhead. Prior PI systems primarily optimize prefill and time to first token (TTFT). This suits applications that need only a single output token, yet most real-world use cases require multi-token responses. Such autoregressive workloads are dominated by time per output token (TPOT) instead. For the first time, we investigate generating full multi-token answers for real prompts under PI. We show that PI decode is hindered by two bottlenecks: (i) nonlinear kernels that require many interactive communication rounds, and (ii) attention protocols that underutilize ciphertext capacity and repeatedly re-encrypt or transmit the growing key and value (KV) cache. We present HERMES, a PI system optimized for LLM decoding. HERMES replaces high-round nonlinear protocols with compute- and bandwidth-intensive alternatives that require fewer communication rounds. It also introduces a novel matrix-multiplication protocol based on homomorphic encryption that keeps the KV cache encrypted on the server and uses grouped-query attention (GQA) to improve ciphertext utilization. On Llama 3.1 8B Instruct, across the network conditions and prompts used in our evaluation, HERMES lowers TPOT by up to 2.7× and total PI latency by up to 2.1×.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2532) | 2026-10-18
