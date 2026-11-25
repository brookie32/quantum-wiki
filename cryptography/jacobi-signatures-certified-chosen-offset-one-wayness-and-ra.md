---
title: "Jacobi Signatures: Certified Chosen-Offset One-Wayness and Random-Offset Collision Resistance"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3006"
summary: "Jacobi signatures are publicly computable vectors of quadratic characters whose security has primarily been studied for fixed consecutive offsets. We investigate two public-offset models under Balance"
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

Jacobi signatures are publicly computable vectors of quadratic characters whose security has primarily been studied for fixed consecutive offsets. We investigate two public-offset models under Balanced Repeated-Factor Factoring for honestly generated moduli N = p^2q. First, we construct a total and compressing family on the full fixed-length Boolean domain and prove certified chosen-offset one-wayness. After observing N, the adversary may choose any publicly certified offset tuple, possibly with correlated coordinates, and retain state before a fresh uniform challenge is sampled. We establish a mean-fiber bound uniformly over all certified tuples and combine it with conditional-probability analysis and CRT/gcd factor extraction, obtaining a quadratic inversion-to-factoring reduction with polynomial loss. Second, we construct a compressing family on canonical legal residues using independently sampled offsets. We state a shifted-Legendre separation bound in the legal-domain form needed by our reduction and combine it with the Jacobi/CRT collision-to-factoring mechanism to obtain collision resistance with negligible additive loss, without an additional Legendre-signature uniqueness conjecture. We further extend the construction to a total compressing family on a full fixed-length Boolean domain.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3006) | 2026-11-23
