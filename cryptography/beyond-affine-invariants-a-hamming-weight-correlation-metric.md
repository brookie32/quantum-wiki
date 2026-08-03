---
title: "Beyond Affine Invariants: A Hamming-Weight Correlation Metric for Template-CPA Leakage in Key-Dependent S-boxes"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1584"
summary: "Classical selection criteria for cryptographic S-boxes—nonlinearity NL, differential uniformity elta, boomerang uniformity eta_{B}, algebraic degree eg—are invariants of affine equivalence. That prope"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Classical selection criteria for cryptographic S-boxes—nonlinearity NL, differential uniformity elta, boomerang uniformity eta_{B}, algebraic degree eg—are invariants of affine equivalence. That property is exactly what blinds them to a class of side-channel weaknesses. The correlation-power-analysis (CPA) template distinguisher is governed by the Hamming-weight functional, and Hamming weight is not affine-invariant; it does not descend to the affine-equivalence quotient on which the classical criteria live. Two S-boxes with identical (NL,elta,eta_{B},eg) can therefore leak differently under template CPA. We make this precise for the key-dependent family S^{G}(x)=A,iota(x)oplus c, with iota the multiplicative inverse in GF(2^8) and (A,c)inGL(8,F_2)imesF_2^8 drawn from a byte stream G. A structural proposition fixes the four invariants at (112,4,6,7) across the entire family; they carry no information about G. We introduce the Hamming-weight template correlation rho_{HW}(dot,S_{AES}), identify it as the population statistic controlling the AES-template CPA distinguisher, and show that it resolves the fiber the classical invariants collapse. As a stress test we instantiate G with three sources of contrasting regularity—a system CSPRNG, a discretised logistic map, and a sin(1/x)/xxHash hybrid—and sample 3imes10^{5} S-boxes from a single master seed. The classical invariants are identical everywhere, as predicted. The metric is not. The logistic source widens the rho_{HW} distribution against S_{AES} by 12–13% (sigma_ell=0.0704 vs. 0.0626/0.0623; Levene p0.13), survives an exact Q1.31 fixed-point reimplementation at 3.1%, and does not appear for a tent-map control. Propagated through the Mangard–Oswald–Popp trace-budget model and checked against a 2.16imes10^{5}-attack Monte-Carlo CPA simulation, it yields a 29% relative excess in AES-template success rate at SNR=10, N=10^3 (empirical ratio 1.29, analytic 1.26). By every standard effect-size measure the widening is small (Cohen's d=0.128 on |rho_{HW}|, Cohen's h=0.130 on the attackable fraction); its significance is detectability, not magnitude. The contribution is a measurement axis, not a weak generator: a metric that flags template-CPA leakage where NL=112, elta=4 report perfect scores.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1584) | 2026-08-03
