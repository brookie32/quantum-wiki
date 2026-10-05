---
title: "Bitwise-Optimal Cryptography: From One-Wayness to Pseudorandomness and Target Collision Resistance"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2335"
summary: "We study cryptographic primitives that are both locally computable (i.e., in NC^0) and exponentially secure. For pseudorandom generators (PRGs) and universal one-way hash functions (UOWHFs), we furthe"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We study cryptographic primitives that are both locally computable (i.e., in NC^0) and exponentially secure. For pseudorandom generators (PRGs) and universal one-way hash functions (UOWHFs), we further require linear stretch and linear compression, respectively, which is essentially the best one can hope for in this setting. Such primitives simultaneously achieve an extreme level of security and efficiency: each output bit inspects only a constant number of input bits, while each input bit buys a constant amount of security and expansion/shrinkage, in an amortized sense. We refer to such primitives as bitwise optimal. We prove that bitwise-optimal PRGs and UOWHFs can be obtained from any exponentially secure one-way function (OWF) in NC^0, thereby establishing an equivalence between these three primitives in the bitwise-optimal regime. Notably, an analogous equivalence is not known in the exponential-security regime for general, unrestricted cryptographic primitives without imposing an additional regularity condition. Our results combine the machinery of the author (Applebaum, FOCS'17) with new structural results on locally computable functions that may be of independent interest. We prove a sparsification theorem that reduces the output length of any exponentially secure local OWF to O(n) while preserving exponential hardness, an input-locality reduction that bounds the number of outputs affected by each input bit, and a structural theorem showing that functions with bounded input locality are typically almost regular. Together, these ingredients remove the regularity assumption required by previous constructions and yield a non-black-box transformation from exponentially secure OWFs in NC^0 to bitwise-optimal PRGs and UOWHFs. As an additional contribution, we prove a projection-based compression theorem for locally samplable sources.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2335) | 2026-10-04
