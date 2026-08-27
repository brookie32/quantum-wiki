---
title: "High-Precision Lewis Weights via Fourth-Moment Control and Local Bregman Acceleration"
date: "2026-08-25"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1797"
summary: "We study the high-precision computation of ell_p-Lewis weights for pge4 in the black-box exact-real full-vector leverage-score oracle model, measuring complexity by the number of adaptive oracle round"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

We study the high-precision computation of ell_p-Lewis weights for pge4 in the black-box exact-real full-vector leverage-score oracle model, measuring complexity by the number of adaptive oracle rounds. In this model, Gribling, Sidford, and Zhang [GSZ26] obtained an O(p^2log(m/epsilon)) bound for computing an epsilon-estimate. We improve this bound to O(plog(mp)+sqrt plog(1/epsilon)). To obtain this result, we isolate the normalized fourth-moment operator governing the nonlinear Hessian of their log-determinant matrix potential and prove that each relative-gradient step with denominator p resets the operator norm to a universal constant. This reset controls the entire update segment and yields an O(plog(mp)) global entrance phase. After entering an O(1/p) spectral neighborhood of the optimum, we switch to a restarted accelerated Bregman-gradient method for the vector potential.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1797) | 2026-08-25
