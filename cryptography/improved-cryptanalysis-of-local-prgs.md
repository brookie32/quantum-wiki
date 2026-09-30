---
title: "Improved Cryptanalysis of Local PRGs"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2240"
summary: "We present two seed-recovery attacks on a family of local PRGs, which map an n-bit random seed to an m-bit pseudorandom string by applying XorMaj predicates. For PRGs with large locality, we extend th"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

We present two seed-recovery attacks on a family of local PRGs, which map an n-bit random seed to an m-bit pseudorandom string by applying XorMaj predicates. For PRGs with large locality, we extend the Group-and-Solve (GAS, Eurocrypt 26) framework to Guess-Filter-Solve (GFS). GFS first guesses that a set of seed bits are all 1s and then filters for outputs whose inputs to Maj contain a sufficiently large subset of the guessed bits. Then high-bias noisy equations can be collected for the correct guess and solved by specific solvers. Compared with GAS, GFS collects substantially more noisy equations with high bias and hence outperforms GAS significantly, especially when the output is short. For example, for the challenge parameter n=256 and m=2^{16} (STOC 16), the complexity for GFS is 2^{68.78} while it is 2^{157.91} for GAS. In addition, the asymptotic complexity of GFS is 2^{0.15n+o(n)}. Independently, inspired by the Guess-and-Decode (GADec, TIT 22), we propose the Filter-Guess-Propagate (FGP) attack. Compared with GADec, FGP introduces two speed-up techniques at each iteration of Belief Propagation (BP): a filter scheme to reduce the number of equations and a dynamic-programming technique to update the log-likelihood ratios of variables efficiently. Together, these improvements enable FGP to perform fast BP and outperform GADec significantly. For XorMaj_{10,64} with n=256 and m=2^{40} (Eurocrypt 24), the total complexity of FGP is 2^{52.66}, whereas even a single BP iteration of GADec costs 2^{106.42}. FGP is further applied to a ZKP protocol from Eurocrypt~25 and QuietOT from Asiacrypt~24, with only a small computational overhead. For the ZKP protocol, FGP leads to an attack on witness indistinguishability, while for QuietOT, it similarly yields an attack on OT receiver privacy.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2240) | 2026-09-28
