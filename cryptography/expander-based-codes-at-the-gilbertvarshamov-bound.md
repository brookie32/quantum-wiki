---
title: "Expander-Based Codes at the Gilbert–Varshamov Bound"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2315"
summary: "We prove that Expand--Accumulate (EA) codes approach the Gilbert--Varshamov (GV) distance as the code length grows. The result holds over the binary field and every fixed finite field. At fixed rate, "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We prove that Expand--Accumulate (EA) codes approach the Gilbert--Varshamov (GV) distance as the code length grows. The result holds over the binary field and every fixed finite field. At fixed rate, encoding uses O(nlog n) expected field operations, with a tunable inverse-polynomial probability of sampling a bad code. Fixed-memory wrapped binary Expand--Convolute (EC) codes satisfy the same guarantee. Allowing O(nlog^2 n) expected field operations makes sampling failure negligible in the code length. These codes combine a sparse random linear map with an invertible recursive map. Our analysis uses exact input--output weight enumerators in place of the earlier concentration bounds. It also gives tighter constants in the logarithmic expected degree. For EA-based pseudorandom correlation functions, these bounds improve the degree--distance tradeoff that controls local evaluation cost. Separately, we obtain finite-length bounds at small degrees by replacing independent incidence with regional regularity. At rate one half, a two-sided regular EC ensemble with left/right degrees 10/5 and memory 15 reaches 99.99% of the binary GV distance. The probability of sampling a generator below this distance is less than 2^{-32.49}. We extend the construction to finite fields using independent nonzero edge labels and full-field convolution coefficients. These coefficients mix field components; scalar extension of a binary matrix does not. Over F_{2^{128}}, degrees 24/12 with memory 5 reach 98.41% of the rate-one-half GV distance with sampling failure below 2^{-45.03}; degrees 26/13 with memory 4 reach the same distance with failure below 2^{-135.20}. Every finite claim is certified with outward-rounded interval arithmetic. The results concern minimum distance of sampled ensembles; they do not provide a decoder or a complete protocol-security proof.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2315) | 2026-10-02
