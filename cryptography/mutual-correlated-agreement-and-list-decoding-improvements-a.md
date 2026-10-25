---
title: "Mutual Correlated Agreement and List-Decoding: Improvements and Separations"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2617"
summary: "At a high level our contribution is threefold: we improve the quantitative MCA error bound for polynomial generators, we prove a refinement of the implication from list-decodability to MCA, and we cla"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

At a high level our contribution is threefold: we improve the quantitative MCA error bound for polynomial generators, we prove a refinement of the implication from list-decodability to MCA, and we clarify that in general, these two notions are distinct. We show that, for every finite field F, every nonempty seed set SsubseteqF, every linear code C subseteq F^{n} of relative minimum distance elta_{C} and every degree d geq 1, the univariate powers generator G_{d}(x) := (1,x,ots,x^{d}) has mutual correlated agreement for C at relative proximity parameter gamma with error O(dmax{1,ngamma}/|S|) below the smaller of the unique decoding radius and the generalized Johnson radius J_{d+2}(elta_{C}) := 1-(1-elta_{C})^{1/(d+2)}, with a one-coordinate margin below the latter when it is smaller. Then, we show that list-decodability at radius p with list size L implies MCA slightly above 1-sqrt{1-p} (the improvement on the radius is dependent on the list size). The previous state-of-the-art result of Gao, Cai, Xu and Kan showed that list-decodability at radius p 1/2 cannot hold for all linear codes C under the sole hypothesis that C is (p,L)-list-decodable. Similarly, for any distance 0<elta<1 and any 1-sqrt{1-elta}<p<gamma<1, there exists a family of linear codes with fixed positive rate and relative distance tending to elta such that |F|epsilon_{mathsf{MCA}}(gamma)leq poly(n) but the list size at radius p is n^{omega(1)}. Both counterexample families exist over fields of any characteristic. Both MCA errors are for the line generator.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2617) | 2026-10-23
