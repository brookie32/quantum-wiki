---
title: "Cryptanalysis of MinRank 2.0"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2733"
summary: "MinRank is an NP-complete problem underlying the security of several post-quantum schemes. It is the hardness assumption of the NIST second-round signature candidate Mirath and of the encryption schem"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

MinRank is an NP-complete problem underlying the security of several post-quantum schemes. It is the hardness assumption of the NIST second-round signature candidate Mirath and of the encryption schemes of Chatterjee et al. and Debris-Alazard et al. at Eurocrypt 2026. Moreover, it is ubiquitous in the cryptanalysis of multivariate schemes, among them the third-round candidates UOV, MAYO, QR-UOV, and SNOVA. In this work, we revisit the attacks on MinRank. On the combinatorial side, we improve the polynomial part of the kernel-search attack by sharing its linear algebra across guesses, which lowers its cost by 3 to 6 bits on the Mirath parameters and the Courtois challenges, and by up to 3 bits in combination with the hybrid approach. With the improved attack, we solved Courtois challenge~D, open since 2001: an instance over F_2 with 19 imes 19 matrices, 81 unknowns, and target rank 10, solved in 11434 CPU days, an estimated 2^{61} bit opetations. Our multi-threaded C++ code is publicly available. On the algebraic side, we show that the complexity of the Kipnis--Shamir (KS) attack is less understood than the literature suggests: the existing estimates rely on a generic Hilbert series that does not predict the rank of the Macaulay matrices of the KS equations. We prove a lower bound on the corank that explains the discrepancy, show that the attack requires a reduced instance with k leq m - r, and derive corrected complexity estimates, which are 1 to 24 bits above the best other attack on every Mirath parameter set. We also extend the Support-Minors and Minors modelings with the field equations, which lowers their estimates over small fields: for q = 2 and m = n = 22, by 9 to 205 bits for Support-Minors and by 17 to 278 bits for Minors. The rank predictions behind the algebraic estimates are stated as assumptions and verified experimentally.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2733) | 2026-11-03
