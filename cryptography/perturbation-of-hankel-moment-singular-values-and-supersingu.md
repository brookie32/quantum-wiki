---
title: "Perturbation of Hankel moment singular values and supersingular endomorphism rings via CVP: a p-adic super-resolution law and a fully computed pipeline"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1586"
summary: "We give two rigorous results in post-quantum algebra with a p-adic strengthening and a complete reproducible pipeline. Part I proves an explicit sufficient noise bound under which the Hankel matrix of"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

We give two rigorous results in post-quantum algebra with a p-adic strengthening and a complete reproducible pipeline. Part I proves an explicit sufficient noise bound under which the Hankel matrix of the power moments of supersingular j-invariants deterministically recovers the nodes, with the propagation constant written through the Vandermonde condition number (Weyl, Bauer-Fike); non-archimedeanly, the Teichmüller lift makes the Vandermonde matrix unimodular (cond_p = 1 for every L) and an exact super-resolution law gives the p-adic precision loss as 2sum_{i<j} v_p(x_i - x_j) + sum_i v_p(c_i), a sharp analogue of Moitra's bound. Part II reduces a Z-basis of End(E) to a rank-4 CVP and recovers the exact Gram matrix of the norm form in poly(log p) time via Weil-pairing discrete logs (Shor; in the smooth regime actually run, the logs are classical Pohlig-Hellman), after which fixed-dimension LLL yields a canonical basis and a lambda_1-criterion reads the node type. Both parts are joined by an end-to-end theorem and fully computed on real numbers: node recovery, real Vélu chains with measured degree, deterministic KLPT construction with the ideal-to-isogeny and smoothing steps, reading the torsion action in F_{p^4} and via Weil pairing + Pohlig-Hellman without an O(N) table, true LLL + Fincke-Pohst, and the classification of all three nodes of B_{23,infty}. The last KLPT heuristic (polynomial running time) is replaced by an explicit hypothesis PRH and a conditional theorem; PRH is shown to be exactly a Titchmarsh-type shifted-prime divisor sum with positive singular series, provable under GRH for fixed p, with uniformity in p an identified open problem. Companion code (23 modules) verifies every numerical claim.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1586) | 2026-08-03
