---
title: "Faster Post-Quantum zkSNARK Provers Using the LCH Polynomial Basis"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1784"
summary: "Univariate-polynomial interactive oracle proofs (IOPs) over binary extension fields F_{2^m} underpin a class of plausibly post-quantum zkSNARKs, but rely heavily on polynomial arithmetic, where large-"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Univariate-polynomial interactive oracle proofs (IOPs) over binary extension fields F_{2^m} underpin a class of plausibly post-quantum zkSNARKs, but rely heavily on polynomial arithmetic, where large-domain evaluation and division by subspace vanishing polynomials are the dominant prover costs. General-basis additive FFTs, such as Gao--Mateer and Lin-Chung-Han (LCH), accelerate the evaluation but impose a basis-conversion stage costing O(n (log n)^2) field additions and O(n log n) field multiplications that dominates in practice. To eliminate basis conversion entirely, we introduce a divide-and-conquer algorithm for polynomial division by vanishing polynomials that operates directly in the LCH polynomial basis, for arbitrary F_2-basis elements, achieving optimal O(n log n) complexity. In the LCH polynomial basis, multiplying a vanishing polynomial by the random blinding polynomial reduces to appending random field elements, eliminating the multiplication entirely. We integrate native LCH-basis arithmetic and auxiliary optimizations across all phases of the Aurora IOP. Benchmarks on Preon (a NIST PQC Round-1 signature scheme candidate built on Aurora) show end-to-end signing speedups of 5.0imes for Preon-128A and 5.8imes for Preon-256C, with the polynomial transform alone 12.6--17.9imes faster.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1784) | 2026-08-23
