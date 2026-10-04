---
title: "Gram Moments and Pairwise Mixing of AES"
date: "2026-10-01"
updated: "2026-10-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2304"
summary: "We prove that 4k+4 rounds of AES with independent uniform round keys are 2^{-14-61k}-close to pairwise independent, improving on Hurst's announced bound of 2^{-3.82-48.03k}. Here, closeness is measure"
last_verified: "2026-10-04"
review_by: "2027-01-02"
stale: false
---

We prove that 4k+4 rounds of AES with independent uniform round keys are 2^{-14-61k}-close to pairwise independent, improving on Hurst's announced bound of 2^{-3.82-48.03k}. Here, closeness is measured by the total variation distance between the outputs on any two distinct plaintexts and those of a uniform random permutation, with the round keys sampled once and retained across evaluations. Consequently, 12, 16, and 20 rounds suffice for statistical accuracy 2^{-128}, 2^{-192}, and 2^{-256}, respectively. Our bound also holds for the complete view of any algorithm making at most two adaptive classical forward queries. We develop a general bound for local difference channels acting on additive MDS codes, expressed through the second moment of a Gram matrix. This bound controls the dependencies created by diffusion and refines the activity-space analysis of previous work. Combining the resulting contraction estimate with a sharper analysis of the initial difference distributions yields the stated mixing bound.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2304) | 2026-10-01
