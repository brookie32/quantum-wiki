---
title: "Quasar: A Field-Agnostic Polynomial Commitment Scheme with Polylogarithmic Verification from Quasi-Abelian Codes"
date: "2026-08-31"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1839"
summary: "Polynomial commitment schemes (PCSs) are fundamental building blocks of modern zkSNARKs and often dominate their concrete prover and verifier costs. We introduce mathsf{Quasar}, a field-agnostic PCS f"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Polynomial commitment schemes (PCSs) are fundamental building blocks of modern zkSNARKs and often dominate their concrete prover and verifier costs. We introduce mathsf{Quasar}, a field-agnostic PCS for multilinear polynomials that combines Quasi-Abelian (QA) codes with BaseFold (Zeilberger et al., CRYPTO 2024) through code switching (Ron-Zewi and Rothblum, JACM 2024). For a polynomial of length N and security parameter lambda, mathsf{Quasar} achieves concretely fast O(Nlog N) commitment, O(N) evaluation time, and O(lambdalog^2 N) proof size and verifier time. Our starting point is a recent work of Li et al. (CRYPTO 2026), which shows that QA codes have fast encoding and strong concrete distance. This opens the door to building efficient PCSs from QA codes via Brakedown's paradigm (Golovnev et al., CRYPTO 2023). However, a direct instantiation, called QAPCS, inherits square-root proof size and verifier time, falling short of practical efficiency when N is as large as 2^{25}. We overcome this crucial limitation by showing that QA codes are essentially code-switchable. In contrast to existing code-switching arguments that utilize algebraic structures of either generator matrices or parity-check matrices, we look into QA encoding algorithms and propose an efficient encoding-oriented argument. Consequently, mathsf{Quasar} simultaneously enjoys fast proving from QAPCS, and polylogarithmic verification of BaseFold. We implement mathsf{Quasar} over the 127-bit Mersenne prime field with rate 1/2 and 100-bit security. Under the 32-thread CPU setting, mathsf{Quasar} accelerates commitment and evaluation over BaseFold by 13.6imes--20.6imes and 5.2imes--63.8imes, respectively. It is also 2.2imes--6.0imes faster in commitment than Brakedown and 2.1imes--4.0imes faster in commitment and 17.4imes--237.6imes faster in evaluation than BrakingBase, while providing smaller proofs and faster verification than both. Compared with QAPCS, it achieves up to 4.3imes faster verification and 2.9imes smaller proofs. Moreover, we observe that QA encoding naturally exposes massive parallelism, enabling a GPU acceleration strategy that is not directly available to the other code families. Across message lengths from 2^{12} to 2^{25}, the GPU encoder is 32.9imes--148.3imes faster than the 32-thread CPU implementation. Over polynomial sizes 2^{20}--2^{29}, the commitment with GPU acceleration further achieve a 3.4imes--16.7imes speedup relative to its 32-thread CPU implementation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1839) | 2026-08-31
