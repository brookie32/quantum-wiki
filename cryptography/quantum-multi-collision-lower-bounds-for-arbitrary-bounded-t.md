---
title: "Quantum Multi-Collision Lower Bounds for Arbitrary Bounded Types"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2663"
summary: "We study quantum collision finding for functions of prescribed exact type. For fixed constants kge rge2 and N=kn, consider functions f:[N]omathbb Z_q of type (k^n), with exactly n distinct output valu"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

We study quantum collision finding for functions of prescribed exact type. For fixed constants kge rge2 and N=kn, consider functions f:[N]omathbb Z_q of type (k^n), with exactly n distinct output values and k preimages for each value. We prove that the worst-case bounded-error quantum query complexity of finding r-collisions in ell distinct equality classes is [ Theta_{k,r}!left( ell^{,2^{r-1}/(2^r-1)} N^{(2^{r-1}-1)/(2^r-1)} right) ] for 1leellle N^{2^{-r}}. The result is uniform over all feasible alphabet sizes qge n. Our proof uses the compressed permutation oracle (CPO). We establish a recurrence for intermediate collision counts and control its accumulated error to obtain database tails exponentially small in ell. The improved CPO soundness estimate then converts these database bounds into function-query lower bounds. Moreover, we extend the analysis to arbitrary exact types with bounded class sizes, without requiring any particular class size to occur linearly often. The resulting lower bounds are tight when forward permutation access is additionally available, although they need not be tight for the original function-query problem. Finally, a sampling reduction relates our collision bounds to sparse k-distinctness instances. A separate analysis using Belovs's transfer framework recovers the same lower-bound exponent, establishing a concrete connection between the two approaches.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2663) | 2026-10-28
