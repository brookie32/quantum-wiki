---
title: "Reverse Substitution in Secret Sharing: The Critical One-Half Threshold and a Route to Superpolynomial Lower Bounds"
date: "2026-10-26"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2652"
summary: "The contribution vector (convec) of a secret-sharing scheme is the vector of its normalized share sizes. The average and maximum coordinates of a convec give, respectively, the average and maximum inf"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

The contribution vector (convec) of a secret-sharing scheme is the vector of its normalized share sizes. The average and maximum coordinates of a convec give, respectively, the average and maximum information ratios of the scheme. Obtaining superlinear lower bounds on these quantities for unrestricted perfect secret sharing has remained a challenging open problem for about four decades. In this paper, we study substitution, a natural way to build complicated access structures from simpler ones: one participant of an outer access structure is replaced by an inner access structure. Given secret-sharing schemes for the two factors, the standard forward construction composes them into a scheme for the composite access structure. We study the converse question. Given an arbitrary scheme for the composite access structure, we ask to what extent its convec admits a reverse factorization into convecs for the outer and inner factors, up to a common multiplicative loss. Exact reversal is false: we give a counterexample whose optimal reverse factor is (8/9), with a composite scheme that is scalar-linear over every finite field. On the positive side, we prove that a factor (1/2) is always attainable, and that every fixed instance admits a strictly larger factor. For a recursive family built from Csirmaz’s classical access structure (mathcal C_k), whose distinguished set has size (k), we identify a critical reverse factor that determines when the resulting lower bound becomes superlinear. This critical factor exceeds one half by only an amount of order ((log k)/k). Crossing it yields superlinear lower bounds, while any fixed positive excess above one half gives a route to superpolynomial lower bounds. Using only Shannon inequalities, the corresponding recursive factor cannot cross the critical value. Thus any improvement sufficient to pass this threshold must exploit constraints beyond the Shannon inequalities.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2652) | 2026-10-26
