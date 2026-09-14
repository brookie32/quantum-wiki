---
title: "Exact Error-Compensated Pruning in Matrix Multiplication Time"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2004"
summary: "We characterize the arithmetic complexity of reproducing a prescribed error-compensated pruning procedure: select weights for removal, set them to zero, and propagate each removal error to later colum"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We characterize the arithmetic complexity of reproducing a prescribed error-compensated pruning procedure: select weights for removal, set them to zero, and propagate each removal error to later columns. With its interaction factor supplied, an mimes d layer with m=Theta(d^alpha) admits a recursive execution in O_arepsilon(d^{omega(alpha,1,1)+arepsilon}+C) operations, where C is the decision cost. The execution preserves every corrected group snapshot and every subsequent decision, including unequal groups and stateful column policies. For every fixed row-wise r-of-q rule, the exponent is exactly omega(alpha,1,1); one row already has quadratic complexity. In square dimensions, matching lower bounds also hold for per-column half selection, whole-group half selection under every contiguous partition, and the reference implementation's inclusive threshold rule with its actual removal count. Under the inverse-Cholesky kernel, all these square lower bounds survive raw calibration and every prescribed nonnegative damping. The square reductions encode an arbitrary product with quadratic overhead, weights bounded by four, covariance condition number below two, and separated score cuts. Their mechanism is a source-to-target factor cancellation, with separate snapshot bounds and isolated guards enforcing the different selectors. A local coefficient-extraction argument validates the exponent comparison in the presence of comparisons and square roots. The results concern exact numerical execution in a nonuniform scalar model; raw rectangular preprocessing and the direct inverse-matrix kernel are treated separately.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2004) | 2026-09-13
