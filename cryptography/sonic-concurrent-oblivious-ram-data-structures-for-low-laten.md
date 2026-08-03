---
title: "SONIC: Concurrent Oblivious RAM & Data Structures for Low-Latency and High-Throughput"
date: "2026-08-02"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1577"
summary: "Relying solely on encryption for privacy-preserving computations is prone to leakage-abuse/access-pattern attacks. TEEs, while cost-effective, are also vulnerable to side-channel attacks. Oblivious pr"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Relying solely on encryption for privacy-preserving computations is prone to leakage-abuse/access-pattern attacks. TEEs, while cost-effective, are also vulnerable to side-channel attacks. Oblivious primitives, such as oblivious memory (ORAM) and data structures (ODS), are effective building blocks to mitigate these risks by concealing memory access patterns and side-channel information. Applications range from private contact discovery (Signal) to anonymous key transparency, encrypted email search, encrypted/oblivious databases, anonymous communication (Sparta/SP'25), private federated learning, LLM privacy (Compass/OSDI'25), and broader confidential computing efforts. Tree-based ORAMs (EnigMap (USENIX'23), GraphOS (PVLDB'23), Oblix (SP'18)) offer low latency but limited parallelism. Partition-based solutions like Snoopy (SOSP'21) shard data across subORAMs (which build oblivious hashtables on incoming requests, then linearly scan them), achieving high throughput by trading off latency, theoretically enabling linear scalability. In practice, Snoopy’s performance hinges on how quickly each subORAM can build the oblivious hashtable and complete its linear scan before exceeding latency targets, constraining server utilization and throughput. While supporting a TB-scale dataset with Snoopy is theoretically feasible, we estimate it would require 1000+ servers. In this work, we reconcile the fractured landscape between low-latency and high-throughput ORAM designs. We introduce SONIC: the first parallel/concurrent doubly-oblivious tree-based ORAM for TEEs. SONIC achieves 156K-3.3M req/s with a single server, tackling the core challenges of all tree-ORAM constructions: overcoming the sequential eviction bottleneck, enabling efficient batch evictions, and providing lock-free access/reshuffle/stash operations. SONIC achieves throughput 29-104imes higher than EnigMap, and 158-560imes higher than GraphOS, with lower latency. In the distributed, high-throughput setting, our SONIC-powered OMAP PMChain can replace Snoopy's subORAM, supporting higher throughput and 64imes larger datasets using the same hardware (reducing Snoopy's server requirements).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1577) | 2026-08-02
