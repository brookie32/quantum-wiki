---
title: "Optimizing HQC with Enhanced Parallel Binary Polynomial Multiplication on GPUs"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2538"
summary: "Graphics processing units (GPUs) are widely employed as accelerators in modern servers to handle key-establishment requests in bulk. Such deployments require the GPU implementation to sustain high thr"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Graphics processing units (GPUs) are widely employed as accelerators in modern servers to handle key-establishment requests in bulk. Such deployments require the GPU implementation to sustain high throughput while keeping each request within its latency bound. In this work, we present a high-performance, end-to-end GPU implementation of Hamming Quasi-Cyclic (HQC), a code-based key encapsulation mechanism (KEM). We propose two novel techniques to accelerate the dominant cost of HQC, which is binary polynomial multiplication over Galois Field GF(2). The first is a parallelization of the Frobenius additive fast Fourier transform (FAFFT), and the second is a mapping of the cyclic product, viewed as a Toeplitz matrix–vector product, onto one-bit integer (INT1) tensor cores. We further explore the design space of these multipliers, measuring them directly on the GPU to derive the best combination for the architecture. We further propose a GPU-resident computation strategy that keeps the entire KEM on the GPU, thereby reducing costly memory traffic. Beyond multiplication, we introduce warp-level parallelization strategies to accelerate the remaining stages, hashing, Reed–Muller/Reed–Solomon (RM/RS) coding, and fixed-weight sampling, which become the performance bottleneck once multiplication is optimized. By varying the mapping of KEM instances to GPU threads, we derive five variants spanning the trade-off between throughput and latency and organize them into a thread-to-KEM mapping taxonomy. On an RTX 4090, the Coarse-Grained (CG) variant maximizes batch throughput. Our multiplier reaches 3,828k polymul/s for standalone multiplication, about 2.9× the latest GPU HQC implementation HIGH, and for the full KEM the CG variant achieves 1.56×, 1.55×, and 2.03× higher end-to-end throughput than HIGH for keygen, encaps, and decaps. For single-shot latency the tensor-core-based BMMAw variant achieves a latency as low as 254 µs. The proposed warp-parallel FGmw variant still attains a latency of 354 µs, demonstrating that our approach remains effective on GPU architectures lacking INT1 tensor-core support. All five variants are further evaluated on an RTX 3090 and an embedded Jetson AGX Orin to confirm cross-platform portability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2538) | 2026-10-19
