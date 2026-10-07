---
title: "The Geometry of Witness-Update Tradeoffs in Additive Positive Accumulators"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "industry"
tags: [industry, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2362"
summary: "An additive positive accumulator represents a growing set by a short public digest. Each inserted element has a membership witness, which may have to be refreshed after later insertions. An execution "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

An additive positive accumulator represents a growing set by a short public digest. Each inserted element has a membership witness, which may have to be refreshed after later insertions. An execution of n insertions therefore defines a labeled update vector d=(d_1,ldots,d_n), where d_i is the number of strict post-insertion refreshes of the witness created at time i. Previous lower bounds concern scalar quantities such as max_i d_i and sum_i d_i. Even when both are known, they do not determine how the updates are distributed among the labeled witnesses. Let mathcal T_w([n]) be the set of left-depth vectors of inorder binary trees on [n] whose right-depth is less than w, and define the convex upward region [ mathcal G_w^{(n)}:=operatorname{conv}(mathcal T_w([n]))+mathbb R_{ge0}^n. ] Our main result constrains the entire expected update vector. For polynomial-time update specifications, let m=Theta(1+L/loglambda), where L bounds the accumulator length. For every fixed elta>0 and all sufficiently large lambda, [ mathbb E[d]in(1-elta)frac{m}{m-1}mathcal G_{m-1}^{(n)}. ] Equivalently, there is one distribution Pi_{lambda,elta} over feasible trees such that [ mathbb E[d_i]ge(1-elta)frac{m}{m-1}mathbb E_{TleftarrowPi_{lambda,elta}}[ell_T(i)] qquadext{for every }i. ] Thus the same tree distribution constrains all labeled coordinates. The region mathcal G_w^{(n)} is characterized by its nonnegative linear inequalities. If [ V_w(a):=min_{T:,max_irho_T(i)<w}sum_i a_iell_T(i), ] then xin cmathcal G_w^{(n)} exactly when adot xge cV_w(a) for every age0. For arbitrary history-dependent update specifications, we establish the corresponding inequality for every predetermined efficiently computable nonnegative weight vector a: [ mathbb E!left[sum_i a_i d_iright]ge(1-o(1))frac{m}{m-1}V_{m-1}(a), ] together with a corresponding lower-tail bound. Indicator vectors give position-independent cohort bounds; in particular, every predetermined cohort of size k has benchmark at least (k-m+1)_+ up to the same factor. The combinatorial basis of these results is that the temporal-blocking vectors used in replay attacks and the vectors in mathcal T_w([n]) have the same upward closure. To transfer this characterization to accumulator executions, we use fractional tuple packing, interval rounding, and conditional resampling controlled by the L-bit accumulator state. For the vector theorem, a separating direction is computed from independent executions before the replay attack is applied to a fresh execution. At fixed width, the same tree vectors describe the coordinatewise lower boundary of online-merger update profiles. Every feasible tree vector is realized by an online merger and, through the standard Merkle-forest construction, by an additive positive accumulator.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2362) | 2026-10-05
