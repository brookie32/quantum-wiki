---
title: "High Precision Noise Cleaning for CKKS with Application to Asynchronous Threshold CKKS"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2675"
summary: "Noise cleaning in discrete CKKS uses Hermite interpolation to reduce the input error while preserving the encrypted discrete message. Cryptographic applications based on noise flooding require the err"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Noise cleaning in discrete CKKS uses Hermite interpolation to reduce the input error while preserving the encrypted discrete message. Cryptographic applications based on noise flooding require the error after cleaning to be sufficiently small for the added noise to provide statistical hiding without preventing exact recovery. This requirement is more stringent than decryption correctness alone, but the achievable noise reduction is limited by errors introduced during homomorphic evaluation. In particular, key switching and rescaling can dominate the output error even when a higher interpolation order substantially reduces the polynomial residual. We propose a high precision noise cleaning method for CKKS that preserves encrypted integer messages while attaining a prescribed bound on normalized output noise. We jointly select the cleaning polynomials and evaluation parameters according to a complete error bound that accounts for the input noise and the errors introduced during homomorphic evaluation. By composing Hermite polynomials of lower degree, we can achieve the same output noise bound with a smaller ciphertext modulus and lower evaluation cost than a single higher degree polynomial. In addition, to reduce the ciphertext tensor degree, we construct polynomial representations with noisy auxiliary powers that cancel selected auxiliary error terms. For integer messages, we extract the bits through multi-value functional bootstrapping, then clean and recombine them into a single ciphertext. Finally, we apply high precision noise cleaning to construct an asynchronous threshold CKKS scheme that achieves strong simulation security in the random oracle model. We implement binary and integer noise cleaning in OpenFHE. For binary messages and a normalized output noise target of 2^{-300}, the selected composition reduces cleaning time from 9.63 to 1.54 seconds compared with a single Hermite evaluation under the same input error bound and security requirements. The composition also requires a smaller input ciphertext modulus and less evaluation key storage. We also evaluate the complete construction on 8 bit integers packed into all 32{,}768 slots. The maximum measured normalized output noise is below 2^{-300} with either leveled digit extraction or functional bootstrapping.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2675) | 2026-10-29
