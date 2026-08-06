---
title: "New Designs of Multivariate-Polynomial Universal Hash Functions"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1602"
summary: "Universal hash functions (UHFs) are basic building blocks in cryptography, making the topic of designing secure, fast UHFs of longstanding interest. This paper presents an exploration of the design sp"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Universal hash functions (UHFs) are basic building blocks in cryptography, making the topic of designing secure, fast UHFs of longstanding interest. This paper presents an exploration of the design space for multivariate UHFs, that is UHFs that involve the evaluation of a multivariate polynomial over a finite field. We focus on two-level designs, wherein a lower-level hash function produces intermediate values that are consumed by a higher-level one, and where both hash functions are based on either univariate or multivariate polynomials. This approach allows designs to benefit from the desirable features of both components and thereby strike new trade-offs between key size, security level, and amenability to optimization techniques. We extend the recent UHF code generation and benchmarking framework of Degabriele et al. (IEEE S&P 2024) to accommodate our multivariate designs (and also to support binary field arithmetic). We then use the framework to study the performance of a large collection of new two-level designs. This is done by first conducting a statistical factor analysis to determine which design features (and combinations of those features) most influence performance, and then using it to identify particular combinations of lower-level and higher-level hash functions offering particularly good performance/security trade-offs. We present new designs for both binary and prime fields, at two different security levels (corresponding to roughly 128 and 256 bits of security). Our best designs have performance that significantly outperforms state-of-the-art UHFs in the research literature and as deployed in mainstream cryptography libraries by up to 25%, resulting in 0.3 cycles/byte for 128-bit binary fields. We expect further gains from optimizations such as vectorization, as our benchmarks rely purely on auto-generated code from the extended framework, while state-of-the-art implementations typically use hand-optimized implementation strategies. We conclude with a brief inquiry into the performance implications of employing our best UHF design in the AEAD and Accordion mode designs currently under consideration for standardization by NIST.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1602) | 2026-08-04
