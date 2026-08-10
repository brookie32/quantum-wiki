---
title: "Quasipolynomial Cryptanalysis of the  McEliece Cryptosystem (or: PIR Meets McEliece)"
date: "2026-08-07"
updated: "2026-08-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1630"
summary: "The McEliece code-based cryptosystem, utilizing binary Goppa codes, is the earliest public-key encryption scheme that is still considered post-quantum secure. We present a simple, classical quasipolyn"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

The McEliece code-based cryptosystem, utilizing binary Goppa codes, is the earliest public-key encryption scheme that is still considered post-quantum secure. We present a simple, classical quasipolynomial-time distinguisher for Goppa--McEliece in the asymptotic "Classic McEliece" regime: for code length n, extension degree m=Theta(log n), Goppa degree t=Theta(n/log n), and public-code dimension k=Theta(n), the algorithm runs in time n^{{mathcal O}(log n)} and distinguishes the McEliece public key from the uniform distribution over mathbb F_2^{kimes n} with advantage 1-o(1). The distinguisher is not merely asymptotic: it applies to all Classic McEliece parameter sets considered in the NIST process and yields improved (though not yet practical) concrete attack estimates. Our distinguishing attack originated from a failed attempt to construct doubly efficient private information retrieval (PIR) protocols from algebraic locally decodable codes, and can be intuitively explained from the PIR perspective. We extend this provable algorithm to a heuristic n^{{mathcal O}(log n)}-time ciphertext-decryption attack that recovers the message from a noisy codeword.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1630) | 2026-08-07
