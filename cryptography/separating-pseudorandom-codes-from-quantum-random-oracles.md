---
title: "Separating Pseudorandom Codes from Quantum Random Oracles"
date: "2026-11-04"
updated: "2026-11-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2774"
summary: "Pseudorandom codes (PRCs) combine two seemingly conflicting goals: robustness to noise and computational indistinguishability from random strings. Recent work has shown that classical symmetric-key PR"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

Pseudorandom codes (PRCs) combine two seemingly conflicting goals: robustness to noise and computational indistinguishability from random strings. Recent work has shown that classical symmetric-key PRCs over binary alphabets cannot be constructed from minimal cryptographic assumptions, such as one-way functions, via black-box reductions. In this work, we revisit this question in the presence of quantum computation and quantum information. We first consider pseudorandom codes with classical codewords but quantum algorithms. We prove that symmetric-key pseudorandom codes robust to Bernoulli noise admit no black-box construction from quantum random oracles, and hence from quantum-secure one-way functions. This establishes that the classical black-box barrier for PRCs persists even in the quantum computational setting. Motivated by this separation, we investigate the notion of quantum pseudorandom codes (QPRCs), in which codewords are quantum states and security is defined via computational indistinguishability from Haar-random states. We then present several positive results. Assuming quantum-secure one-way functions, we construct QPRCs that are secure against a single encoding query, allow multiple copies of the challenge state, and tolerate an error rate matching that of any classical uniquely decodable binary error-correcting code against a dephasing or bit-flip channel. We also show that the PRFS with proof of destruction due to Behera et al. (TCC 2023) can be extended to a 0-bit QPRC that is secure against multiple encoding queries and tolerates unbounded phase errors but only a constant number of bit-flip errors. Finally, assuming the existence of quantum-secure single-query pseudorandom states (1PRS), we construct single-query single-copy QPRC that tolerate arbitrary Pauli noise up to the decoding radius of a quantum error-correcting code with unique decoding.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2774) | 2026-11-04
