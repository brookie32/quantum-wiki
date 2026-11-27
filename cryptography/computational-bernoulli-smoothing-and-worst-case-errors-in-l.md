---
title: "Computational Bernoulli Smoothing and Worst-Case Errors in LPN Reductions"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3051"
summary: "Learning Parity with Noise (LPN) is a central problem in modern post-quantum cryptography. Recently, Aggarwal et al. (TCC 2026) proposed a new approach toward establishing worst-case foundations for t"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Learning Parity with Noise (LPN) is a central problem in modern post-quantum cryptography. Recently, Aggarwal et al. (TCC 2026) proposed a new approach toward establishing worst-case foundations for the hardness of LPN in the low-noise regime. Their reduction turns an average-case LPN solver into two algorithms such that, for every (worst-case) linear code, either one decodes noisy codewords of that code or the other distinguishes noisy codewords of its dual from uniform. Their main technique, computational code smoothing, relaxes a requirement of earlier reductions: noisy dual codewords need only be computationally pseudorandom, rather than statistically close to uniform. However, their result requires random Bernoulli errors for the decoding alternative (so only the code is worst case) and fixed-weight noise for the dual distinguishing alternative (rather than the more common Bernoulli noise). We remove both of these restrictions using a new analytical technique. As our main technical tool, we establish a computational Bernoulli perturbation bound for finite groups, which may be of independent interest. We show that if multiplying a random group element from some distribution D by a fixed element with probability eta<1/2 produces an arepsilon-pseudorandom distribution, then D itself is arepsilon/(1-2eta)-pseudorandom. This bound is tight. As a result, for Bernoulli-weighted sums in abelian groups, we show that revealing any k coefficients increases the distinguishing advantage by at most a factor of (1-2eta)^{-k}. This can be viewed as the computational generalization of the Bernoulli smoothing technique of Yu and Zhang (CRYPTO 2021).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3051) | 2026-11-25
