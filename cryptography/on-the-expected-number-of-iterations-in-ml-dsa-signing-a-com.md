---
title: "On the Expected Number of Iterations in ML-DSA Signing: A Complete Accounting of the Rejection Conditions"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2456"
summary: "FIPS 204 Table 1 gives the expected number of iterations of the ML-DSA signing loop (ML-DSA.Sign_internal, Algorithm 7), citing CRYSTALS-Dilithium Equation (5). That equation covers only the validity "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

FIPS 204 Table 1 gives the expected number of iterations of the ML-DSA signing loop (ML-DSA.Sign_internal, Algorithm 7), citing CRYSTALS-Dilithium Equation (5). That equation covers only the validity checks on line 23 (lVert z rVert_infty and lVert r_0 rVert_infty) and omits the two encoding-correctness checks on line 28 (lVert c dot t_0 rVert_infty and the hint weight), a scoping distinction the Dilithium specification states explicitly and FIPS 204 does not reproduce. We give a complete accounting of all four conditions. The z check on line 23 is computed exactly by counting; the c dot t_0 term follows a closed-form Irwin-Hall tail, restating a peer-reviewed result by Yan, Luo and Wang; the hint-weight term's per-coefficient probability, conditioned on line 23 having passed, does have a closed form, but the tail of the sum over 256k such coefficients does not, since their probabilities are unequal, random, and correlated with each other, so we give the conditioned per-coefficient probability in closed form and estimate its tail by Monte Carlo. The corrected expected iteration counts are 4.36, 5.14 and 3.91 for ML-DSA-44, -65 and -87, matching a real end-to-end measurement to within 0.14% and already reflected in NIST's own errata to FIPS 204.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2456) | 2026-10-12
