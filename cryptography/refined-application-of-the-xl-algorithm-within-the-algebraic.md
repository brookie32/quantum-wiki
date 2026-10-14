---
title: "Refined Application of the XL Algorithm within the Algebraic Approach to the Regular Syndrome Decoding Problem"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2470"
summary: "The Syndrome Decoding Problem (SDP) is a fundamental mathematical problem underlying code-based cryptography, which is considered a promising candidate for post-quantum cryptography. The Regular Syndr"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

The Syndrome Decoding Problem (SDP) is a fundamental mathematical problem underlying code-based cryptography, which is considered a promising candidate for post-quantum cryptography. The Regular Syndrome Decoding Problem (RSDP) is a variant of the SDP in which the error vector follows a specific block-wise structure. Recent developments in RSDP-based cryptographic schemes have led to a wider variety of parameter settings, making it increasingly important to evaluate the complexity of solving the RSDP over a broad range of parameters. One of the main approaches to solving the RSDP is the algebraic approach, which transforms a given RSDP instance into a polynomial system and solves it using algebraic techniques such as the XL algorithm. In this work, we construct and analyze algebraic algorithms for the RSDP by combining and extending techniques used in existing algebraic approaches. Our algorithms mainly follow the framework of the hybrid algorithm proposed by Wang et al., while allowing an arbitrary solving degree d in the application of the XL algorithm. We further consider two variants: an XFL-based method that combines partial Gaussian elimination with variable guessing, and a WXL-based method that exploits the sparsity of the Macaulay matrix. Our complexity analysis for various parameter settings shows that, for some fixed values of n and k, the WXL-based variant using a larger solving degree d>2 is particularly efficient when the block size eta is sufficiently small, while the original hybrid algorithm becomes more efficient as eta increases.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2470) | 2026-10-14
