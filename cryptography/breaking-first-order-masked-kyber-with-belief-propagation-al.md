---
title: "Breaking First-Order Masked Kyber with Belief Propagation Alone"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2448"
summary: "We recover the long-term key of a first-order masked Kyber768 implementation on an ARM Cortex-M4 from about 2200 decapsulation power traces, using only authentic ciphertexts that pass ciphertext-valid"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

We recover the long-term key of a first-order masked Kyber768 implementation on an ARM Cortex-M4 from about 2200 decapsulation power traces, using only authentic ciphertexts that pass ciphertext-validity checks. The secret is freshly shared before every decapsulation, and the attack combines weak second-order leakage from both shares. Under the evaluated leakage model, even exact Hamming weights of both shares provide about 97% less mutual information about a decryption-noise coefficient than the exact Hamming weight of the unmasked coefficient. A profiled neural network estimates Hamming-weight distributions for the two arithmetic shares of each noisy message coefficient. We combine these distributions into likelihoods on the decryption noise, which is a known affine function of the secret and the public-key error. A belief-propagation (BP) solver accumulates these likelihoods across traces, preserving their non-Gaussian shapes while approximating the aggregate interference from other key coordinates by a Gaussian. An Onsager correction from approximate message passing corrects for feedback between each factor and the current beliefs. The solver recovers all 1536 secret and error coefficients without lattice reduction. At the evaluated trace budgets, least squares performs no better than the all-zero estimate, and a greedy inequality solver fails even with exact Hamming weights. The evaluated primal-lattice cascade does not reduce the trace requirement: below BP's recovery threshold, its output remains too diffuse to enable practical lattice recovery. At 2000 traces, BP-derived hints lower the estimated BKZ block size from 624 to 505, leaving the lattice attack impractical.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2448) | 2026-10-12
