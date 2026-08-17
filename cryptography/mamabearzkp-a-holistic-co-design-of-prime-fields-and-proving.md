---
title: "MamaBearZKP: A Holistic Co-design of Prime Fields and Proving Stacks for High-Throughput ZKP on Modern CPUs"
date: "2026-08-15"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1698"
summary: "Sum-check and Fast Fourier Transforms (FFTs) dominate the computational cost of modern zero-knowledge proving systems, such as HyperPlonk (Eurocrypt 2023) and FRI-based schemes like DeepFold (USENIX S"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

Sum-check and Fast Fourier Transforms (FFTs) dominate the computational cost of modern zero-knowledge proving systems, such as HyperPlonk (Eurocrypt 2023) and FRI-based schemes like DeepFold (USENIX Security 2025). Despite numerous optimizations, existing efforts remain fragmented across algorithmic, protocol, and implementation layers, leaving significant CPU performance potential untapped. We present MamaBearZKP, a co-designed framework that bridges these layers to enable high-throughput ZK proving on modern CPUs. At its core, MamaBearZKP leverages MamaBear, a 49-bit prime field (p = 2^{49} - 2^{34} + 1), and introduces a systematic vectorization framework specifically tailored for the AVX-512IFMA execution model. By treating field arithmetic, protocol structure, and low-level hardware primitives as a unified optimization target, MamaBearZKP achieves unprecedented efficiency. We instantiate our framework in a HyperPlonk-DeepFold prover and obtain single-thread speedups of up to 42imes, 33imes, 15imes, 21imes, and 21imes for ZeroCheck, ProductCheck, DeepFold Commit, DeepFold Open, and end-to-end proof generation, respectively, compared to a Goldilocks-based baseline on the same platform. With 8-thread execution, the corresponding speedups increase to as much as 64imes, 47imes, 81imes, 45imes, and 45imes. Across our end-to-end evaluations, MamaBearZKP also achieves up to 18imes single-thread speedup over Plonky3, which already uses an AVX-512 BabyBear backend. Rather than resulting from isolated improvements, these gains arise from a synergistic cascading effect: the 49-bit field’s headroom enables efficient lazy reduction, which paves the way for high-performance fused fold-and-evaluate kernels. The efficiency of these kernels facilitates a unified stay-packed dataflow throughout the HyperPlonk and DeepFold stacks; it is precisely this end-to-end dataflow that materializes the hardware throughput of AVX-512IFMA into realized performance gains.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1698) | 2026-08-15
