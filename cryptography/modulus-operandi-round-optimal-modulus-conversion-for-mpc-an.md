---
title: "Modulus Operandi: Round-Optimal Modulus Conversion for MPC and Threshold FHE"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2450"
summary: "In secure multiparty computation (MPC), modulus conversion turns a sharing of a value x modulo q into a sharing of the same value modulo t, without leaking anything about x. One important application "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

In secure multiparty computation (MPC), modulus conversion turns a sharing of a value x modulo q into a sharing of the same value modulo t, without leaking anything about x. One important application of modulus conversion is in threshold decryption for lattice-based cryptosystems, where a sharing modulo the ciphertext modulus has to be moved to the plaintext modulus before it can be opened. The most efficient protocols so far (Damgård et al., Asiacrypt 2026) are in the preprocessing model, assume x is bounded away from q by a constant factor and take two rounds for a prime target modulus, three rounds for arbitrary moduli, and one round when all moduli are 2-powers. We improve upon this by constructing three new modulus conversion protocols in the preprocessing model: - Our first conversion protocol takes a single round for arbitrary moduli, consisting of just one opening. - Our second conversion protocol is a variant of the first protocol, where in the preprocessing most of the secure multiplications are replaced by private inputs, which are checked in a batch using fully linear interactive oracle proofs (FLIOPs). This makes the preprocessing cheaper (amortized over a batch of conversions) when the number N of parties is small. This comes at the cost of making the bound on x a factor N stronger. - Our third conversion protocol avoids the bound on x altogether but takes two rounds. All our protocols are stated in the arithmetic black box (ABB) model, so they can run on top of a wide variety of MPC protocols, inheriting their corruption threshold and security model. To allow the third conversion protocol to run in two rounds, we construct the first one-round comparison protocol in the ABB model for comparing a bitwise shared n-bit value against a public threshold with polynomial-size preprocessing. Concretely, the preprocessing size is mathcal O(n^2) in general, and mathcal O(n^2 / log n) in our case where the secret value is fixed in preprocessing. We also construct constant-round ABB protocols without preprocessing for computing symmetric functions and comparisons of values shared bitwise modulo powers of arbitrary primes (e.g., 2^k), at communication quasi-linear in the number of input bits. Previously, this required either a sufficiently large prime or polynomially larger communication. Finally, we give an impossibility result for non-interactive modulus conversion, demonstrating that a single round is optimal: unless t divides q, every non-interactive conversion for inputs x < q/eta is incorrect with probability at least approx 1/(4eta).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2450) | 2026-10-12
