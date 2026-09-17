---
title: "Tighter and Friendlier Integer Bounds for Quaternion Algorithms - Application to SQIsign"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2049"
summary: "The digital signature scheme SQIsign, currently under consideration in NIST's call for additional post-quantum signatures, offers the smallest key and signature sizes among all candidates. Its signing"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The digital signature scheme SQIsign, currently under consideration in NIST's call for additional post-quantum signatures, offers the smallest key and signature sizes among all candidates. Its signing procedure, however, relies on an involved arithmetic layer over quaternions, in which the objects are represented by small-dimensional integer lattices. In this layer, the intermediate integers can grow significantly larger than the final outputs. Controlling this growth is essential for fixed-precision and, ultimately, constant-time implementations. In this work, we revisit the integer-size analysis of this arithmetic layer. We first observe that all lattices arising in SQIsign satisfy a structural containment property that allows their canonical form to be computed with a modulus of half the bit length used in previous analyses. Exploiting the same property, we give a matrix inversion algorithm using only exact divisions whose intermediate integers remain bounded by twice the modulus. This algorithm avoids the cubic blow-up of standard inversion methods. We show that the triangular-form convention used in the SQIsign implementation reduces the size of intermediate values by a factor of O(p). Second, we show that these lattices can be represented in dimension two over the Gaussian integers instead of dimension four over the integers. This allows us to replace the LLL algorithm by the simpler Lagrange reduction that has the number of iterations bounded by a multiple of the bit-size of the longest input vector. Furthermore, this reduction provably outputs the shortest basis without requiring floating-point arithmetic. Combining these results, we derive integer-size bounds for SQIsign key generation and signing, improving on previous bounds for key generation and for all signing subroutines outside of the response quaternion sampling. We provide an implementation of our algorithms in the GMP-based C reference implementation of SQIsign.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2049) | 2026-09-15
