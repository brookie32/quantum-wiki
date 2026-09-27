---
title: "Linear Key Recovery in the BAG-Loong Reference Implementation"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2223"
summary: "The BAG-Loong reference implementation samples its secret matrices X and Y from fixed, publicly known subspaces, although the specification calls for secret random supports. This makes the public-key "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

The BAG-Loong reference implementation samples its secret matrices X and Y from fixed, publicly known subspaces, although the specification calls for secret random supports. This makes the public-key relation S = HX + Y , with public H, amenable to Gaussian elimination. Expanding the relation over F2 and projecting away the support of Y leaves a linear system for X. We prove an exact recovery criterion based on its column rank. All 40 supplied known-answer-test records, covering four parameter sets, satisfy this criterion: two independent solvers recover each X exactly, and the unmodified decapsulation code reproduces the corresponding session keys. For the largest parameter set, the reduced system has 9360 equations in 728 unknowns per column; one elimination solves all 15 columns.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2223) | 2026-09-26
