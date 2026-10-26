---
title: "Notes on BulletProofs++ Range Proofs"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2648"
summary: "We review the Bulletproofs++ construction which replaces the bit-decomposition inner-product argument of Bulletproofs with a reciprocal set-membership argument over base-16 digits. We present a self-c"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

We review the Bulletproofs++ construction which replaces the bit-decomposition inner-product argument of Bulletproofs with a reciprocal set-membership argument over base-16 digits. We present a self-contained specification of the 64-bit range proof as well as a general batched variant parametric in the batch size M and bit width b and prove honest-verifier zero-knowledge and exact-form knowledge soundness. We describe the evaluation and optimizations of our Rust implementation over Ristretto255, which proves up to 7.8imes and verifies up to 4.5imes faster than regular Bulletproofs. Finally, we correct two formulas of the original paper: the affine T^3 term of the scalar polynomial p_s(T) carries a factor of 2, and the slot-0 component of the blinding vector r_S carries the opposite sign.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2648) | 2026-10-26
