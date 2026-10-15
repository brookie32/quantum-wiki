---
title: "Speeding up Sumcheck using Algebraic Geometry"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2494"
summary: "The sumcheck protocol, a ubiquitous component of modern proof-systems, enables proving the sum of evaluations of a low-degree multivariate polynomial. In theory, sumcheck has been generalized from pol"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

The sumcheck protocol, a ubiquitous component of modern proof-systems, enables proving the sum of evaluations of a low-degree multivariate polynomial. In theory, sumcheck has been generalized from polynomials to (tensors of) any multiplication code, a code whose pointwise products of codewords lie in a related product code. All practical systems nonetheless specifically use polynomials. For proof-systems over binary fields that target Boolean circuits, this choice has a real cost: the product of two binary messages under Reed--Solomon is no longer binary. As a result, the prover's work in the first, and most expensive, round of sumcheck (the so-called univariate skip) grows by a logarithmic factor. We present a new concrete multiplication code based on algebraic geometry that is binary-preserving: the product of two encoded binary messages is again a binary message. Specifically, we construct an explicit multiplication code over F_{2^{128}} that carries 64-bit messages to binary product messages of length 222, and whose product code has relative distance greater than 1-2^{-119}. The part of the product message that the prover actually sends in sumcheck is more than 3 imes smaller than with Reed--Solomon, as used in practice. The code comes from a genus-95 curve over F_2 with 64 rational points, built as a (Z/2)^3 Artin--Schreier cover of a genus-4 curve. We implemented the resulting protocol, which we call the AG skip, inside the Flock proof-system. For 2^{32} constraints, it speeds up the skip round by 2.36imes and the whole zerocheck, which was the prover's most expensive component, by 1.65imes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2494) | 2026-10-15
