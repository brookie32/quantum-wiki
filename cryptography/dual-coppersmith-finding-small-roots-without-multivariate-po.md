---
title: "Dual Coppersmith: Finding Small Roots Without Multivariate Polynomial Systems"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2740"
summary: "The multivariate Coppersmith algorithm is a central tool in public-key cryptanalysis for finding a small hidden root of modular polynomial equations. It consists of two stages. First, a lattice-reduct"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The multivariate Coppersmith algorithm is a central tool in public-key cryptanalysis for finding a small hidden root of modular polynomial equations. It consists of two stages. First, a lattice-reduction (LR) stage constructs auxiliary equations satisfied by the hidden root over mathbb Z. Second, a root-recovery (RR) stage solves these equations. The RR stage can be a bottleneck: auxiliary polynomials may not isolate the root, and solving them can take exponential time in the worst case, even when LR is feasible. We introduce Dual Coppersmith, which replaces algebraic root recovery with geometric recovery from a modular orthogonal lattice. Our construction embeds the hidden root as a short lattice vector, and we prove that LLL recovers its direction whenever a sufficient gap separates it from all independent lattice vectors. The root can then be recovered directly from coordinate ratios. To analyze this gap, we propose a heuristic model for the second successive minimum by examining both the full lattice and a structured sublattice. Under this model, Dual Coppersmith achieves the standard Coppersmith product-size bound without solving an auxiliary polynomial system. Experiments on the approximate common divisor (ACD) and Herrmann-May (HM) problems support the model's predictions and demonstrate root recovery in higher-dimensional instances where the Gröbner-based baseline reaches its timeout.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2740) | 2026-11-03
