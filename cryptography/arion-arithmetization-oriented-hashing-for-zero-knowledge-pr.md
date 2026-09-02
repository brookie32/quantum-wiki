---
title: "Arion: Arithmetization-Oriented Hashing for Zero-Knowledge Proof Systems"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1842"
summary: "We propose the arithmetization-oriented (AO) hash function Arion, following a permutation-based design approach. We first define the permutation Arion-π over the finite field F_p, where (p > 2) is pri"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

We propose the arithmetization-oriented (AO) hash function Arion, following a permutation-based design approach. We first define the permutation Arion-π over the finite field F_p, where (p > 2) is prime. The design of Arion-π is based on the recently introduced generalized triangular polynomial system, a novel algebraic framework for constructing cryptographic permutations using polynomials over finite fields. Using this permutation, we define the hash function Arion in two modes: the well-established Sponge construction and a feed-forward truncation mode (Trunc). Secure parameter sets are specified for prime fields commonly used in zero-knowledge proof applications, including the scalar fields of the BLS12-381 and BN254 elliptic curves. We provide an extensive security analysis of Arion, with particular emphasis on algebraic techniques — including interpolation and polynomial system solving (PoSSo) based techniques, such as Gröbner basis computations, and resultants — which are especially relevant for cryptographic primitives defined over prime fields. To the best of our knowledge, Arion is the first hash function whose security analysis is explicitly based on the algebraic invariant of the underlying ideal - the quotient ring dimension. In particular, we explicitly determine the dimension of the quotient ring associated with the CICO problem induced by the hashing modes. Furthermore, our analysis of the CICO-t problem applies to any t ≥ 1 and covers both the Sponge and feed-forward constructions. We evaluate the efficiency of Arion across several arithmetization frameworks — R1CS, Plonk, and AIR — and compare it with prominent AO hash functions, including Poseidon, Poseidon2, Anemoi, Griffin, and Rescue. Our results show that Arion is frequently the best-performing design in the Plonk setting and remains highly competitive, often ranking second, in both RoneCS and AIR. In terms of native performance, Arion is the only construction based on high-degree power maps that achieves performance comparable to Poseidon/Poseidon2. This makes it an attractive choice for applications where both zero-knowledge proving efficiency and native evaluation costs are important considerations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1842) | 2026-08-31
