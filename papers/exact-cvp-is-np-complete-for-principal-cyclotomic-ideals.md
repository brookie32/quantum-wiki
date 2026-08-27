---
title: "Exact CVP Is NP-Complete for Principal Cyclotomic Ideals"
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1793"
summary: "We prove that exact Euclidean decision-CVP is mathsf{NP}-complete on the coefficient lattices of nonzero principal ideals in the power-of-two cyclotomic rings R_d=Z[y]/(y^d+1). A deterministic reducti"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

We prove that exact Euclidean decision-CVP is mathsf{NP}-complete on the coefficient lattices of nonzero principal ideals in the power-of-two cyclotomic rings R_d=Z[y]/(y^d+1). A deterministic reduction from Exact Cover by 3-Sets (X3C) produces an integral target and an integer squared threshold Delta such that the closest squared distance is exactly Delta in YES instances and at least Delta+4 in NO instances. Moreover, the ideal elements whose squared distance from the target under the coefficient embedding is at most Delta are in bijection with the exact covers of the given X3C instance. This also gives mathsf{NP}-hardness of exact search-CVP under polynomial-time Turing reductions. We also transfer the resulting principal-ideal CVP instances to full-rank principal ideals of the cyclic quotient ring Z[X]/(X^D-1), where D=2d. Their coefficient lattices are invariant under a cyclic rotation by one coordinate. The lift preserves principality, doubles the dimension, and scales the squared distances of corresponding elements by eight. Thus, on principal cyclic ideal lattices, exact decision-CVP is mathsf{NP}-complete and exact search-CVP is mathsf{NP}-hard. The cyclotomic and cyclic hardness results also admit uniformly computable fixed-family forms. For each X3C universe size, one principal cyclotomic ideal and one principal cyclic ideal can be fixed before the collection of triples is known, and only the respective targets and squared thresholds depend on the collection. Thus exact decision-CVP remains mathsf{NP}-complete on both fixed families. If exact decision-CVP with preprocessing (CVPP) were solvable in polynomial time on either family, then mathsf{NP}subseteqmathsf{P}/poly. By the Karp--Lipton theorem, such a preprocessing scheme would collapse the polynomial hierarchy to Sigma_2^{mathsf{P}}. To our knowledge, the cyclic results resolve the exact decision versions of Micciancio's questions of whether CVP is mathsf{NP}-hard on cyclic lattices and on a fixed family of cyclic lattices, even under the stronger restriction to full-rank principal cyclic ideals.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1793) | 2026-08-24
