---
title: "A Provable Subexponential-Time Algorithm for LWE from (n+o(n)) Samples via Wagner-Style Gaussian Sampling"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2261"
summary: "We give a randomized subexponential-time algorithm for decision Learning with Errors (LWE) in two complementary parameter regimes. For polynomial prime modulus (q=n^{kappa+o(1)}) with any fixed (kappa"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

We give a randomized subexponential-time algorithm for decision Learning with Errors (LWE) in two complementary parameter regimes. For polynomial prime modulus (q=n^{kappa+o(1)}) with any fixed (kappa>1/2), the algorithm handles independent discrete Gaussian errors drawn from (D_{mathbb Z,s_e}), with Gaussian parameter (s_e) satisfying (ln(2+s_e)=(ln n)^{a+o(1)}) for any fixed (0le a0), can be handled with a quasipolynomial prime modulus (q=exp!left((ln n)^{1+eta+o(1)}right)) for any fixed (eta>0). In both regimes, for an arbitrary secret distribution, the algorithm succeeds with probability (1-o(1)) using (m=n+Theta(n/lnln n)) original samples, with expected time and space (2^{Theta(n/lnln n)}). Our starting point is the Wagner-style Gaussian sampler of Ducas, Engelberts, and Loyer (CRYPTO 2025). We instantiate its auxiliary extensions with random (P)-ary lattices whose improved smoothing bound supports the accuracy required for LWE without increasing the leading list size exponent. At the smaller Gaussian width enabled by this geometry, the basis-dependent condition of the exact sampler used in prior work is no longer available. We therefore use the statistically approximate shifted discrete Gaussian sampler of Aggarwal, Dadush, and Stephens-Davidowitz (FOCS 2015) and control its error for adaptively chosen shifts. Finally, a martingale analysis applies the Aharonov--Regev Fourier distinguisher (JACM 2005) directly to the dependent output, avoiding the loss incurred by comparison with an independent product distribution. Our analysis applies to unstructured LWE with independent uniform public vectors. In particular, it does not directly apply to ML-KEM, whose security is based on the Module-LWE problem: the algebraic dependencies arising from its module structure are not covered by our analysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2261) | 2026-09-29
