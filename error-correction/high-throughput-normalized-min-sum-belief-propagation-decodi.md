---
title: "High-Throughput Normalized Min-Sum Belief Propagation Decoding for Quantum LDPC Codes with Near-Memory Processing"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27901"
summary: "arXiv:2608.27901v1 Announce Type: new Abstract: Real-time quantum error correction requires classical decoders to process growing syndrome workloads with low and predictable latency. For quantum low-d"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27901v1 Announce Type: new Abstract: Real-time quantum error correction requires classical decoders to process growing syndrome workloads with low and predictable latency. For quantum low-density parity-check (qLDPC) codes, iterative belief propagation (BP) repeatedly updates messages over sparse Tanner graphs, creating substantial memory-access and data-movement demands. We map normalized Min-Sum BP decoding of the [[144,12,12]] Bivariate Bicycle qLDPC code onto a DPU-based Processing-in-Memory (PIM) architecture. Within each DPU, 11 tasklets cooperatively decode one syndrome, while multiple DPUs process independent syndrome instances in parallel. Using uPIMulator and a data-qubit Pauli error model with ideal syndrome measurements, we compare throughput, per-syndrome processing time, logical error rate (LER), and single-syndrome tail latency against a 16-logical-CPU baseline. At a component-wise physical error probability of p=0.001 and one BP iteration, the projected aggregate kernel throughput of 2,560 DPUs reaches 1.071 x 10^7 decodes/s, compared with 1.22 x 10^6 decodes/s for the CPU, an 8.8x improvement. From two iterations onward, the measured LER remains below the physical error probability for every evaluated value of p. For one to five iterations, the maximum sampled serialized X+Z DPU compute latency remains below the 1 ms decoder-side reference for trapped-ion QEC, reaching approximately 0.873 ms at five iterations. These results show that near-memory processing can provide high aggregate throughput and sub-millisecond compute latency for qLDPC BP decoding under the evaluated conditions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27901) | 2026-08-31
