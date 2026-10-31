---
title: "(Balanced) Boolean Functions on 375 Variables with Nonlinearity Exceeding the Patterson-Wiedemann Direct-Sum Bound"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2680"
summary: "Patterson and Wiedemann [IEEE-IT 1983] constructed Boolean functions on 15 variables with nonlinearity 16276, which is strictly greater than the bent concatenation bound. Taking their direct sum with "
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Patterson and Wiedemann [IEEE-IT 1983] constructed Boolean functions on 15 variables with nonlinearity 16276, which is strictly greater than the bent concatenation bound. Taking their direct sum with a bent function gives nonlinearity 2^{n-1}-27dot2^{(n-11)/2} for every odd nge15. Much later, Schmidt [JCT-A 2019] proved that the asymptotic maximum nonlinearity is 2^{n-1}-(1+o(1))2^{n/2-1} as noinfty. In this work, we construct Boolean functions f on 375 variables such that the nonlinearity is greater than 2^{374}-442367dot2^{168}=2^{374}-2^{187}+81921dot2^{168}, which exceeds the direct sum of a 15-variable Patterson-Wiedemann function and a bent function on 360 variables. To be specific, the direct sum of a 15-variable Patterson-Wiedemann function and a 360-variable bent function has nonlinearity 2^{374}-2^{187}+20dot2^{180}=2^{374} 2^{187}+81920dot2^{168}. Thus our construction improves on this direct-sum value by more than 2^{168}. Our construction idea is as follows. Let H be the multiplicative subgroup of order (2^{375}-1)/751 in mathbb F_{2^{375}}^*. The support of f is the disjoint union of 375 prescribed cosets and a subset Bsubseteq H. The evaluation of Gauss sums reduces the contribution of the prescribed cosets to a computation of 751 integers. The conditions on B form a 0-1 linear feasibility problem. Using a potential criterion for simultaneous linear constraints, we prove the existence of a single subset Bsubseteq H satisfying the constraints at all frequencies. Taking direct sums with bent functions extends the result to every odd nge375. The support construction does not require balancedness. As a natural follow-up, we also obtain balanced functions with the same strict lower bound by changing the minimum possible number of values, using sampling without replacement. The subsets B and the sets of modified points are obtained by existence proofs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2680) | 2026-10-29
