---
title: "Zero-G: A Pre-Decoder-Aware Decoder for Quantum Error Correction"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.02030"
summary: "arXiv:2608.02030v1 Announce Type: new Abstract: Fault-tolerant quantum computing requires classical decoders that keep pace with the underlying hardware, translating syndrome measurements into correct"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.02030v1 Announce Type: new Abstract: Fault-tolerant quantum computing requires classical decoders that keep pace with the underlying hardware, translating syndrome measurements into corrections fast enough to avoid an exponential backlog. To meet this real-time constraint, pre-decoders have emerged as part of a hierarchical decoding approach to resolve simple, local errors before passing a sparser residual syndrome to a strong decoder. While pre-decoding should, in theory, speed up the strong decoder, in practice, the speedup is only marginal, since existing strong decoders are designed to decode dense syndromes and cannot exploit the sparsity provided by pre-decoders. To address this, we present Zero-G, a strong decoder designed for use alongside pre-decoders. As a stochastic approximate minimum-weight perfect matching (MWPM) decoder, Zero-G exploits sparse residual syndromes, dynamically trading latency for accuracy rather than relying on an all-or-nothing runtime-accuracy trade-off. By decoupling hardware control from the decoding core itself, we enable heterogeneous deployment across both FPGAs and CPUs without maintaining separate implementations. Zero-G achieves a 10imes latency improvement over existing strong decoders at matching accuracy, with worst-case sub-350ns decoding at code distances up to d=15, while scaling to 640 logical qubits on a single 128-core CPU and 32 logical qubits on a single AMD Versal V80 FPGA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.02030) | 2026-08-04
