---
title: "Efficient Ternary Computation of Optimal Ate Pairing on BLS27 Curves"
date: "2026-07-24"
updated: "2026-07-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1522"
summary: "The computation of optimal Ate pairings on elliptic curves with embedding degree k=27 (BLS27) is highly relevant for achieving the 256-bit security level, especially in the context of recent advances "
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

The computation of optimal Ate pairings on elliptic curves with embedding degree k=27 (BLS27) is highly relevant for achieving the 256-bit security level, especially in the context of recent advances in the Number Field Sieve (NFS) and its variants (exTNFS, SexTNFS). Traditional binary approaches fail to fully exploit the degree-3 extension tower of Fpk{27}. In this work, we propose an efficient ternary version of the Miller loop, restricting the seed representation to sparse ternary digits {0, 1} to streamline point operations and eliminate costly inversions. Furthermore, we generate two new parameter seeds tailored for exTNFS and SexTNFS security levels. These seeds feature sparse ternary representations that simultaneously guarantee the efficiency of the Miller loop and allow the full exploitation of cyclotomic cubing in F_{p^{27}} during the hard part of the final exponentiation. Compared to the state of the art binary approach by Fouotsa et al. (2020), our exTNFS seed yields a 22% improvement in the overall optimal Ate pairing computation cost. Concurrently, our proposed SexTNFS seed ensures a higher level of security against the most advanced NFS variants.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1522) | 2026-07-24
