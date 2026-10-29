---
title: "Faster complete formulas and their application to curves with efficient endomorphisms"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2667"
summary: "We revisit scalar multiplication on prime curves y^2 = x^3 + b with p equiv 1 pmod 3, the family including secp256k1, BN, and BLS curves. We apply a 15-year-old technique in a novel way to improve the"
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

We revisit scalar multiplication on prime curves y^2 = x^3 + b with p equiv 1 pmod 3, the family including secp256k1, BN, and BLS curves. We apply a 15-year-old technique in a novel way to improve the best complete addition from 12 to 11 multiplications (or 10 for mixed coordinates) for the first time in 10 years: its final stage is a 3D cross product, which needs only five multiplications. We implement the new formulas on the exttt{libsecp256k1} library, with an improvement of 5.2% in constant-time fixed-base scalar multiplication. Furthermore, we propose a complete tripling formula with the same cost as incomplete tripling in Jacobian coordinates, and combine both formulas into an exception-free width-3 au-NAF with au = 1 - omega and a six-point precomputed table. In an operation-count model it is about 14% faster than exception-free GLV-based scalar multiplication at 256 bits and 3--7% faster than the fastest incomplete GLV. A constant-time implementation in RELIC confirms the model on the BLS families: in G_1 of BLS12-381, BLS24-509 and BLS48-575 the au-NAF is 9--13% faster than GLV with the same complete formulas, and the regular variant is 10--12% faster than regular GLV with complete formulas and 5--9% faster than regular GLV with incomplete Jacobian formulas. In G_2 of the same curves, where GLS gives the baseline, the au-NAF stays 10--11% faster than GLS with complete formulas and 7--9% faster with Jacobian formulas, while the regular variant gains at most 6%. We also develop an `imaginary' version of Toom-Cook that is useful for the G_T extension field arithmetic, yielding a 4--6% improvement in G_T exponentiation for BLS24-509 and BLS48-575. A cyclotomic cube at 0.77 multiplications carries the au-adic method over to G_T, where it makes exponentiation 3% faster on BLS24-509 and 11% faster on BLS48-575.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2667) | 2026-10-28
