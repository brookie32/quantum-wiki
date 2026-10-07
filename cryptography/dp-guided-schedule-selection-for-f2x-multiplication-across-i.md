---
title: "DP-Guided Schedule Selection for F_2[x] Multiplication across ISAs"
date: "2026-10-06"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2371"
summary: "Efficient multiplication over F_2[x] is a core primitive in classical and post-quantum cryptographic software. As ARM and RISC-V become increasingly relevant for open-source cryptographic libraries su"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Efficient multiplication over F_2[x] is a core primitive in classical and post-quantum cryptographic software. As ARM and RISC-V become increasingly relevant for open-source cryptographic libraries such as OpenSSL and liboqs, arithmetic kernels must be retuned across a wider range of Instruction Set Architectures (ISAs). High-performance arithmetic libraries recursively apply Karatsuba- and Toom-style decomposition rules, each splitting the operands into smaller subproblems and recombining the resulting products. The resulting decomposition schedule is the recursive tree of rule choices from the top-level multiplication down to the base kernels. However, hand-tuned schedules can miss better decompositions at large operand sizes, while ISA-specific primitive costs complicate cross-platform retuning. In this paper, we formulate recursive F_2[x] multiplication as a schedule-selection problem. The recursive rule space has optimal substructure, allowing dynamic programming (DP) over a compact ISA profile that accounts for base multiplication, XORs, memory traffic, and recursive overhead. The resulting schedules are materialized as dispatch tables or fixed-size kernels. Across x86-64, ARM64, RISC-V64, and RP2040, DP costs track runtime trends across input sizes, and the full rule set achieves 1.04–1.18imes geomean speedup over gf2x. HQC and BIKE integrations on the three 64-bit platforms yield 1.06–1.21imes and 1.01–1.70imes end-to-end speedups, respectively, against their platform baselines. We also evaluate Classic McEliece on these platforms. With prepared profiles, HQC/BIKE schedule selection takes 0.075–0.762 seconds, avoiding candidate compilation and benchmarking during search. The scheme provides a systematic alternative to hand tuning and measurement-driven per-size empirical search, reducing the effort required to port and retune carry-less multiplication kernels.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2371) | 2026-10-06
