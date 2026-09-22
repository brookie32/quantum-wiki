---
title: "Post-Quantum PKE and More from a Noisy Unstructured Linear Algebraic Assumption: Beyond LWE and LPN"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2113"
summary: "Noisy linear algebraic assumptions (NLAs), such as mathsf{LWE} and Alekhnovich’s mathsf{LPN}, have long served as the most reliable sources of post-quantum hardness. However, a series of recent classi"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Noisy linear algebraic assumptions (NLAs), such as mathsf{LWE} and Alekhnovich’s mathsf{LPN}, have long served as the most reliable sources of post-quantum hardness. However, a series of recent classical attacks on assumptions once believed to be quantum-secure, coupled with the rapid progress in quantum technology, underscores the urgent need for assumptions that are plausibly hard even if both mathsf{LWE} and mathsf{LPN} turn out to be broken. A fascinating recent work of Ghosal et al. (Eurocrypt 2025) takes an important first step in this direction, constructing a PKE scheme by combining two NLAs that remain plausibly secure even if mathsf{LWE} and Alekhnovich’s parameter regime for mathsf{LPN} were to be polynomially broken. A critical weakness of their work, however, is that it is still mathsf{LPN}-broken: namely, an oracle that breaks mathsf{LPN} with n^{-elta} noise rate can break their NLA, for some elta>0. We ask: can this barrier be overcome? We answer this question positively, by introducing an NLA that is plausibly hard given an oracle that breaks even constant noise rate mathsf{LPN}, while still being plausibly hard given an oracle that breaks mathsf{LWE}. Along the way, we improve upon the work of Ghosal et al. significantly in several dimensions. Specifically, we introduce a single new natural NLA and provide constructions of (i) public-key encryption and (ii) two-round maliciously secure oblivious transfer protocol from this single assumption. We also construct a one-time circular-secure secret-key encryption from a binary variant of this assumption. Our assumption takes the form (mathbf{A}, mathbf{A}mathbf{s} + mathbf{e}), where mathbf{A} is a random unstructured square matrix, the secret mathbf{s} has short and sparse entries, and the error mathbf{e} is a mixture of two components: a small-but-dense error combined with a large-but-sparse error. We provide a comprehensive initial cryptanalysis, ruling out (1) efficient combinatorial attacks that exploit sparsity such as information set decoding, (2) dimension reduction attacks, and (3) dual lattice attacks. We also prove, via a reduction, that our assumption, and its binary variant, is at-least as hard as mathsf{LWE}. Additionally, we show that for a broad range of parameters including those used by our constructions, our assumption does not appear to fall within the class of “lattice” assumptions, that is, there seems to be no reduction to approximate shortest vector problem solvers, and, crucially, it is plausibly hard even given an oracle that breaks mathsf{LPN} for any noise density parameter.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2113) | 2026-09-19
