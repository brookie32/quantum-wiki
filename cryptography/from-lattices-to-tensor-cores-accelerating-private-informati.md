---
title: "From Lattices to Tensor Cores: Accelerating Private Information Retrieval"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1816"
summary: "This work introduces SandwichPIR, the first single-server PIR protocol that implements the overwhelming majority of the server computation as dense 8-bit integer matrix multiplications on GPU tensor c"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

This work introduces SandwichPIR, the first single-server PIR protocol that implements the overwhelming majority of the server computation as dense 8-bit integer matrix multiplications on GPU tensor cores and requires no offline communication. For a 4 GB database with 32 KB records, SandwichPIR answers a query in 8.2 ms and communicates 688 KB of data. This amounts to a server throughput of 488 GB/s and is 88imes faster than the best CPU-based protocol that does not rely on offline communication. The performance of SandwichPIR shines when processing a batch of queries from many independent clients. This moves the server from a memory-bandwidth-bound regime into a compute-bound regime. A single Nvidia L40S GPU can process a batch of 128 queries to the same 4 GB database in 21.0 ms. This gives an amortized per-query processing time of 0.16 ms and an effective throughput of roughly 24 TB/s. This is 50imes higher than the single-query throughput. With a fleet of 8 GPUs, SandwichPIR can process a batch of 128 queries to a 256 GB database in 119 ms and achieves an effective throughput of nearly 270 TB/s. Finally, we show how to use SandwichPIR to enable private access to (text-only) English Wikipedia (8 GB compressed). Retrieving an article (up to 128 KB) requires 768 KB of client-server communication, with an estimated total end-to-end latency under 200 ms over a broadband network connection. By processing 64 queries at a time, a single GPU can handle over 2,500 queries per second (with a computational cost of $0.20 per million queries based on current AWS pricing).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1816) | 2026-08-27
