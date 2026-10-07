---
title: "BOLT-FHE: An Efficient Unified Framework for GPU-based TFHE Bootstrapping via On-Chip Local Tiling Strategies"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2356"
summary: "Bootstrapping is the main performance bottleneck in bitwise Fully Homomorphic Encryption (FHE), and practical acceleration requires careful orchestration of the blind rotation and external product cha"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Bootstrapping is the main performance bottleneck in bitwise Fully Homomorphic Encryption (FHE), and practical acceleration requires careful orchestration of the blind rotation and external product chain under GPU resource constraints. This paper presents BOLT-FHE, a GPU bootstrapping framework that emphasizes block-local execution, on-chip tiling, and a unified MegaKernel supporting both gadget decomposition and modulus raising, with optional support for a recently proposed technique (Bergerat et al, CHES 2025) based on the common mask assumption (CM packing). Our design keeps the accumulator update chain within a single thread block and fuses NTT/INTT, external products, and accumulator updates using a fixed execution template. Two compile-time parameters—WPP (warps per polynomial) and IPT (items per thread)—control multi-warp cooperation and per-thread register footprint, enabling consistent kernel structure across different parameter sets. On an NVIDIA RTX 4090, BOLT-FHE reaches 40,166 bootstrappings per second at 128-bit security, demonstrating high-throughput TFHE bootstrapping on a commodity GPU. Compared to the state-of-the-art GPU implementation VeloFHE (Shen et al, CHES 2025), BOLT-FHE achieves 1.85×–2.92× speedups with gadget decomposition. In particular, for modulus raising, BOLT-FHE improves by 2.38×–2.42× without CM packing, and by 3.17×–3.31× under the best packing configuration, reflecting the combined benefits of fused arithmetic, more regular memory access, and amortization enabled by CM packing. Overall, BOLT-FHE shows that a portable, fused-kernel organization with explicit on-chip budgeting can substantially improve TFHE bootstrapping throughput while remaining compatible with both noise management paths.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2356) | 2026-10-05
