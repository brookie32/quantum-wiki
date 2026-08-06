---
title: "Strided Frobenius Additive FFT and its Application to HQC"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1588"
summary: "Boolean polynomial multiplication is the primary computational bottleneck of the Hamming Quasi-Cyclic (HQC) key encapsulation mechanism. In this paper, we reframe the Frobenius Additive FFT (FAFFT) in"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Boolean polynomial multiplication is the primary computational bottleneck of the Hamming Quasi-Cyclic (HQC) key encapsulation mechanism. In this paper, we reframe the Frobenius Additive FFT (FAFFT) in ring-theoretic terms, via quotient-ring homomorphisms and the Chinese Remainder Theorem. This perspective shows that a complete decomposition into evaluation points is unnecessary for multiplication, and naturally yields the Strided FAFFT (SFAFFT), which operates over smaller finite fields with fewer butterfly stages and admits a much sparser CRT modulus for the non-power-of-two degrees in HQC. Our SFAFFT implementations outperform all previous FAFFT-based multiplications on every tested platform (x86 AVX2, GFNI, Apple M1, ARM Cortex-A72, and Cortex-M4), and set new overall speed records for HQC in nearly all settings except plain AVX2, where Toom-Cook-Karatsuba remains faster for the two smaller parameter sets.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1588) | 2026-08-03
