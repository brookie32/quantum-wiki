---
title: "CycloSPDZ: Efficient MPC over 2-Power Cyclotomic Rings mod (2^k) for Dishonest Majority"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2972"
summary: "Most multi-party computation (MPC) protocols support arithmetic over finite fields or integer rings. Polynomial arithmetic in applications such as convolution evaluation and distributed key generation"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Most multi-party computation (MPC) protocols support arithmetic over finite fields or integer rings. Polynomial arithmetic in applications such as convolution evaluation and distributed key generation motivates extending these protocols to the 2-power cyclotomic rings R_k=Z_{2^k}[X]/(X^N+1), where N is a power of two. However, no native protocol is known for actively secure computation over these rings with a dishonest majority. In this work, we present an information-theoretic MAC that is homomorphic over R_k and requires only a small increase in coefficient bit length. We apply this to construct CycloSPDZ, an actively secure MPC protocol for a dishonest majority in the preprocessing model that has efficiency comparable to the state-of-the-art field-based convolution protocols in Convolutions in Overdrive (PoPETs 2023). We also construct an efficient preprocessing protocol from authenticated integer-ring triples by adapting Toom–4 multiplication to power-of-two moduli via scaled interpolation and batched exact division, and combining it with Karatsuba multiplication in a hybrid scheme. As an application, we evaluate convolution workloads using polynomial encoding and blocking. We implement and benchmark the online phase of CycloSPDZ against our hybrid variant of SPDZ_{2^k} (CRYPTO 2018) and the function-dependent variant of the Matrix Rings (ASIACRYPT 2024), achieving speedups of up to 5imes and 48imes, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2972) | 2026-11-21
