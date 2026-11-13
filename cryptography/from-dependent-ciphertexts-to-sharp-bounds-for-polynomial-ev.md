---
title: "From Dependent Ciphertexts to Sharp Bounds for Polynomial Evaluation in BGV"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2869"
summary: "A central challenge in Fully Homomorphic Encryption (FHE) is the selection of ciphertext moduli, which depends on accurately estimating noise growth during homomorphic evaluation. Choosing excessively"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

A central challenge in Fully Homomorphic Encryption (FHE) is the selection of ciphertext moduli, which depends on accurately estimating noise growth during homomorphic evaluation. Choosing excessively large moduli reduces the efficiency and scalability of the scheme, whereas underestimating noise can result in decryption failures and potential security vulnerabilities. Average-case analyses have provided promising probabilistic estimates of noise growth in practical FHE computations. However, recent studies indicate that reliable estimates must account for dependencies among ciphertext errors, as neglecting these correlations can systematically underestimate noise. This work presents the first average-case analysis for the BGV scheme that accounts for both correlations induced by secret/public keys and ciphertext dependencies. We propose new variance estimates for the noise coefficients in homomorphic additions and multiplications involving dependent ciphertexts, and extend our framework to the homomorphic evaluation of polynomial functions, which is widely employed in FHE applications. Our theoretical estimates closely align with experimental observations, exhibiting discrepancies smaller than 1.2 bits. Finally, these estimates are adopted to choose the initial BGV parameters, leading to significantly smaller ciphertext moduli compared to those currently adopted in widely used FHE libraries, thus improving the efficiency of the scheme. Compared to OpenFHE, we obtain an average reduction of about 11.5% in the ciphertext modulus size, while relative to HElib, we reduce the ratio between consecutive moduli up to 23 bits per level in practical settings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2869) | 2026-11-11
