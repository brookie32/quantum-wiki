---
title: "An Algebraic-Geometry Lower Bound against the ePrint:2026/1747 McEliece Key-Recovery Attack"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1810"
summary: "A few weeks ago, Ghoshal, Ishai, Jain, and Sun (ePrint:2026/1630) introduced a 'hold-out distinguisher' for the Goppa–McEliece public key. This past week, Vedenev (eprint:2026/1747) proposed to turn i"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

A few weeks ago, Ghoshal, Ishai, Jain, and Sun (ePrint:2026/1630) introduced a "hold-out distinguisher" for the Goppa–McEliece public key. This past week, Vedenev (eprint:2026/1747) proposed to turn its polynomial relations into key recovery by reconstructing the hidden generalized Reed–Solomon representation from nested Hasse-derivative spaces at held positions. Vedenev’s proposed held-position count explicitly assumes that the resulting linear equations are independent across positions. Yet, experiments on proper binary Goppa instances contradict that assumption, demonstrating a familiar "waterfall" phenomenon where - just before the required independent equation count for a successful attack - additional held positions sharply drop in value, providing just a single, independent equation rather than the approx {k hoose 2} such equations from the early positions. This note identifies an algebraic-geometric reason for this inherent dependence. For a binary Goppa polynomial of degree t, an explicit linear map constructs a (2t+3)-dimensional family modulo the true solution. At each held support point, the entire derivative-flag block restricts on this family to at most one ordinary evaluation condition. Consequently, under a concrete nondegeneracy condition stated in terms of the hidden vector polynomial f F and its formal derivative {f F}': c_{need} gt 2t + 3, where c_{need} is the number of sampled held positions required at the critical step in Vedenev’s algorithm. (The proposed key-recovery algorithm’s cost depends on c_{need} in the exponent.) For ISO/NIST Category 5 parameter set {sf mceliece8192128}, this gives c_{rm need} gt 259, which implies Vedenev’s key-recovery algorithm costs in excess of 2^{1500} bit operations there.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1810) | 2026-08-26
