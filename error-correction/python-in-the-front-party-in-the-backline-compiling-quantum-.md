---
title: "Python in the front, party in the Backline: compiling quantum workloads across CPUs, GPUs, and FPGAs"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.09270"
summary: "arXiv:2609.09270v1 Announce Type: new Abstract: Moving from quantum research and development to production-grade, fault-tolerant quantum workload execution remains one of the most significant challeng"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.09270v1 Announce Type: new Abstract: Moving from quantum research and development to production-grade, fault-tolerant quantum workload execution remains one of the most significant challenges facing quantum platform builders. While Python frameworks have enabled an easy entry point for quantum algorithm design, the low-latency requirements for real-time quantum error correction (QEC) demand performance that traditional interpreted environments cannot provide. FPGAs and ASICs play a central role at these layers, but their specialized programming models make development rigid and time-consuming. CPUs, GPUs, and other accelerators introduce a different challenge: as infrastructure becomes increasingly heterogeneous, programming across different devices and their associated abstractions becomes more complex. Allowing researchers to write workloads in high-level languages that map to low-latency execution across diverse distributed target platforms will enable the development of key infrastructure for utility-scale quantum systems. For this, we introduce extit{Backline}, a heterogeneous compilation and runtime framework built within PennyLane and Catalyst. Backline allows us to design and build quantum-classical workloads for high-performance and low-latency devices, with compilation directly from a Python interface through MLIR. We demonstrate the compilation and execution of several quantum workloads with low-latency data movement across a mix of CPUs, GPUs, and FPGAs, for both local and distributed remote hardware targets, all from a vendor-agnostic Python frontend. With an AMD VPK120 FPGA board as the controller, issuing each round from its hardware-handshake engine, we measured median steady-state round-trip latencies over RoCE v2 of 2.305~mus to an AMD Ryzen Threadripper PRO CPU and 4.5~mus to an AMD Instinct MI210 GPU across 10^6-1 rounds per path, demonstrating microsecond-scale synchronous co-processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.09270) | 2026-09-10
