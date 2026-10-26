---
title: "A Memory-efficient Implementation of Wiedemann XL"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2641"
summary: "The signature schemes MQOM, SNOVA, MAYO, and UOV are third-round candidates in the NIST standardization process for additional post-quantum signatures, and their security relies on the hardness of the"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

The signature schemes MQOM, SNOVA, MAYO, and UOV are third-round candidates in the NIST standardization process for additional post-quantum signatures, and their security relies on the hardness of the multivariate quadratic (MQ) problem. XL with block Wiedemann (BW) is one of the most efficient MQ solvers in practice, but its memory demand has led to a debate about its memory access cost: generating the rows of the Macaulay matrix on the fly is widely believed to save memory at a non-negligible computational cost. In this work, we evaluate the memory--time trade-off in practice. We provide the first efficient on-the-fly implementation of XL with BW. We build on the state-of-the-art implementation by Cheng, Chou, Niederhagen, and Yang (CCNY), which uses SSE instructions and supports the fields F_2, F_{16} and F_{31}; we remove its column-index tables and generate the rows on the fly in the first phase of BW (BW1). We amortize the cost of on-the-fly generation with a new algorithm that computes column indices with O(n^2) instead of O(n^3) table look-ups, where n is the number of variables. In our experiments we observe that our on-the-fly implementation achieves running times comparable to CCNY's with up to five times less memory. We also port both implementations to AVX2 over F_{256}, the main field of UOV, and observe a similar behavior: comparable BW1 running times with less memory for the on-the-fly variant.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2641) | 2026-10-26
