---
title: "Software-Pipelining The Number Theoretic Transform on Neural Processing Units: A Loop-Fission Methodology"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2474"
summary: "Lattice-based post-quantum cryptography (PQC) and fully homomorphic encryption (FHE) rely heavily on the number theoretic transform (NTT) for efficient polynomial multiplication. While GPUs and FPGAs "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Lattice-based post-quantum cryptography (PQC) and fully homomorphic encryption (FHE) rely heavily on the number theoretic transform (NTT) for efficient polynomial multiplication. While GPUs and FPGAs have been widely explored for NTT acceleration, neural processing units (NPUs), a rapidly growing class of AI accelerators, remain largely unexplored for cryptographic workloads. In this work, we develop a methodology for accelerating the NTT on NPUs, using AMD’s AI Engine (AIE) architecture as a representative NPU to develop and benchmark it. At its core is manual loop fission, in which large and complex loops are split into smaller primitives, enabling highly efficient software pipelining and avoiding memory stalls or register spilling. Applying it, we develop efficient Barrett reduction primitives and use these to construct three high-throughput, low-latency NTT implementations (radix-2, radix-4, and radix-8), achieving significant performance gains over the AIE compiler and prior literature. On AMD’s first-generation AIE specifically, we achieve speedups of 8.27imes to 13.2imes in throughput and 2.44imes to 10.3imes in latency per AIE tile in comparison with prior work. Our implementations support arbitrary NTT-friendly moduli and polynomial sizes up to degree 4096 for 14-bit moduli and 2048 for 30-bit moduli. Finally, we discuss the portability of our techniques to other NPU architectures, and identify which architectural features are most beneficial for NTT acceleration.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2474) | 2026-10-14
