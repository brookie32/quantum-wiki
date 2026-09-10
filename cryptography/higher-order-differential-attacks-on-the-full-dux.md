---
title: "Higher-order differential attacks on the full DuX"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1907"
summary: "DuX is a family of substitution-permutation block ciphers over F_q^{16} with qin{2^{8},2^{16},65537} and twelve rounds. For the two large-word instances its designers estimate that integral and higher"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

DuX is a family of substitution-permutation block ciphers over F_q^{16} with qin{2^{8},2^{16},65537} and twelve rounds. For the two large-word instances its designers estimate that integral and higher-order differential distinguishers in the encryption direction reach at most six rounds, and fix the number of rounds accordingly. We bound the word-wise algebraic degree of DuX by exponent sets in the decryption direction, where the decryption S-box has coordinate degrees (2,3,4,2) against the (5,3,2,8) of the encryption S-box. Each row of the inverse diffusion matrix is supported on two residue classes of word indices modulo four. An active set equal to one class therefore keeps the vector of degree bounds constant within each class at every layer, and we prove that the four class-wise bounds then obey an exact recursion with base 2+sqrt{3} instead of four. This yields higher-order differential distinguishers for eleven rounds of DuX(2^{16}) and DuX(65537) with q^{4} chosen ciphertexts, and for seven rounds of DuX(2^{8}) with 2^{88}. Extending one round towards the plaintext gives three successive systems of equations. Every unknown there has a coefficient computed from the returned plaintext words, and the key words recovered at one stage are substituted into the next; for DuX(65537) the last two systems are replaced by bivariate interpolation. Once each system attains the maximal rank that its structure permits, a condition that can be checked during the attack, solving the systems recovers all sixteen master-key words of the full twelve-round DuX(2^{16}) and DuX(65537). The data and time complexity is 2^{67.32} and 2^{67.58} with constant memory, and eight rounds of DuX(2^{8}) are covered with 2^{91.32}. The two diffusion layers differ by a rotation of four words, so the analysis is the same for each of the 2^{11} key-dependent choices of diffusion layers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1907) | 2026-09-07
