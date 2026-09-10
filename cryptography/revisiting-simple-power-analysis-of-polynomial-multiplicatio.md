---
title: "Revisiting Simple Power Analysis of Polynomial Multiplication in the HQC Implementation"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1906"
summary: "The Hamming Quasi-Cyclic (HQC) scheme is a post-quantum key encapsulation mechanism recently selected for standardization by NIST, making the security of its implementations a critical concern. In thi"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

The Hamming Quasi-Cyclic (HQC) scheme is a post-quantum key encapsulation mechanism recently selected for standardization by NIST, making the security of its implementations a critical concern. In this work, we revisit the side-channel resistance of the latest HQC reference implementation, with a focus on its polynomial multiplication routine used in decryption. While prior work demonstrated a simple power analysis (SPA) attack against a lookup-table-based multiplication, the updated implementation replaces this with a bitwise schoolbook multiplication. Despite these modifications, we show that the updated function schoolbook_mul still shows clear, visually distinguishable variations in power consumption that depend on secret data. Using these patterns, an attacker can recover individual bits of the secret polynomial, demonstrating that SPA remains effective against the updated design. To address this vulnerability, we analyze potential countermeasures and propose a zero-cost mitigation based on swapping operand roles so that the mask computation depends only on public data. This eliminates direct leakage of secret-dependent control flow while preserving performance.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1906) | 2026-09-07
