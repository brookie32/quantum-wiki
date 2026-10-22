---
title: "DISCO*: DIstributed and SCalable Oblivious Joins and Oblivious Primitives"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2572"
summary: "Trusted Execution Environments (TEEs) let clients outsource computation to untrusted clouds, but they remain vulnerable to side-channel and leakage-abuse attacks. Recent work closes this gap by combin"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

Trusted Execution Environments (TEEs) let clients outsource computation to untrusted clouds, but they remain vulnerable to side-channel and leakage-abuse attacks. Recent work closes this gap by combining hardware enclaves with oblivious computation, which offers strong security guarantees yet struggles to meet the performance and scalability demands of real-world deployments. In this work, we present DISCO, the first scalable, distributed, and fully oblivious database system that seamlessly combines hardware enclaves with cutting-edge oblivious primitives and novel optimizations that significantly reduce inter-server communication overheads. What distinguishes DISCO from prior work is a suite of distributed frameworks that unlock parallel computation and fundamentally shift the design paradigm of distributed oblivious systems, enabling practical deployment at scales that were unattainable with previous solutions. We provide a thorough evaluation of the performance of our system on both synthetic and real-world datasets. Our evaluation demonstrates that our design significantly reduces the gap between theory and practice, achieving 88× speedup over Jodes and 180× over SODA on non-foreign key joins with N = 2²⁵ elements. Most importantly, we report, for the first time, results for computations at the terabyte scale.



## Related
- [[sonic-concurrent-oblivious-ram-data-structures-for-low-laten|SONIC: Concurrent Oblivious RAM & Data Structures for Low-Latency and High-Throughput]]
- [[toward-secure-compilation-leakage-detection-for-masked-imple|Toward Secure Compilation: Leakage Detection for Masked Implementations in Jasmin]]
- [[charrm---characterizing-hardware-leakage-in-the-robust-rando|CHARRM - Characterizing Hardware Leakage in the Robust Random Probing Model]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2572) | 2026-10-20
