---
title: "QSimAdv: A Late-Bound, Vendor-Agnostic Architecture for High-Performance Quantum-Circuit Simulation"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16940"
summary: "arXiv:2608.16940v1 Announce Type: new Abstract: Portability in high-performance quantum-circuit simulation need not begin at the kernel. We present QSimAdv, which makes late binding, rather than a com"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.16940v1 Announce Type: new Abstract: Portability in high-performance quantum-circuit simulation need not begin at the kernel. We present QSimAdv, which makes late binding, rather than a common kernel, the basis of vendor independence. Representation, operator lowering, and data placement are bound only when their required inputs become available. Before full-state allocation, circuit, noise, and output inspection can route eligible generic sampled-count requests to a stabiliser tableau; explicitly requested representations remain fixed. For full-state execution, backend constraints shape fusion; an ordered fused operator binds to a native lowering only after its physical targets are known. A first-class logical-to-physical layout map records non-canonical order across local and rank-address bits, so the dispatcher moves nonlocal targets only on demand. GPU, CPU, and Message Passing Interface (MPI) backends share these semantics while retaining native execution paths. We realize this design on NVIDIA GH200 and AMD MI250X/EPYC systems across local and distributed execution. With matched complex 32-bit floating-point state storage, QSimAdv leads both Aer Hopper configurations at N=32 and Aer's HIP backend at four shared MI250X sizes from N=24 to 30. Strong scaling exposes platform dependence: on setonix, QSimAdv leads both GPU and CPU comparisons at every measured rank, achieving 3.4imes and 2.8imes speedups, respectively, from one to eight ranks; neither the GH200 path nor the CPU path speeds up at eight ranks. Weak scaling reaches 256 ranks with 2 TiB GPU and 1 TiB CPU states. Together, these results support that portability can reside above the kernel boundary while execution remains native and extends across distributed memory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16940) | 2026-08-19
