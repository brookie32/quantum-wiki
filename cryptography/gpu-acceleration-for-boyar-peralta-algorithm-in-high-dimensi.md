---
title: "GPU Acceleration for Boyar-Peralta Algorithm in High Dimensional Linear Layers"
date: "2026-10-17"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2520"
summary: "The design of lightweight cryptographic schemes necessitates efficient circuit implementations of linear layers. A commonly used metric for evaluating circuit efficiency is the number of XOR gates req"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The design of lightweight cryptographic schemes necessitates efficient circuit implementations of linear layers. A commonly used metric for evaluating circuit efficiency is the number of XOR gates required. For a given linear transformation over mathbb F_2, finding its circuit implementation with the minimum number of XOR gates is referred to as the Shortest Linear Program (SLP) problem. As a prominent heuristic, the Boyar-Peralta (BP) algorithm provides competitive results, and numerous subsequent studies have introduced further optimizations. However, the inefficient implementations of the BP-like algorithms significantly limit their applicability to high-dimensional and dense matrices, and effective solutions to these performance bottlenecks remain scarce. In this paper, we address the performance bottlenecks of the BP algorithm and its variants (e.g., A1, A2 and BP-LSL) both theoretically and practically. We introduce the meet-in-the-middle (MITM) approach to reduce their theoretical time complexity. Practically, we re-design the implementation framework of these algorithms to fully leverage GPU parallelism, which significantly reduces the time spent on computing multiple XOR sums of bases, performing binary search, and updating distances. Meanwhile, we also propose a candidate pruning mechanism to reduce the computational burden on the GPU side and further improve the overall efficiency. Compared with the original implementations, we significantly accelerate the solving process for both normal and depth-constrained scenarios while maintaining the same solution quality. Our experimental results demonstrate that, for a 26-dimensional matrix with density 0.5, our implementation requires only 9.44 seconds on an entry-level GTX 1650 GPU, achieving a speedup of over 6{,}200imes compared with the current recursive, exhaustive, and one-threaded implementation. Using a high-performance RTX 4090 GPU, we extend the solvable boundary to 64-dimensional sparse matrices and 42-dimensional matrices with density 0.381. For 32-dimensional dense matrices, our accelerated A1 algorithm successfully establishes some new g-XOR records, including a 172-step g-XOR implementation for Whirlwind M0 and a 170-step implementation for Whirlwind M1. Besides, we also provide a 157-step g-XOR sequence for AES-InvMixColumn matrix with depth 5 through our BP-LSL implementation. Based on our accelerated BP implementation, we construct some MDS matrices with dimension 40 or more. For 4imes 4 blockwise circulant matrices of dimensions 40, 48, and 64, the minimum g-XOR sequence lengths we found are 110, 132, and 184.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2520) | 2026-10-17
