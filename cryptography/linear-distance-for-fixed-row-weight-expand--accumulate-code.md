---
title: "Linear Distance for Fixed-Row-Weight Expand--Accumulate Codes over Arbitrary Fields"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1753"
summary: "Expand–accumulate (EA) codes are sparse linear codes underlying constructions of correlated pseudorandomness and field-agnostic succinct arguments. In “Field-Agnostic SNARKs from Expand–Accumulate Cod"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Expand–accumulate (EA) codes are sparse linear codes underlying constructions of correlated pseudorandomness and field-agnostic succinct arguments. In “Field-Agnostic SNARKs from Expand–Accumulate Codes” (CRYPTO 2024), Block et al. conjectured that a single fixed-row-weight EA component already achieves constant relative distance with inverse-polynomial failure probability. We prove this conjecture in a stronger, field-uniform form. For every rate Rin(0,1), there exists elta_R>0 such that, for every target exponent C>0, one can choose gamma=gamma(R,C)>0 for which the fixed-row ensemble with t=lceilgammalog Nrceil satisfies [ P!left[ min_{xinF_q^{lfloor RNrfloor}setminus{0}} operatorname{wt}(xEA) le elta_R N right] le N^{-C} ] for all sufficiently large N. The same constants work for every prime power q; in particular, the field may vary arbitrarily with the block length. Thus, a single fixed-row-weight EA component is asymptotically good over all finite fields, and its polynomial reliability exponent can be made arbitrarily large by increasing the row-weight constant. The proof separates sparse and high-weight messages. Sparse messages are handled through expansion and a compact analysis of accumulator cancellations, while high-weight messages are controlled by a surplus of linear constraints over large fields and a stochastic accumulator analysis over bounded fields. A terminal-boundary obstruction shows that, for t=Theta(log N), inverse-polynomial failure is qualitatively optimal.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1753) | 2026-08-20
