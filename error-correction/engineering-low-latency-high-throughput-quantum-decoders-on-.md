---
title: "Engineering Low-Latency, High-Throughput Quantum Decoders on NVIDIA GPUs"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28867"
summary: "arXiv:2610.28867v1 Announce Type: cross Abstract: We design and optimize a quantum error correction (QEC) decoder for NVIDIA GPUs, combining Relay belief propagation, a state-of-the-art message-passin"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.28867v1 Announce Type: cross Abstract: We design and optimize a quantum error correction (QEC) decoder for NVIDIA GPUs, combining Relay belief propagation, a state-of-the-art message-passing algorithm, with order-zero ordered statistics post-processing. Our implementation uses CUDA Graphs to control GPU execution, stops updates for converged samples, and collects unresolved samples in queues for post-processing. We optimize sparse traversal through coalesced message accesses, prefetching, and register reuse, and accelerate binary post-processing with warp-level collectives. In addition, mixed FP16-FP32 arithmetic and INT8 quantization reduce message storage and traffic while retaining accuracy using accumulators at higher precision. We evaluate surface, hypergraph product, and bivariate bicycle code workloads on NVIDIA A100 and GH200 data-center GPUs and a commodity RTX 5080. On the bivariate bicycle code at error probability 0.003, INT8 halves amortized decoding time relative to independently tuned FP32 with a negligible logical error rate increase on RTX 5080. With independent syndrome batches submitted back-to-back to concurrent decoder instances, RTX 5080 delivers 91% of GH200's highest measured throughput with an 8.9x shorter median submission-to-correction latency. The combination of performance optimization, mixed precision, INT8 quantization, and concurrent decoder instances opens a path toward QEC decoder clusters built from commodity GPUs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28867) | 2026-10-22
