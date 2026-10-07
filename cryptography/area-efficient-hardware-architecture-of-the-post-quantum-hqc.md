---
title: "Area-Efficient Hardware Architecture of the Post-Quantum HQC Cryptosystem with Side-Channel Protection"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2359"
summary: "The Hamming-Quasi Cyclic (HQC) is the Post-Quantum Cryptography (PQC) Key Encapsulation Mechanism (KEM) algorithm recently selected by the National Institute of Standards and Technology (NIST) for sta"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The Hamming-Quasi Cyclic (HQC) is the Post-Quantum Cryptography (PQC) Key Encapsulation Mechanism (KEM) algorithm recently selected by the National Institute of Standards and Technology (NIST) for standardization as an alternative candidate for the KEM category. While the algorithm is mathematically robust, several studies state that the physical implementation of HQC remains vulnerable to power-based side-channel attacks (SCA). Countermeasures for such SCAs primarily focus on masking and shuffling, which severely increase hardware resources, introducing additional performance overhead. To address this problem, this paper presents a resource-efficient, constant-time hardware architecture for HQC that features a novel idle-hardware reuse strategy as an SCA countermeasure. By intentionally reusing the KECCAK hardware to generate dynamic power during decoding, the proposed architecture scrambles secret-dependent power correlations with less than 0.5% area overhead for the countermeasure logic. The complete design is fully parameterized to support all NIST security categories (HQC-128, HQC-192, and HQC-256). A prototype implementation on an Artix-7 FPGA achieves a maximum clock frequency of 139 MHz while consuming 11,489 LUTs, 6,785 FFs, and 4 DSPs. Functional correctness is verified via NIST Known Answer Tests (KATs) across Key Generation, Encapsulation, and Decapsulation operations, and Test Vector Leakage Assessment (TVLA) confirms significant suppression of side-channel leakage.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2359) | 2026-10-05
