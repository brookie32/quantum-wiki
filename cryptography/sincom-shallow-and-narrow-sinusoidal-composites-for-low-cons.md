---
title: "SinCom: Shallow-and-Narrow Sinusoidal Composites for Low  Constant-Round Secure Evaluation of Activation Functions"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3004"
summary: "Non-linear activations remain the bottleneck in privacy-preserving machine learning: secure comparison is expensive, polynomial approximation needs many multiplication rounds, and the nested-sine cons"
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

Non-linear activations remain the bottleneck in privacy-preserving machine learning: secure comparison is expensive, polynomial approximation needs many multiplication rounds, and the nested-sine construction of CRAfT is strictly serial---round count grows with depth, with no parallel ``width'' in which to buy accuracy. We start from an asymmetry that holds across secure-computation back-ends---depth is expensive, width is free---and ask for the shallowest, narrowest composite that still reaches high accuracy. The result is extsf{SinCom}: a layered composite of MPC-friendly operators with depth Din{2,3} and per-layer width Win{2,3,4,5}, joined by cross-channel weight matrices, whose round complexity equals~D independently of~W. Frequency is learned per layer rather than prescribed. Unbounded activations must be split before they can be approximated. We single out a component that is bounded and smooth and let the exact remainder be a branch-free skeleton, f=xdot h(x); on softplus the split is instead the half-slope form f=frac{x}{2}+E(x) with E~even, and the optimizer places the skeleton coefficient at c=frac12 on its own, beating the classical c=1 by up to 22.7imes. Neither form is universal, so the outcome is a selection rule, not a single recipe. At six sines the composite fits GELU to 1.4imes10^{-6}, SiLU to 6.0imes10^{-6} and mish to 1.2imes10^{-5} (24-bit, [-8,8]); on CRAfT's own domain [-3,3] with four sines it reaches 3.30imes10^{-7} on Phi against CRAfT's 1.62imes10^{-4}, a 245imes improvement like for like. All figures are function-level: the error of the composite in exact arithmetic, excluding what a distributed realization adds (Sref{sec:errmodel}). Parameters are public constants fitted offline, so a deployment ships the best of many fits at no online cost---which is why we report best-of-N.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3004) | 2026-11-23
