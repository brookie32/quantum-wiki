---
title: "Functional Verification of Additive FFT Assembly Implementations in Code-Based PQC"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2307"
summary: "We present the first formal verification results for the highly optimized additive Fast Fourier Transforms (FFTs) in two different code-based post-quantum cryptosystems: Classic McEliece and Hamming Q"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We present the first formal verification results for the highly optimized additive Fast Fourier Transforms (FFTs) in two different code-based post-quantum cryptosystems: Classic McEliece and Hamming Quasi-Cyclic. Since Classic McEliece is already a standard and HQC is being standardized, they may both see wide adoption in the future. The Gao-Mateer and Frobenius additive FFTs during decoding are clearly the most intricate, error-prone components in the two cryptosystems respectively. They are not only complicated and mathematically intricate, but also aggressively optimized in practical implementations. A main problem of this verification is the >2^{14} independent bit-variables in each multiplicand. Aside from adding a vector syntax and improving various syntactic transformations to the open-source tool CryptoLine, we also formulate additive FFTs as Chinese Remainder Theorem decompositions which factors the verification problem into local checks feasible for computer algebra systems like Singular. The workload was also tractable: the calendar time for the formal verification in this paper was less than three months for our very limited workforce.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2307) | 2026-10-02
