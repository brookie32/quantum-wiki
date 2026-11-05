---
title: "Refined Bounds for the Smoothing Parameter of Lattices"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2756"
summary: "The smoothing parameter eta_arepsilon(Lambda) is a fundamental invariant in lattice-based cryptography. Zheng, Zhao, and Xu (AAECC 2021) proved eta_arepsilon(Z) le sqrt{ln(frac{2}{arepsilon} + frac{ar"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The smoothing parameter eta_arepsilon(Lambda) is a fundamental invariant in lattice-based cryptography. Zheng, Zhao, and Xu (AAECC 2021) proved eta_arepsilon(Z) le sqrt{ln(frac{2}{arepsilon} + frac{arepsilon}{44})/pi} and eta_arepsilon(Lambda) le sqrt{ln(n - 1 + frac{2n}{arepsilon})/pi},bl(Lambda). Guo, Liu, Wang, and Tian (PLOS One 2025) proposed eta_arepsilon(Z) le sqrt{ln(frac{2}{arepsilon} + frac{arepsilon}{m})/pi} for 0 frac{arepsilon^2}{4}, our bound is strictly tighter for all admissible (arepsilon, m), improving the worst-case gap from O(arepsilon^2) to O(arepsilon^6). Second, for all n ge 2 and 0 < arepsilon < min{1, (rho(Z)-1)n}, [ eta_arepsilon(Lambda) le sqrt{frac{ln!left(frac{2}{elta_n} + frac{elta_n^2}{4}right)}{pi}},bl(Lambda) < sqrt{frac{ln!left(frac{2n}{arepsilon} + (n - 1) - frac{(n^2 - 1)arepsilon}{6n(1 + arepsilon)}right)}{pi}},bl(Lambda), ] where elta_n = (1+arepsilon)^{1/n} - 1; the rational bound is strictly tighter than Guo et al.'s across 100% of their validity window, while remaining valid as arepsilon o 0^+. Third, for any basis mathbf{B} with Gram--Schmidt vectors mathbf{b}_i^* and M = max_i |mathbf{b}_i^*|, define N_arepsilon(mathbf{B}) = sum_{i=1}^n (arepsilon/2)^{M^2/|mathbf{b}_i^*|^2 - 1} in [1, n]; then [ eta_arepsilon(Lambda) le sqrt{ln!left(frac{2}{elta_{eff}} + frac{elta_{eff}^2}{4}right)/pi},M, ] where elta_{eff} = frac{n}{N_arepsilon(mathbf{B})}((1+arepsilon)^{1/n}-1). For reduced bases with geometrically decaying Gram--Schmidt lengths, N_arepsilon(mathbf{B}) = O(1) is independent of n, eliminating the O(n) factor inside the logarithm.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2756) | 2026-11-04
