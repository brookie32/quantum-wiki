---
title: "Sub-Cubic Homomorphic Matrix Multiplication]{Sub-Cubic Homomorphic Matrix Multiplication via Self-Dual Normal Bases"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1592"
summary: "This paper analyzes the bilinear embedding of matrix algebras into commutative cyclotomic rings. We apply the Cohn-Umans method. This establishes that single-multiplication bilinear monomial embedding"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

This paper analyzes the bilinear embedding of matrix algebras into commutative cyclotomic rings. We apply the Cohn-Umans method. This establishes that single-multiplication bilinear monomial embeddings require a ring degree of widetilde{Omega}(N^3). We circumvent this bound by routing Strassen tensor rank decompositions through orthogonal Chinese Remainder Theorem ideals. This reduces the asymptotic complexity to widetilde{Omega}(N^{log_2 7}). We optimize the coprime tensor decomposition. Embedding the inner tensor into the maximal real subfield satisfies the Lempel-Weinberger parity constraint. This guarantees the existence of a Self-Dual Normal Basis, reducing the required basis generators to a single element and mathematically halving the homomorphic trace depth. Canonical integer polynomial lifts ensure uniform norm bounds. Type I Optimal Normal Bases bound the trace dual expansions to an O(1) constant. By invoking Kronecker's theorem, we prove that the polynomial power basis minimizes the canonical expansion for the non-evaluated tensor components. A towered evaluation over composite degrees controls noise propagation. This decouples key-switching errors into a logarithmic bound. We generalize the embedding to Galois rings via Hensel's and Nakayama's lemmas to support high-precision integer arithmetic. Furthermore, we extend the architecture to boundless matrices exceeding the fixed ring capacity via a multi-ciphertext block-Strassen decomposition. By deferring the homomorphic trace operator to post-Strassen recombination, we completely eliminate homomorphic basis-switching, achieving an asymptotic complexity of O(N^{log_2 7 - 1/rho}) multiplications and widetilde{O}(N^{2 - 2/(rho log_2 7)}) automorphisms for matrices of arbitrary dimension. Empirical benchmarks over the BGV scheme validate the approach. A multi-threaded towered trace evaluates 32 imes 32 matrices in 141.3 milliseconds at a security level of lambda=148 using one ciphertext-ciphertext multiplication. We achieve a speedup factor of 2.49 over multi-threaded baselines.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1592) | 2026-08-03
