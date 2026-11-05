---
title: "Tight Depth Lower Bounds for Stretch Amplification"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2728"
summary: "We investigate the depth overhead of stretch-amplification for pseudorandom generators in the black-box model. We show that any black box construction of a PRG H: {0,1}^m o {0,1}^M which makes poly(n)"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

We investigate the depth overhead of stretch-amplification for pseudorandom generators in the black-box model. We show that any black box construction of a PRG H: {0,1}^m o {0,1}^M which makes poly(n) queries to a PRG G: {0,1}^n o {0,1}^N in d adaptive phases during each evaluation (and with a black-box reduction to the security of G) must satisfy: M leq (m + O(log n)) Bigl( frac{N}{n - O(log n)} Bigr)^d. This implies that the standard amplification procedure [GM'84, GGM'86] based on repeated composition of G is essentially optimal. In particular, amplifying n mapsto n+1 to m mapsto 2m requires depth overhead d = Omega(frac{n}{log n}), and amplifying n mapsto 2n to m mapsto m^2 requires depth overhead d = Omega(log n); each of these bounds is tight up to a constant factor. As an immediate corollary we obtain tight lower bounds on the depth complexity of black-box constructions of PRFs from PRGs. Both of these problems (pertaining to amplification and PRF construction) have been studied in various prior works [V'05, MV'11, BJP'11, MV'15, BMM'24, ADV'26]. Despite progress on special cases in which the structure of the reductions is constrained, it was previously unknown whether completely parallel constructions (d=1) existed in every stretch regime. The kinds of amplification procedures we investigate have more recently found use outside of cryptography in the study of range avoidance ("Avoid") [K'21]. We show an analogous result in this setting: any black-box FP^{NP} reduction from an Avoid instance G: {0,1}^n o {0,1}^N to a second Avoid instance H: {0,1}^m o {0,1}^M which has "depth d" in the above sense must satisfy the same bound relating n,N,m,M,d. Using this impossibility result for Avoid, we construct an oracle relative to which E notsubseteq NC/poly but E^{NP} subseteq P/poly. Our oracle separation implies that in the relativized setting, the bounded arithmetic theory S^1_2 cannot prove the existence of functions outside P/poly, even given as an axiom the existence of functions outside NC/poly.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2728) | 2026-11-03
