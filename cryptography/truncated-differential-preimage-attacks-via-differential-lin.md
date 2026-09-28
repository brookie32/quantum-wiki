---
title: "Truncated Differential Preimage Attacks via Differential-Linear Correlations"
date: "2026-09-27"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2231"
summary: "We derive joint truncated differential (TD) probabilities from multiple differential-linear (DL) approximations and use them in a framework for preimage filtering. For a fixed input difference, the in"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

We derive joint truncated differential (TD) probabilities from multiple differential-linear (DL) approximations and use them in a framework for preimage filtering. For a fixed input difference, the inverse Walsh transform recovers the probabilities of affine output cosets from DL correlations over a complete mask subspace. In our applications, these correlations are estimated using the round-based DL method. A filter accepts a selected union of affine cosets, whose probability is computed from their joint distribution without assuming independence among the DL events. The framework handles multiple targets, sharing base evaluations and confirming each accepted candidate only once. An independent sampling analysis allows candidate sets from different iterations to overlap and relates success probability to confirmation cost. Applying this framework, we obtain the first preimage attacks on KNOT-Hash below the designers' claimed preimage bounds, for 9 to 12 rounds. For all four JH members, we obtain preimage attacks on the reduced-round hash functions under the padding rule of the specification, covering 3 rounds per compression-function call forJH-224/256/384 and 4 rounds for JH-512, with speedups ranging from 2^{54} to 2^{158} over generic preimage search. For reduced-round SKINNY-Hash, we also present the first second-preimage attacks on target messages containing at least two padded blocks, covering 5 and 6 rounds of SKINNY-tk2-Hash and 5, 6, and 7 rounds of SKINNY-tk3-Hash. As a further application of the DL-to-TD construction, we give a 6-round TD distinguisher on Xoodoo/Xoodyak in the related-key setting, whose estimated sample complexity improves on the previous best by about 25 bits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2231) | 2026-09-27
