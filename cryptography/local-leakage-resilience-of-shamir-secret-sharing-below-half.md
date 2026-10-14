---
title: "Local Leakage Resilience of Shamir Secret Sharing: Below Half Threshold Rate"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2454"
summary: "We study the local leakage resilience of Shamir secret sharing, where an adversary leaks a bounded number of bits from every share. For n parties and reconstruction threshold k over a prime field F_p "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

We study the local leakage resilience of Shamir secret sharing, where an adversary leaks a bounded number of bits from every share. For n parties and reconstruction threshold k over a prime field F_p with p>n, we prove the following. (1) There is an absolute constant c_{bh}0 and kge cn, Shamir sharing is resilient to quadratic-residue leakage and to almost all local leakage functions of up to eta_clog_2 p bits, for a constant eta_c>0. All three results follow from one analytic framework, which we develop for generalized Reed--Solomon codes: local leakage from a uniform codeword is statistically close to the same leakage from independent uniform field elements. The framework expresses the leakage distance as the norm of a function on the leakage outputs. The Efron--Stein decomposition splits this function into orthogonal components indexed by supports of dual codewords. Two tools bound the components: list recovery of the dual code, which is ordinary list decoding for one-bit leakage, and a generalized von Neumann inequality for MDS systems of linear forms that retains linearly many Gowers norms. The first tool gives the result above half, the second gives the constant-rate result, and applying both to different ranges of supports in the same decomposition gives the result below half.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2454) | 2026-10-12
