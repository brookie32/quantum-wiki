---
title: "GPU-Based Parallel BP Decoding for Quantum LDPC Memory"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.13879"
summary: "arXiv:2610.13879v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) decoding requires reliable corrections and low latency over long syndrome histories. We extend BP-SF, an oscill"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.13879v1 Announce Type: new Abstract: Quantum low-density parity-check (qLDPC) decoding requires reliable corrections and low latency over long syndrome histories. We extend BP-SF, an oscillation-guided belief-propagation (BP) decoder with independent syndrome-flip trials, by introducing windowed and streaming operations. Our CUDA implementation combines disordered-memory retries, sliding windows, correlation-aware graphs, and layered scheduling. Circuit-level simulations test fixed-basis memory and complete logical Pauli-frame recovery. On the [[144,12,12]] bivariate bicycle code at physical error rate p = 0.002, parallel BP-SF reduces 99.9th-percentile call latency by a factor of 13.15 relative to an eight-chain Relay-BP GPU baseline on 100,000 matched samples for which every tested method's initial BP stage fails within 80 iterations. Windowed BP-SF maintains a flat logical error rate and nearly constant per-round compute time through 512 rounds, reaching a 17.1-fold speedup over monolithic decoding. In 512-round full-frame streaming decoding with 2.97-ms syndrome arrivals, layered BP-SF on a transformed joint graph with 20 retries reduces 99.9th-percentile correction-release age from 166.29 to 36.25 ms relative to the joint graph with flooding updates and 100 retries. These results connect parallel BP post-processing to lower decoding costs and earlier correction release in streaming quantum memory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.13879) | 2026-10-12
