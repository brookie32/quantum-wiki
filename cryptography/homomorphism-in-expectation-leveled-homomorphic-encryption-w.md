---
title: "Homomorphism in Expectation: Leveled Homomorphic Encryption with Range-Relative Correctness"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2854"
summary: "Lattices have dominated the development of homomorphic encryption for deep computation. We introduce extit{Homomorphism in Expectation (HIE)}, a new construction showing that encrypted addition suffic"
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

Lattices have dominated the development of homomorphic encryption for deep computation. We introduce extit{Homomorphism in Expectation (HIE)}, a new construction showing that encrypted addition suffices for both addition and multiplication in deep real-valued computation. Given any additively homomorphic encryption scheme over Z_2, we construct range-relatively correct leveled homomorphic encryption for arithmetic circuits C of extit{arbitrary} polynomial depth. For depth bound d and any chosen public input bound r>0, our scheme supports inputs in [-r,r]. Outputs lie in [-eta_C,eta_C], where eta_C=C(r,ldots,r) is the circuit's maximum output range magnitude over this input range. Decryption returns an answer with error at most arepsilondoteta_C except with probability elta. Each input requires ell_{mathsf{in}}=O(d+log(1/arepsilon)) base ciphertexts, and each output requires ell_{mathsf{out}}=O(arepsilon^{-2}log(1/elta)) base ciphertexts. For n inputs, online evaluation uses only {sim}ell_{mathsf{out}}dot ndotell_{mathsf{in}} ciphertext additions and {sim}ell_{mathsf{out}}dot |C|dotell_{mathsf{in}} memory accesses. Our construction begins by encoding real-valued inputs as encrypted bitstreams, allowing multiplication through encrypted bit addition. The direct approach incurs costs exponential in circuit depth, limiting efficient evaluation to logarithmic depth and requiring non-compact input ciphertexts. We overcome these limitations with new encoding and circuit evaluation techniques, which eliminate the exponential overhead, enabling compact homomorphic arithmetic at arbitrary polynomial depth from additive encryption alone.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2854) | 2026-11-10
