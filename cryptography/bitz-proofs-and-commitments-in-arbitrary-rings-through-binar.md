---
title: "BitZ: proofs and commitments in arbitrary rings through binary fields"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2141"
summary: "We introduce BitZ, a hash-based Polynomial Commitment Scheme (PCS) for committing to multilinear polynomials mathbf{f} with coefficients in an arbitrary finitely generated ring S, e.g. a finite field "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We introduce BitZ, a hash-based Polynomial Commitment Scheme (PCS) for committing to multilinear polynomials mathbf{f} with coefficients in an arbitrary finitely generated ring S, e.g. a finite field F, the integers Z, a cyclotomic ring, etc. Moreover, given another arbitrary ring R and a ring homomorphism psi:So R, BitZ then proves evaluation claims over R for the polynomial psi(mathbf{f}). BitZ's costs depend almost exclusively on the number of bits in the coefficients of mathbf{f}, and not on S, R or psi. Moreover, BitZ provides range checks (or more generally, bit-size checks) essentially for free. BitZ can thus be used as a PCS in essentially any proof system. We do so to build a SNARK, called BitZ-SNARK, for integer polynomial constraints, following the fingerprinting technique of Campanelli and Hall-Andersen, where one commits over Z and proves the constraints over a random prime field F_q, i.e. BitZ is deployed with S=Z, R=F_q, and psi reduction modulo q. BitZ applies equally to other ring-based proof systems, or field-based ones. To commit to mathbf{f}, BitZ first decomposes mathbf{f} into a string of bits, and then commits to it over a binary field F_{2^{nu}}, in packed form. The scheme then proves the linear claim on psi(mathbf{f}) over the arbitrary ring R, even though it committed to the bits forming mathbf{f} over a binary field. We implement BitZ-SNARK and use it to prove, among others, SHA-256 hashing followed by ECDSA signature verification; RSA modular exponentiation and Poseidon hashing; integer multiplication; and SHA-256 hashing followed by multiplication modulo 2^{32}, consistently obtaining better performance than prior approaches on most tasks. As an example, we achieve a throughput of 5 million proved 32-bit integer multiplications per second on a MacBook Air M5 24 GB (10 threads, CPU-only) with proof sizes under 150 kB. We prove a SHA-256 hash of a 2 kB (2^5 compressions) message followed by a P-256 ECDSA signature verification with 50 ms and 3.3 ms prover and verifier time, respectively, and with a proof of 76 kB, single-threaded. With 10 threads the times are 20 ms and 3.4 ms.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2141) | 2026-09-21
