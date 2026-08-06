---
title: "Budget Allocation in Neural Differential Distinguishers"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1595"
summary: "Neural differential distinguishers are usually compared at a fixed number of labeled samples. However, different input representations may require different numbers of ciphertexts per sample, making f"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Neural differential distinguishers are usually compared at a fixed number of labeled samples. However, different input representations may require different numbers of ciphertexts per sample, making fixed-sample comparisons potentially misleading from a cryptanalytic data-complexity perspective. In this paper, we study neural differential distinguishers under a fixed ciphertext budget. We ask whether the available encryption queries should be spent on more independent plaintext bases, or on richer samples containing more ciphertext-difference rows. We introduce a shared-base multi-difference representation in which several input differences are applied around the same plaintext base, and compare it with the standard single-difference baseline and an independent-pair control representation. Experiments on GIFT-64, PRESENT-64, RECTANGLE-64, and SPECK-64/128 show that the single-difference baseline is rarely the best fixed-budget allocation. Adding more difference rows often improves the distinguisher even though it reduces the number of independent training samples. At the same time, the optimal number of rows is not universal: logistic regression often benefits from larger representations, while a multilayer perceptron frequently prefers intermediate values due to sample-starvation and overfitting. We further test several non-adaptive difference sets and observe that the main trend is not tied to a single hand-picked set. The results suggest that the number of differences per sample should be treated as an explicit design parameter in neural differential cryptanalysis, and that fixed-budget evaluation is necessary for comparing richer neural distinguisher inputs fairly.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1595) | 2026-08-04
