---
title: "The Distributed Producer-Consumer Model Is All You Need: A Compiler for Asynchronous BFT"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2598"
summary: "Building an Asynchronous Byzantine Fault Tolerant (BFT) protocol requires establishing payload availability with total order despite Byzantine faults and arbitrarily delayed messages. Although many BF"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Building an Asynchronous Byzantine Fault Tolerant (BFT) protocol requires establishing payload availability with total order despite Byzantine faults and arbitrarily delayed messages. Although many BFT systems separate payload dissemination from agreement, they often couple their composition to protocol-specific selection or scheduling mechanisms. We present the Distributed Producer-Consumer Model (DPCM), an event-driven abstraction that separates payload-specific certified availability from payload-oblivious binary finalization. We prove that DPCM compiles any producer–consumer pair satisfying interfaces specified herein into an asynchronous BFT object log. DPCM batch-finalizes certified heights, deterministically refining failed batches until each height yields a normal or evidence-backed dummy entry. We instantiate DPCM as Octopus, which combines parallel consistent broadcast producers with batched asynchronous binary agreement (ABA). To achieve performance advantages, Octopus lets producers certify blocks without waiting for consumer decisions and keeps payload recovery off the agreement path. One ABA optimistically finalizes multiple consecutive producer columns, while failures trigger parallel row-wise refinement with logarithmic bisection depth. Across an eight-region WAN with nin{8,16,32} and 2200-transaction blocks, Octopus remains within 6.5% of Dumbo-NG's (ACM CCS'22) fault-free throughput. With the maximum tested number of silent faulty parties, it outperforms Dumbo-NG by 25.9% and 18.7% at n=8 and n=16, respectively, and remains within 1% at n=32. At n=16 and n=32, Dumbo-NG's latency is 1.9--2.5imes that of Octopus. Across all evaluated settings, Octopus achieves 2.9--16.8imes the throughput of Alea-BFT (USENIX NSDI'24), whose latency is 2.4--15.2imes that of Octopus.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2598) | 2026-10-22
