---
title: "Cryptanalysis of the Alternative Mod-2/Mod-3 Weak PRF"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1982"
summary: "The alternative mod-2/mod-3 function is one of the most widely used weak PRF constructions in modern cryptographic protocols. Despite its practical importance, its security has received relatively lim"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The alternative mod-2/mod-3 function is one of the most widely used weak PRF constructions in modern cryptographic protocols. Despite its practical importance, its security has received relatively limited attention, with the main cryptanalytic results consisting of two distinguishing attacks due respectively to Cheon et al. and Johansson et al. In this work, we revisit the cryptanalysis of this primitive by analyzing the output distribution of the weak PRF under fixed Hamming weights for both the secret key and the inputs. This refined analysis allows us to isolate and amplify statistical biases that were averaged out in previous works. Using this approach, we derive a new distinguishing attack with asymptotic data and time complexity mathcal O(2^{0.099n}). We implemented the attack for the original parameter set n=384, thereby obtaining the first practical attack against this instance of the construction. We then introduce a generic technique, called the splitting strategy, which consists in partially fixing or guessing part of the secret key in order to amplify the biases while introducing an additional computational cost that can be efficiently handled using Fast Fourier Transform-like techniques. This leads to the currently best known attack against the construction, with asymptotic data, time, and memory complexities widetilde{mathcal O}(2^{0.09n}). This last technique also provides a useful time-memory trade-off for estimating the security of real-world constructions when the available data is bounded: we show that the weak PRF offers less than 128-bit security for n = 510 when the data is limited to 2^{45}. Finally, we revisit the attack of Johansson et al. and provide a corrected and refined analysis of the underlying bias, showing that the statistical behavior of the attack differs significantly once the Hamming weight of the secret key is taken into account. This new analysis explains phenomena previously observed experimentally but left unexplained. Thanks to this approach we are able to identify a large class of keys for which the attack performs much better asymptotically than anticipated by Johansson et al.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1982) | 2026-09-11
