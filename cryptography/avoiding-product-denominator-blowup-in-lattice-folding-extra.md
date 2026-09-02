---
title: "Avoiding Product-Denominator Blowup in Lattice-Folding Extraction"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1841"
summary: "Coordinate-wise extraction in lattice folding naturally produces source openings normalized by challenge differences, while an inconsistency branch must ultimately yield a short integral SIS relation."
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Coordinate-wise extraction in lattice folding naturally produces source openings normalized by challenge differences, while an inconsistency branch must ultimately yield a short integral SIS relation. Branchwise polynomial integralization converts each extracted tuple under one common multiplier before comparing the tuples; this collects the local challenge slacks into a global product and can push the resulting relation outside the useful shortness regime. We retain each local normalization until the two extracted tuples are compared. The resulting integral kernel relation depends only on local slack factors. In the sequential interactive setting, we realize this comparison by synchronizing two successful coordinate stars at the same numerical folding challenge. The remaining difficulty is probabilistic: the common challenge is inherited from a successful execution and is therefore success-biased. Acceptance-weighted shared-root synchronization gives additive raw extraction loss and linear unconditional expected retry-invocation complexity. For a Cyclo-compatible instantiation, this changes the concrete extraction regime. At arity two, the coefficient radii for local comparison and branchwise integralization have base-two logarithms 25.04 and 49.63, respectively, while the coefficientwise centered-modulus threshold is about 49. We also instantiate the required short unit-difference challenge interface and give a one-fold classical-ROM compilation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1841) | 2026-08-31
