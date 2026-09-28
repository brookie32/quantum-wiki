---
title: "Enhanced Embarrassingly Parallel Attacks against EC-HMQV-C and ECMQV"
date: "2026-09-27"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2234"
summary: "In~ite{sarr25}, Sarr introduced an embarrassingly parallel impersonation attack against ECMQV and ECHMQV-C whose core step is an adding-based pseudo-random walk over a cyclic group G, of order n, sear"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

In~ite{sarr25}, Sarr introduced an embarrassingly parallel impersonation attack against ECMQV and ECHMQV-C whose core step is an adding-based pseudo-random walk over a cyclic group G, of order n, searching for a decomposed i-point. In this work, we revisit that construction in the richer multi-party setting where two sets of parties, the initiators {hat{A}_1,dots,hat{A}_{z_1}}, and the responders {hat{B}_1,dots,hat{B}_{z_2}}, interact under ECHMQV-C. First, we exhibit an embarrassingly parallel attack such that, when m~processors are available, the attack runs in expected time $ frac{sqrt{n}}{m,z_1 z_2}left(osta(z_1)+ostd(z_1 z_2)right), wherein osta(z_1) is the time for a batch of z_1 elliptic-curve additions and ostd(z_1 z_2) is the time for a batch of z_1 z_2 digest computations. Second, for any positive integer z_3 such that z_1 z_2 z_3ll sqrt{n}, we propose an improved attack that runs in time frac{sqrt{n}}{m,z_1 z_2 z_3}left(osta(z_1 z_3)+ostd(z_1 z_2 z_3)right), Third, for ECMQV, assuming z_1z_3 ll sqrt{n}, we propose an attack that runs in time frac{sqrt{n}}{m,z_1 z_3}osta(z_1 z_3). The attacks require no shared storage among processors, they require respectively O(z_1 z_2), O(z_1 z_2 z_3), and O(z_1 z_3) memory complexity at each processor, and only marginal server--processor communication. As a concrete illustration, for a 128-bit ECHMQV-C instance, with m=2^{10} processors, z_1=z_2=2^{15}, and z_3=2^{10}$, our improved attack yields an effective parallel running time corresponding to 78 bits of security under an idealized massively parallel architecture in which the required batch elliptic-curve additions can be evaluated concurrently. This figure refers to parallel time rather than total computational work, which remains proportional to the number of elliptic-curve additions performed.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2234) | 2026-09-27
