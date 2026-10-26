---
title: "Subexponential Algorithms for LWE via Rejection Sampling on Superlattices"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2640"
summary: "Recent superlattice algorithms have improved the provable complexity of lattice problems. Ducas, Engelberts, and Loyer used this framework to obtain a subexponential algorithm for infinity-norm short "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Recent superlattice algorithms have improved the provable complexity of lattice problems. Ducas, Engelberts, and Loyer used this framework to obtain a subexponential algorithm for infinity-norm short integer solution, while also identifying a key obstacle to extending it to learning with errors (LWE). A similar difficulty arose in the analysis of Kirchner and Fouque, whose claimed subexponential running time with only linearly many LWE samples was not rigorously established. Building on the framework of Ducas, Engelberts, and Loyer, we develop two refinements based on rejection sampling that solve this open problem. First, we use rejection sampling to cancel the shift-dependent normalization factor that arises when sampling from a shifted, scaled integer lattice. This factor is a product of one-dimensional Gaussian masses and can be evaluated efficiently. This yields a provably subexponential classical search-LWE algorithm for prime qin[n^2,2n^2] and constant Gaussian error width. It uses only m=4n independent samples and runs in time and space exp(O(n/lnln n)). Second, we use random auxiliary superlattices and apply rejection sampling to the difference of two Gaussian lattice samples, ensuring that the accepted output follows the desired discrete Gaussian distribution up to a small statistical error. For q=n^{kappa+o(1)}, m=n+h=O(n), and R=hln q/[mln(2+sigma)]oinfty, the resulting algorithm uses time and space 2^{(1/2+o(1))n/ln R}, where sigma is the Gaussian error width. In particular, for sigma=n^{o(1)} and any fixed m/n>1, our algorithm achieves provable subexponential classical running time, whereas the primal and dual baselines have exponential-time bounds and earlier provable subexponential BKW analyses require Omega(nln n) samples.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2640) | 2026-10-26
