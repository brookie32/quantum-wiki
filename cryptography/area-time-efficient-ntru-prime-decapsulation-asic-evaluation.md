---
title: "Area-Time Efficient NTRU Prime Decapsulation: ASIC Evaluation of the First Five-Way Char-3 Multiplier"
date: "2026-09-16"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2064"
summary: "Streamlined NTRU Prime (sntrup761) is a lattice-based key encapsulation mechanism that, although not a NIST standard, remains widely deployed in critical internet infrastructure. It is the post-quantu"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Streamlined NTRU Prime (sntrup761) is a lattice-based key encapsulation mechanism that, although not a NIST standard, remains widely deployed in critical internet infrastructure. It is the post-quantum key-exchange default in OpenSSH, standardized in RFC 9941, and used well beyond SSH, in Red Hat Enterprise Linux, the liboqs library, PQConnect, and commercial VPNs. Its decapsulation performs a polynomial multiplication over the characteristic-three ring Z_3[x]/(x^{p}-x-1), so faster methods for this operation directly improve these protocols. We use the Yeniaras-Cenk 5-way multiplier (U1-hybrid), which has the lowest arithmetic complexity among characteristic-three multipliers and gives a 35.52% scalar-C software speedup over Bernstein's three-way method (B1). Yet every prior NTRU Prime hardware design, on FPGA or the single existing ASIC, uses only schoolbook or a single layer of two-way Karatsuba. Three-way splits have been implemented only in software; no 5-way split had been implemented at all before this work. We present the first ASIC evaluation of the Yeniaras-Cenk 5-way multiplier (U1-hybrid), synthesized to the Nangate 45 nm library and compared against the state-of-the-art parallel schoolbook multiplier of Peng et al. On the area-delay product (ADP), the Yeniaras-Cenk 5-way multiplier is 6.8x better than the Peng schoolbook at the multiplier level, and 1.27x better in the sntrup761 decapsulation core, which it completes in 2471 cycles against Peng's 3829, a 35.5% core reduction (12.4% once the fixed hash is included). We also compare against a 3-way Karatsuba baseline (Bernstein's B1), noting that no optimized hardware B1 exists and we do not build one; the comparison there is at the operation-count level only. Synthesizing U1 and B1 as combinational circuits isolates where the five-way advantage comes from. It is not gate count: each F_9 product expands into four F_3 products, so at the same architecture the two use nearly the same area. The gain is in depth, as those four F_3 products run in parallel: 138.27 ps against 57.95 ps for one F_3 multiplier, 2.4x rather than 4x. The advantage is thus a hardware effect: it grows with design parallelism and matches the scalar-C software figure across two parameter sets. All Verilog, testbenches, and synthesis scripts are openly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2064) | 2026-09-16
