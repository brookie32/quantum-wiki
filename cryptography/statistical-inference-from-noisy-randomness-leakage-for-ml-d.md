---
title: "Statistical Inference from Noisy Randomness Leakage for ML-DSA Attacks"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1712"
summary: "ML-DSA is a NIST post-quantum signature standard whose security argument rests on rejection sampling making released signatures independent of the secret key. Liu et al. and Damm et al. showed that a "
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

ML-DSA is a NIST post-quantum signature standard whose security argument rests on rejection sampling making released signatures independent of the secret key. Liu et al. and Damm et al. showed that a single leaked bit of the masking randomness per signature breaks this guarantee, making ML-DSA subkeys recoverable from a number of so-called informative relations, and the resulting attacks were sharpened by Schubert et al. and Bashiri et al.. All of them treat every leaked bit as equally trustworthy. We show that they need not. After the j-independence transformation introduced by al., the values extracted from a clean and from a flipped bit are exact complements in absolute value, so the observable relation |ilde z| follows a two-component mixture whose components we determine in closed form for all leakage regimes. This yields, first, a method-of-moments estimator for the bit-error rate p that requires only the informative relations an attack already collects and that, unlike the estimator of Schubert et al., also works in the low-leakage regime, down to leakage index 4 for ML-DSA-44 and ML-DSA-87 and 5 for ML-DSA-65, the same indices at which the attack itself remains feasible. However lower leakage indices come with a lower accuracy, at 25{,}000 informative relations the mean absolute error for the lowest cases is about 0.022 to 0.040 compared to values below 0.002 in the high-leakage regime. The noise estimator is also adjustable to estimate asymmetric noise rates. Second, it yields a posterior probability, for each individual relation, that its leaked bit is correct. Thresholding this posterior gives an O(alpha) preprocessing step that corrects relations classified as noisy and that any downstream attack can use unchanged, where alpha is the amount of informative relations. Applied to the attack of Schubert et al., the preprocessing reduces the number of informative relations required for key recovery by about 20% to 44% across all three parameter sets, leakage indices 6 to 9, and error rates 20% and 40%. Applied to the attack of Bashiri et al. for ML-DSA-44 at leakage index 8, it improves key recovery across the noise range we tested: at p = 0.45 from 1{,}900{,}000 informative relations, at p = 0.40 from 450{,}000 informative relations, at p = 0.20 from 40{,}000 informative relations, a single fixed threshold chosen in hindsight succeeds for 20, 22, and 23 of 30 seeds against 16, 18, and 19 of 30 without the preprocessing, and a parallel search over ten thresholds succeeds for 23, 25, and 29 of 30.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1712) | 2026-08-17
