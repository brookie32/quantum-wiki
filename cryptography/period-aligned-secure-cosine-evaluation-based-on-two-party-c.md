---
title: "Period-Aligned Secure Cosine Evaluation Based on Two-Party Computation"
date: "2026-09-18"
updated: "2026-09-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2079"
summary: "The cosine function is widely used in machine-learning applications, but evaluating it on secret-shared data is difficult. Conventional approaches use polynomial approximations or lookup tables, whose"
last_verified: "2026-09-20"
review_by: "2026-12-19"
stale: false
---

The cosine function is widely used in machine-learning applications, but evaluating it on secret-shared data is difficult. Conventional approaches use polynomial approximations or lookup tables, whose costs grow substantially over large input domains. More recent protocols first reduce the private input modulo the cosine period, but securely performing this modular reduction also incurs significant cost. We present a period-aligned two-party cosine protocol. Based on the cosine addition rule, it rescales each share so that a wrap of the input modulus corresponds to a full 2pi period and therefore does not change the recombined cosine. Each party evaluates sine and cosine locally on its share, while the secure computation uses only two cross-party products and one fixed-point output conversion. We evaluate the protocol directly on synthetic inputs and within private RFF-based RBF-SVM prediction. Comparisons with the protocol of Xing et al. (NDSS 2025) and Guo et al. (USENIX Security 2026) demonstrate better efficiency of our proposed protocol.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2079) | 2026-09-18
