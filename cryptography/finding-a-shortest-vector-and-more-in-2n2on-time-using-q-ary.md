---
title: "Finding a Shortest Vector and More in 2^{n/2+o(n)} Time using q-ary Coset Difference Tree"
date: "2026-09-02"
updated: "2026-09-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1859"
summary: "This paper presents a new randomized algorithm for solving the exact shortest vector problem. For the n-dimensional lattice mathcal L, our algorithm runs in time and space 2^{n/2+o(n)}. Our algorithm "
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

This paper presents a new randomized algorithm for solving the exact shortest vector problem. For the n-dimensional lattice mathcal L, our algorithm runs in time and space 2^{n/2+o(n)}. Our algorithm can be viewed as a q-ary analogue of the midpoint Hessian for an odd prime q; more precisely, we use the fact that, for a shortest vector v, the gradient (rather than Hessian) of the periodic Gaussian function at v/q is nearly proportional to v (up to sign), even after aggregation over a relatively large random affine coset. We compute the relevant coset gradient along a chain of intermediate lattices using a combinatorial procedure inspired by Wagner's generalized birthday algorithm, yielding the 2^{n/2+o(n)} time and space complexity. A variant of the algorithm solves the exact closest vector problem on every input (y,mathcal L) with a distance guarantee operatorname{dist}(y,mathcal L)le 1.039lambda_1(mathcal L) within the same time and space complexity. This guarantee holds for a random target and a random lattice drawn according to the Haar-Siegel measure. Thus, this algorithm solves a closest vector problem on such random instances in time and space 2^{n/2+o(n)}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1859) | 2026-09-02
