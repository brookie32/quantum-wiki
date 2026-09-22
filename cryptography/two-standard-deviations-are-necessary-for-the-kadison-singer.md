---
title: "Two Standard Deviations Are Necessary for the Kadison-Singer Problem"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2123"
summary: "Let C_0 be the least constant such that, for every finite family of vectors u_1,ldots,u_ninmathbb C^d and independent finitely supported real random variables xi_i, there are values arepsilon_iinopera"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Let C_0 be the least constant such that, for every finite family of vectors u_1,ldots,u_ninmathbb C^d and independent finitely supported real random variables xi_i, there are values arepsilon_iinoperatorname{supp}(xi_i) satisfying |sum_{i=1}^n(arepsilon_i-E[xi_i])u_i u_i^*| leq C_0|sum_{i=1}^nVar[xi_i](u_i u_i^*)^2|^{1/2}, where |dot| denotes the operator norm. This rank-one matrix discrepancy formulation generalizes the signing formulation of the Kadison--Singer problem [KS59], resolved by Marcus, Spielman, and Srivastava [MSS15b]. Let C_1 be the least constant such that, for every epsilon>0 and every finite family in mathbb C^d, in every dimension d, satisfying sum_{i=1}^n u_i u_i^*=I and max_{iin[n]}|u_i|^2leqepsilon, there are signs arepsilon_1,ldots,arepsilon_nin{-1,1} such that |sum_{i=1}^narepsilon_i u_i u_i^*|leq C_1sqrtepsilon. Taking the xi_i to be independent symmetric signs gives C_1leq C_0, since |sum_{i=1}^n(u_i u_i^*)^2|leqepsilon under these hypotheses. The general formulation allows arbitrary finite real supports and does not require sum_{i=1}^n u_i u_i^*=I. Kyng, Luh, and Song [KLS20] proved C_0leq4. We prove 2leq C_1leq C_0leq2.176. This improves the bounds sqrt2leq C_0leq3 of Xie, Xu, and Zhu [XXZ21]. We conjecture that the optimal constant is C_0=2.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2123) | 2026-09-20
