---
title: "Efficient (Functional) Bootstrapping for CKKS over the Conjugate-Invariant Ring"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2618"
summary: "The CKKS fully homomorphic encryption scheme enables efficient encrypted computation over complex-valued data. In many real-world cases, however, the computation only involves real data, and storing t"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

The CKKS fully homomorphic encryption scheme enables efficient encrypted computation over complex-valued data. In many real-world cases, however, the computation only involves real data, and storing them inside complex slots wastes the encoding ability. This motivated the design of conjugate-invariant CKKS (CI-CKKS) instantiated over the conjugate-invariant ring (CIR), which provides the same number of real slots while halving the RLWE dimension. Despite its better efficiency in handling real data, CI-CKKS cannot be bootstrapped directly in CIR, since the CoeffToSlot and SlotToCoeff linear transformations used in bootstrapping require storing complex values in both plaintexts and ciphertexts. The existing method in Lattigo bootstraps two CI-CKKS ciphertexts by converting them to a standard CKKS ciphertext, bootstrapping there, and converting back. This bootstrapping is efficient only for batched inputs, and therefore suffers from limited flexibility. Another issue with CI-CKKS is that many existing functional bootstrapping methods encode intermediate values using complex roots of unity, whereas CI-CKKS provides only real-valued slots. Our first contribution is a real FFT algorithm over the conjugate-invariant ring, thereby enabling native bootstrapping in CI-CKKS. Our second contribution investigates functional bootstrapping over CI-CKKS. We adapt the real-valued AKP interpolant with radial correction and develop a single-cosine Hermite interpolation method using a single real ciphertext. We show existing complex-valued interpolation methods can be implemented using two real ciphertexts to simulate complex arithmetic. We also study the numerical behavior of real-valued interpolation and evaluate the tradeoffs between computational efficiency and precision. We implement our methods in Lattigo. Our native CI-CKKS bootstrapping achieves a 1.46--1.80imes speedup in single-ciphertext bootstrapping across different StC and CtS factorizations. Compared with state-of-the-art functional bootstrapping methods over standard CKKS, our methods achieve 1.16--1.68imes higher throughput.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2618) | 2026-10-23
