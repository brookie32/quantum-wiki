---
title: "A New Approach to Reducing Modulus Requirements in Homomorphic Computation: Precision Allocation in CKKS"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2562"
summary: "Fully homomorphic encryption (FHE) enables computation over encrypted data subject to the prescribed security and precision requirements (allowable deviations from ideal results). Among all FHE scheme"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

Fully homomorphic encryption (FHE) enables computation over encrypted data subject to the prescribed security and precision requirements (allowable deviations from ideal results). Among all FHE schemes, CKKS is a representative scheme for approximate arithmetic, allowing the same operation on multiple values packed into a single RLWE ciphertext. Reducing ciphertext modulus (Q) for given output precision requirements under RLWE security constraints is a central challenge in homomorphic computation. However, despite advances in plaintext and ciphertext representations, algorithmic optimizations, and modulus management, the budget in most existing approaches remains dependent on the highest required precision and cannot reduce the baseline modulus cost to overcome encryption noise. In this work, we make average rather than maximum precision requirements govern the modulus budget and achieve savings in the baseline cost. Under decryption correctness constraints, we make these possible by allocating arbitrary output precision among independent values and quantify the modulus savings arising from differences in their precision requirements. As a bonus, our construction preserves the standard CKKS ciphertext format, which helps maintain compatibility with existing optimizations. And the construction inherits the IND-CPA security of CKKS without additional cryptographic assumptions. With a 64-bit average precision requirement, we transfer 75 bits of precision without reducing evaluation depth and up to 735 bits while preserving correct initial recovery, raising the precision allocated to the target values to 2,269 bits. For six successive squarings of 256 messages targeting 224-bit precision, our implementation reduces the initial modulus bit length by 67% compared with standard CKKS, allowing a fourfold reduction in ring dimension.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2562) | 2026-10-20
