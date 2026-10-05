---
title: "Low-Noise Multi-Value Bootstrapping via Log-Unit Lattice Search and LUT Shifting"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2310"
summary: "Programmable bootstrapping is a central procedure in the FHEW and TFHE families of fully homomorphic encryption schemes, but its computational cost remains a major performance bottleneck. Multi-value "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Programmable bootstrapping is a central procedure in the FHEW and TFHE families of fully homomorphic encryption schemes, but its computational cost remains a major performance bottleneck. Multi-value bootstrapping amortizes this cost by sharing a blind rotation among several functions evaluated on the same encrypted input. However, the standard choice of common factor for multi-value bootstrapping can produce unnecessarily large noise amplification for many collections of lookup tables, thereby reducing the practical benefits of sharing the blind rotation. The main contribution of this work is a log-unit lattice search for selecting common factors that substantially reduce this amplification. This search is complemented with LUT shifting, which generates alternative function-preserving test-polynomial representations and further enlarges the search space. Both optimizations are performed offline and leave the online procedure of multi-value bootstrapping essentially unchanged. The proposed construction is evaluated in TFHE at failure probability 2^{-128}. For example, on 256-bit homomorphic integer multiplication, it achieves a latency speed-up of 1.47imes and a throughput improvement of 1.59imes relative to a baseline that evaluates each output with a separate programmable bootstrapping.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2310) | 2026-10-02
