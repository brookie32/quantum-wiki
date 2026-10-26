---
title: "Trident: Efficient Load Verification for Yoked Surface Codes using a Three-Level Memory Hierarchy"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32152"
summary: "arXiv:2610.32152v1 Announce Type: new Abstract: Fault-Tolerant Quantum Computers (FTQCs) commonly use the surface code to encode program qubits as error-corrected logical qubits. Unfortunately, the su"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32152v1 Announce Type: new Abstract: Fault-Tolerant Quantum Computers (FTQCs) commonly use the surface code to encode program qubits as error-corrected logical qubits. Unfortunately, the surface code has a poor encoding rate, so recent work has proposed Yoked Surface Codes (YSCs), which concatenate the surface code with a high-rate quantum code. The surface code qubits in YSCs are protected by the checks, or yokes, of the high-rate code. YSCs have 1D and 2D variants, which are 1.8imes and 4.5imes more efficient than the surface code, respectively. Modern FTQC architectures use a two-level hierarchy: surface codes perform logical operations (compute) while 2D YSCs store idle program qubits (memory). To load a qubit from memory, the FTQC first performs retrieval, which logically moves a program qubit from a 2D YSC into a surface code (8 cycles). However, retrieval is not fault-tolerant, so the FTQC must verify the load by measuring all the yokes of the 2D YSC (178 cycles). As verification dominates memory access latency, eliminating it can provide a speedup of 5.7imes. Our goal is to reduce the verification overhead of 2D YSCs while retaining their storage efficiency. We exploit the fact that 1D YSCs, though less storage-efficient, incur negligible verification latency. We propose Trident, which expands the two-level hierarchy into a three-level hierarchy by adding a small intermediate level containing a 1D YSC (L1). If most loads hit L1 rather than L2 (2D YSC tier), it can significantly reduce verification overhead. We present two variants: Trident-D (demand-driven) and Trident-P (prefetch-driven), which achieve speedups of 2.8imes and 4.2imes, respectively, while increasing the physical qubit cost of memory by only 4.9%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32152) | 2026-10-26
