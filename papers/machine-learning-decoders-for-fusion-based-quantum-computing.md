---
title: "Machine-learning decoders for fusion-based quantum computing in real time"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13630"
summary: "arXiv:2611.13630v1 Announce Type: new Abstract: Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low latency, and scalability to large numbers of physical qubits"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13630v1 Announce Type: new Abstract: Fault-tolerant quantum computation requires decoders that combine accuracy, throughput, low latency, and scalability to large numbers of physical qubits. In photonic fusion-based architectures, erasures from photon loss and probabilistic fusion measurements are a dominant error mechanism, motivating decoders that remain accurate at high erasure rates. We introduce PRISM, a transformer-based machine-learning decoder designed to exploit the known locations of erasures in protocols subject to both Pauli and erasure errors. We benchmark PRISM across a wide range of fault-tolerant protocols based on surface codes, color codes, and quantum low-density parity-check codes, with distances up to 24. Across these benchmarks, PRISM matches the logical error rates of integer-programming-based decoders while being significantly faster, including at error rates up to 50% of threshold. We further optimize the decoder and its real-time hardware implementation to reduce latency while maintaining accuracy. Our optimized implementation on an AMD VP1902 FPGA can decode logical blocks of distance 8 in both space and time, demonstrating a latency of 6.59 microseconds and an amortized decoding time of 1.56 microseconds per logical block is possible. These results show that machine-learning decoding can provide accurate, low-latency inference for erasure-dominated fault-tolerant quantum architectures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13630) | 2026-11-11
