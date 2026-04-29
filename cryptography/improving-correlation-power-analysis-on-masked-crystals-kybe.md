---
title: "Improving Correlation Power Analysis on Masked CRYSTALS-Kyber with Lattice Attack"
date: "2026-04-27"
updated: "2026-04-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/820"
summary: "Tosun and Savas (IEEE TIFS'23) proposed a non-profiling power analysis attack on masked ML-KEM, or CRYSTALS-Kyber. Their attack can recover a full secret key of Kyber with 7,000 power traces. Later, T"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

Tosun and Savas (IEEE TIFS'23) proposed a non-profiling power analysis attack on masked ML-KEM, or CRYSTALS-Kyber. Their attack can recover a full secret key of Kyber with 7,000 power traces. Later, Tosun et al. (IEEE Access'24) claimed an improvement over the previous attack with only 550 traces, but the result is not convincing. In particular, their attack does not seem to recover a full secret key of masked Kyber; instead, it recovers only the absolute values for every coefficient of a secret key. Unfortunately, Tosun et al. did not provide convincing and efficient ways to recover the signs of every secret coefficient. In this paper, we show that 400 traces are sufficient to recover a full secret key of masked Kyber. This improvement is arguably significant, as the number of traces is only about 5% of a previous full key recovery attack by Tosun and Savas. The key technique for improvement is the use of a lattice embedding method. So far, there have been several known attacks that use Kannan's embedding method to reduce the number of traces for recovering a full secret key of Kyber. Specifically, these attacks recover only a partial secret key through power analysis attack and recover the remaining part by applying the embedding method. In contrast, we use not only recovered partial secret key but also recovered absolute values to recover the remaining part. For this purpose, we utilize an unusual embedding method that is a combination of Kannan's embedding and Bai-Galbraith's embedding. Our technique can also be applied to other post-quantum cryptosystems that use NTT-based multiplication. We demonstrate the applicability of our method to the first-order masking implementations of NTT-based variants of SABER and Dilithium, achieving full key recovery with 150 and 1,000 traces, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/820) | 2026-04-27
