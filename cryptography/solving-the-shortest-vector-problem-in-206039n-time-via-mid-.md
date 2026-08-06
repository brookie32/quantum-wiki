---
title: "Solving the Shortest Vector Problem in 2^{0.6039n} Time via Mid-point Hessian"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1597"
summary: "We present randomized algorithms for the shortest vector problem (SVP). For the n-dimensional lattice mathcal L, our algorithms solve SVP in time 2^{0.6039n+o(n)} classically and 2^{0.5411n+o(n)} quan"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

We present randomized algorithms for the shortest vector problem (SVP). For the n-dimensional lattice mathcal L, our algorithms solve SVP in time 2^{0.6039n+o(n)} classically and 2^{0.5411n+o(n)} quantumly and space 2^{0.5n+o(n)}, improving the previous best algorithm running in 2^{n+o(n)} time and space of Aggarwal, Dadush, Regev, and Stephens-Davidowitz [STOC'15]. Our algorithms heavily use the property of the Hessian of the periodic Gaussian function at the half shortest vector: For a shortest vector v in mathcal L, the Hessian at v/2 has the eigenvector close to v, which can be used to recover v using the (preprocessing) bounded distance decoding algorithm. Given the periodicity modulo mathcal L, the candidate midpoints are indexed by the parity classes in mathcal L/2mathcal L. Our algorithm searches for the class of a shortest vector by estimating the corresponding Hessians using discrete Gaussian samples. We optimize the algorithm using random sublattice cosets and various sampling technique, achieving the final complexity. The optimization techniques may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1597) | 2026-08-04
