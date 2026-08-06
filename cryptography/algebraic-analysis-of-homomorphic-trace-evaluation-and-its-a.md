---
title: "Algebraic Analysis of Homomorphic Trace Evaluation and Its Applications"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1604"
summary: "Field trace evaluation has emerged as a powerful tool in fully homomorphic encryption, with broad applications ranging from bootstrapping algorithms to privacy-preserving protocols. Recent advances ha"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Field trace evaluation has emerged as a powerful tool in fully homomorphic encryption, with broad applications ranging from bootstrapping algorithms to privacy-preserving protocols. Recent advances have significantly reduced its noise growth by combining tower-based evaluation strategies with rescaling operations. However, existing analyses rely on uniform noise bounds that fail to capture the actual noise behavior across different coefficients, leading to substantial gaps between theoretical estimates and empirical observations. In this work, we present a refined algebraic analysis of trace evaluation over power-of-two cyclotomics that uncovers structured cancellation effects among noise coefficients induced by subsequent linear operators, in particular the trace mappings of subextensions. We show that, except for the constant term, the variance of each output noise coefficient depends on the 2-adic valuation of its index, yielding bounds that improve upon prior uniform estimates by a factor of O(log n) both for non-constant coefficients and after a subsequent plaintext-ciphertext multiplication, where n is the ring degree. We further extend our analysis to two typical algorithmic applications of trace evaluation. For ciphertext packing, we derive a non-recursive formulation that admits a cleaner structure and slightly tighter noise estimates. For coefficient extraction, our coefficient-wise analysis improves upon prior uniform variance bounds by factors ranging from Theta(n) to Theta(n^2) for non-constant coefficients and by a factor of O(n) after post-multiplication. Experimental results confirm that the observed noise variances follow the coefficient-wise pattern predicted by our analysis and demonstrate pronounced improvements over existing estimates, providing effective guidance for parameter selection and system configuration in practice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1604) | 2026-08-04
