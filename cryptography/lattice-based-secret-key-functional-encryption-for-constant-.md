---
title: "Lattice-based Secret-Key Functional Encryption for Constant-Degree Polynomials"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1977"
summary: "We present a lattice-based construction of secret-key functional encryption (FE) for low-norm polynomials of any constant degree d, hence also for mathsf{NC}^{0} circuits. We rely on two core ingredie"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We present a lattice-based construction of secret-key functional encryption (FE) for low-norm polynomials of any constant degree d, hence also for mathsf{NC}^{0} circuits. We rely on two core ingredients: 1. New trapdoor and preimage sampling algorithms for certain degree-d tensor-structured matrices, used to generate functional secret keys. 2. A new k-LWE-style assumption where short preimages of non-zero images with respect to the above tensor-structured matrix are given as hints, under which we prove that our secret-key FE scheme is selectively secure (under unbounded collusion). To gain confidence in the new assumption, we prove that the standard LWE assumption implies the degree-1 case and cryptanalyse the d > 1 case. As a corollary, we obtain a new pathway to post-quantum secure indistinguishability obfuscation (iO), conditioned on the above new assumption, standard LWE, and the existence of polynomial-stretch pseudorandom generators in mathsf{NC}^{0}. Along the way, we give a new, simple (public-key) FE scheme for linear functions with selective security under the standard LWE assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1977) | 2026-09-11
