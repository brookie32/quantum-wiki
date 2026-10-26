---
title: "Bounds on polynomial approximations of the discrete logarithm function"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2621"
summary: "We revisit a classical result of Coppersmith and Shparlinski [CS00] showing bounds on how well polynomials can approximate the discrete log function. They showed that for any univariate polynomial f(X"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

We revisit a classical result of Coppersmith and Shparlinski [CS00] showing bounds on how well polynomials can approximate the discrete log function. They showed that for any univariate polynomial f(X) in F_p[X] with eg(f) leq D, we have: $ |{ x in F_p^imes mid f(x) = mathsf{dlog}(x) }| leq sqrt{2 D p}. We show two improvements: (1) For all D, we improve the upper bound above to (1+o(1)) dot sqrt{Dp}. In particular, we give nontrivial upper bounds on the approximation even for D > p/2. This new upper bound is the Johnson bound from the theory of list-decoding of error-correcting codes, and in fact our proof uses a connection to that problem, as well as other combinatorial ideas. (2) For D = 1, where both the above bounds are O(sqrt{p}), we give an asymptotically improved upper bound of O(p^{2/5}). This is based on the sum-product phenomenon of additive combinatorics. We also improve the [CS00] bounds on the number of points of the form (x, mathsf{dlog}(x)) in F_p^2 that any bivariate polynomial Q(X,Y) in F_p[X,Y] with eg(Q) leq D$ can vanish on, with our new bounds approaching the analogue of the Johnson bound for this problem.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2621) | 2026-10-24
