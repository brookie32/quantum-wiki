---
title: "A Polynomial-Time Quantum Algorithm for the Dihedral Coset Problem"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1591"
summary: "We present a polynomial-time quantum algorithm for the Dihedral Coset Problem (DCP). The algorithm is based on Regev's polynomial-time reduction of the Dihedral Subgroup Problem (DSP) to the modular s"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

We present a polynomial-time quantum algorithm for the Dihedral Coset Problem (DCP). The algorithm is based on Regev's polynomial-time reduction of the Dihedral Subgroup Problem (DSP) to the modular subset sum problem, but uses a different technique to erase sample bits without use of a subset sum oracle. The algorithm can thus combine with Regev's reduction of lattice problems to DCP, improved by Brakerski, Kirshanova, Stehl{e and Wen, to yield polynomial-time quantum algorithms for various lattice problems, such as finding a polynomial-factor approximation to the shortest vector in an n-dimensional lattice (SVP), and the ``learning with errors'' problem (LWE). The algorithm can tolerate a faulty sample rate as high as 1/O(log{n}), allowing the algorithm-reduction combination to efficiently solve, for example, SVP with a sqrt{n} polylog(n) approximation factor, or LWE instances with alpha=sqrt{n} polylog(n).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1591) | 2026-08-03
