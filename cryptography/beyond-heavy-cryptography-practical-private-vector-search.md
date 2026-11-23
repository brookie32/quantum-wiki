---
title: "Beyond Heavy Cryptography: Practical Private Vector Search"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2974"
summary: "Driven by the explosion of AI applications, private vector search has recently gained widespread attention, but it still faces performance bottlenecks. Graph-based private search systems (Zhu et al., "
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Driven by the explosion of AI applications, private vector search has recently gained widespread attention, but it still faces performance bottlenecks. Graph-based private search systems (Zhu et al., OSDI 2025) suffer from multi-round communication latency, while IVF-based systems (Henzinger et al., SOSP 2023) incur recall degradation and heavy computational overhead. In this paper, we propose EHSearch, a single-round, high-throughput private vector search system on encrypted data. EHSearch introduces HGI, an index structure that distills the HNSW graph into fixed-size groups, preserving local navigability for high recall. To avoid heavy cryptographic primitives, EHSearch presents Compute-Free Encrypted Filtering, which couples binary quantization with block-scoped pigeonhole matching, reducing the server workload from dense encrypted arithmetic to lightweight exact lookups. Extensive evaluations across four real-world datasets demonstrate that EHSearch outperforms state-of-the-art private baselines by 2 to 5 orders of magnitude in throughput, and scales out-of-core to 1 billion vectors on a single SSD. Specifically, when achieving 90% Recall@10 on 1 million points, EHSearch answers a private vector search in 22.35ms P99 latency in LAN, and sustains 223.3ms P99 latency in WAN environments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2974) | 2026-11-21
