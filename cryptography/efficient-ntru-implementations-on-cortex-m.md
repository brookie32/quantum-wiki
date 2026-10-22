---
title: "Efficient NTRU+ Implementations on Cortex-M"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2568"
summary: "Post-quantum cryptography on embedded devices requires implementations that perform cryptographic operations efficiently within limited computation and memory. Most lattice-based KEMs use 2-way NTTs o"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

Post-quantum cryptography on embedded devices requires implementations that perform cryptographic operations efficiently within limited computation and memory. Most lattice-based KEMs use 2-way NTTs over power-of-two cyclotomic rings, and their embedded implementations have been studied extensively. In contrast, implementations of schemes based on 3-way NTTs, which combine radix-3 and radix-2 layers, remain scarce. This work therefore presents efficient implementations of NTRU+, a KEM built on 3-way NTTs, on Arm Cortex-M0+, M3, M4, and M7. We configure the layer fusion, modular arithmetic, and instruction scheduling of the 3-way NTT for each parameter set and core. We also introduce ω-folded front layers, which compute the first two layers of the forward NTT on ternary inputs without modular reduction. Based on these techniques, we present two implementations. The speed-optimized implementation keeps operands as full polynomial arrays to prioritize execution time. The memory-optimized implementation reuses a single polynomial workspace and regenerates the required operands in pieces aligned with radix-3 blocks. On physical boards, the speed-optimized implementation reduces execution time by up to 52.43% compared with the official optimized C implementation. The memory-optimized implementation reduces peak stack usage by up to 82.60% while running faster than the official optimized C implementation in every KEM operation. A controlled NTT-replacement experiment and per-technique comparisons show that the same technique can have different effects depending on the instruction set and pipeline of each core.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2568) | 2026-10-20
