---
title: "One Discrete Gaussian Sample in 2^{n/2+o(n)} Time"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1599"
summary: "Aggarwal, Dadush, Regev, and Stephens-Davidowitz (ADRS; STOC 2015) sample 2^{n/2} discrete Gaussians at an arbitrary parameter in 2^{n+o(n)} time, and above smoothing in 2^{n/2+o(n)} time. They ask wh"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Aggarwal, Dadush, Regev, and Stephens-Davidowitz (ADRS; STOC 2015) sample 2^{n/2} discrete Gaussians at an arbitrary parameter in 2^{n+o(n)} time, and above smoothing in 2^{n/2+o(n)} time. They ask whether the latter bound suffices for one sample at an arbitrary parameter. We answer this question affirmatively: for every rank-n lattice LsubseteqR^n specified by a rational basis and every rational s^2>0, we produce one sample from D_{L,s} within statistical distance exp(-Omega(n^3)) in expected 2^{n/2+o(n)} time and 2^{n/2+o(n)} space on every execution. The algorithm samples from random superlattices that are smooth at the required scale with constant probability and outputs the first point in L; a Gaussian-mass comparison shows that the 2^{n/2} samples produced by one ADRS call contain a point of L with inverse-polynomial probability. The factor 2^{n/2} is tight in this Gaussian-mass comparison. For every fixed rational alpha<1.4697, the same comparison gives a sub-2^n algorithm for exact CVP on targets satisfying ist(y,L)lealphalambda_1(L), without a uniqueness assumption, and an exact-SVP algorithm in 2^{0.7315n+o(n)} time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1599) | 2026-08-04
