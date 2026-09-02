---
title: "Improved Conversion for Gao-Zheng FHE Scheme with O(1) Bootstrapping"
date: "2026-08-30"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1836"
summary: "Efficiently supporting both arithmetic operations and logic operations in Fully Homomorphic Encryption (FHE) is an essential step towards general-purpose privacy-preserving computation. Recently, Gao "
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Efficiently supporting both arithmetic operations and logic operations in Fully Homomorphic Encryption (FHE) is an essential step towards general-purpose privacy-preserving computation. Recently, Gao and Zheng (Crypto'26) introduced a triangle encoding for arithmetic computation over n-bit machine words, with the refreshing cost of O(1) CKKS bootstrapping operations. Notably, the triangle encoding can be converted to the discrete-CKKS encoding for supporting logic operations, with the cost of amortized O(1) CKKS bootstrapping for O(n) input ciphertexts, or O(n) CKKS bootstrapping operations for a single input ciphertext. It remains open whether there is a cheaper conversion method for a single input ciphertext. In this work, we propose a new conversion method to discrete-CKKS encoding for a single ciphertext in triangle encoding, with the cost of O(1) CKKS bootstrapping and additional O(log n) level consumption. When combined with existing refreshing and conversion methods in Gao-Zheng, we obtain an FHE scheme for SIMD Arithmetic Logic Unit (ALU) with O(1) bootstrapping.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1836) | 2026-08-30
