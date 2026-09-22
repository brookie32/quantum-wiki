---
title: "Actively Secure PPML with Soft-Boundary Overflow Detection"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2105"
summary: "MPC-based privacy-preserving machine learning (PPML) typically operates over finite rings rather than floating-point arithmetic, making arithmetic overflow an inherent risk. Existing overflow-detectio"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

MPC-based privacy-preserving machine learning (PPML) typically operates over finite rings rather than floating-point arithmetic, making arithmetic overflow an inherent risk. Existing overflow-detection techniques generally require the evaluation of nonlinear functions, resulting in substantial computation and communication overhead. We propose Soft Boundary Detection, which reduces boundary verification to probabilistic functions over partitioned intervals, with a cost comparable to that of linear computation. Building on this abstraction, we develop an efficient mechanism for detecting arithmetic overflow in PPML workloads. Moreover, we show that Soft Boundary Detection naturally extends to the malicious-adversary setting. In ring-based computation, it further avoids the need to choose a ring space substantially larger than the actual data range to ensure soundness against malicious behavior. Our framework provides two key benefits: (1) highly efficient arithmetic overflow detection, and (2) active security without requiring ring extension or enlarging the underlying ring space. Experimental results demonstrate that our approach substantially strengthens security while retaining high efficiency, providing a practical solution for robust and actively secure PPML.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2105) | 2026-09-19
