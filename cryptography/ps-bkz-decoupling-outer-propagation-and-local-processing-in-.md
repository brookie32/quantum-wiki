---
title: "PS-BKZ: Decoupling Outer Propagation and Local Processing in BKZ by Parameter Separation"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2736"
summary: "This work provides a systematic study of parameter separation in Block Korkine–Zolotarev (BKZ) reduction. We propose a general framework with separate parameters for outer propagation and the dominant"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

This work provides a systematic study of parameter separation in Block Korkine–Zolotarev (BKZ) reduction. We propose a general framework with separate parameters for outer propagation and the dominant local computation. The framework covers the local parameter settings of standard BKZ and variants using extended preprocessing, dimensions for free, or progressive sieving, with corresponding adaptations to the outer operations. This allows less expensive local processing without narrowing the outer propagation range. Within this framework, we give idealized and executable constructions that use inner BKZ with a smaller blocksize to supply local vectors for larger outer blocks. We derive a worst-case quality bound for the idealized construction and analyze its quality–cost behavior using a practical fixed-point model. Experiments on the executable construction cover random q-ary bases up to dimension 300 and SVP Challenge bases up to dimension 240. The detailed comparisons at n ≥ 200 show lower mean root-Hermite factors (RHFs) and 14.1%–59.3% shorter mean running times than BKZ 2.0. Joint improvements generally become more frequent with dimension. On q-ary inputs against BKZ 2.0 with blocksize 50, their frequency increases from 15.56% at n = 150 to 73.33% at n = 300.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2736) | 2026-11-03
