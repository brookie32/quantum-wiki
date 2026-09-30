---
title: "Affine-Padding Rabin-Oracle Factoring in L_n!left(frac{1}{3},sqrt[3]{frac{32}{9}}right)"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2256"
summary: "The 2007 algorithm of Joux, Naccache, and Thomé (JNT) shows that, with subexponential access to an e-th root oracle, one can forge RSA signatures for odd e in time close to the special number field si"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The 2007 algorithm of Joux, Naccache, and Thomé (JNT) shows that, with subexponential access to an e-th root oracle, one can forge RSA signatures for odd e in time close to the special number field sieve, without factoring the modulus; a recent JNT implementation by Shea et al. carried that attack to 1024-bit RSA. We revisit the JNT construction at e=2, the Rabin case, where an e-th root oracle is a square-root oracle. A raw square-root oracle factors n=pq in one query, so it is of no interest; the interesting object is a redundancy-constrained (affine-padded) Rabin oracle that returns a single canonical root and thereby resists the one-query attack. We show that a one-sided number field sieve against such an oracle produces a congruence of squares X^2equiv Y^2pmod n with Xnotequivpm Y with probability 1/2 per dependency, and hence factors n in special-number-field-sieve time [ L_n(1/3,sqrt[3]{32/9})simeq L_n(1/3,1.526ldots), ] strictly below the general number field sieve's [ L_n(1/3,sqrt[3]{64/9})simeq L_n(1/3,1.923ldots).] The mechanism is a pleasant inversion: the sign ambiguity that the odd-e algorithm must suppress becomes, at e=2, the very quantity that leaks the factorization. We give the algorithm in full --- LLL polynomial selection for a quadratic field, a line sieve producing prime-ideal relations, quadratic characters, mathbb F_2 linear algebra, and an exact number-field square root --- prove the half-rate splitting, and analyse the complexity, including the precise reason the attack collapses when the padding is a hash rather than an affine function of an attacker-chosen message. A small toy example run of it, from the padded modulus to the recovered factors, is given in Appendix A. A measurement campaign on larger moduli is currently running and will be reported as updates to this ePrint.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2256) | 2026-09-29
