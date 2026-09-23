---
title: "Cryptanalysis of Goldreich's PRGs with MAJ–XOR Predicates"
date: "2026-09-22"
updated: "2026-09-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2156"
summary: "Goldreich's pseudorandom generators (PRGs) expand a secret seed by evaluating a fixed low-locality predicate on random subsets of its bits. We study the concrete and asymptotic security of constructio"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

Goldreich's pseudorandom generators (PRGs) expand a secret seed by evaluating a fixed low-locality predicate on random subsets of its bits. We study the concrete and asymptotic security of constructions whose local predicate combines majority with XOR. We introduce Deterministic Pooled Recovery (DPR), which guesses a set of seed positions and pools the outputs whose majority inputs are forced by the guess. The selected outputs yield noiseless sparse linear equations. For the proposed (operatorname{MAJ}_7oplusoperatorname{XOR}_4) challenge published in ToSC 2025, with seed length (n=1024) and output length (m=n^2), DPR has an estimated recovery cost of (2^{109.71}) operations using (omega=2.38) for the linear-algebra exponent. This is below the claimed 128-bit security level. We also refine the common-bias analysis by evaluating its advantage at each fixed seed weight. This viewpoint motivates Bias-Amplified Pooled Recovery (BAPR), which uses partial majority bias to construct pooled noisy linear systems. For (m=n^s) with fixed (s>1), odd majority locality (ainomega(1)ap O(log n)), and fixed XOR locality (bge3), we prove that BAPR admits a worst-case (2^{o(n)})-time implementation that recovers any fixed seed with high probability. This rules out exponential security in this intermediate-locality regime. In addition, we identify exploitable affine structure and residue constraints in proposed alternative predicates.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2156) | 2026-09-22
