---
title: "Which Pairs Belong Together? An Optimization Approach to Pair Selection in F_4"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3048"
summary: "The security of multivariate public key cryptosystems (MPKC) relies in part on the hardness of the Multivariate Quadratic (MQ) problem, which consists in finding a solution to a system of quadratic eq"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The security of multivariate public key cryptosystems (MPKC) relies in part on the hardness of the Multivariate Quadratic (MQ) problem, which consists in finding a solution to a system of quadratic equations over a finite field. One of the main approaches to solving such systems is to compute a Gröbner basis, which is often done with Faugère's F_4 algorithm. In each iteration, F_4 selects a set of critical pairs to reduce, and the selection strategy strongly affects its performance. The standard approach, the normal strategy, selects pairs by degree alone. In this work, we introduce two features of critical pairs, novelty and column growth, and use them to formulate pair selection as a weighted quadratic unconstrained binary optimization (QUBO) problem. By studying different weightings, we find that penalizing novel pairs and strongly weighting column growth reduces the computation time of F_4, excluding the cost of selection, by a median factor of about 1.5, at the cost of a far more expensive selection step. Based on these findings, we design the coverage strategy that keeps the two features but replaces the optimization by a sequential rule with a budget derived from the expected number of new head terms. Experiments on weakly overdetermined MQ instances over F_{31} with 11 to 16 equations show that the coverage strategy reduces the total computation time, including selection, by 35% to 67% compared to the normal strategy, without additional memory, and that this improvement grows with the size of the system.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3048) | 2026-11-25
