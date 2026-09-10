---
title: "Security Properties of Iterated Random Functions"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1923"
summary: "Iteration of a cryptographic hash function is a common practice in many applications, typically used to enhance resistance against various attacks (e.g., to slow down dictionary attacks in password ha"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Iteration of a cryptographic hash function is a common practice in many applications, typically used to enhance resistance against various attacks (e.g., to slow down dictionary attacks in password hashing). While the security properties of (non-iterated) cryptographic hash functions are well studied and understood by the cryptographic community, their iterated counterparts have received comparatively little attention. Even in idealized models such as the random oracle model, preimage and collision resistance of an iterated hash function do not seem to be fully characterized. The security of an iterated random function has mainly been studied through its indistinguishability from the (non-iterated) random function. Bhaumik et al. (ASIACRYPT 2017) analyse the collision resistance of an iterated random function, but in a model where the adversary has oracle access to the iterated random function (and not the random function itself). Kogan et al. (CCS 2017) then study the preimage resistance of an iterated random function in the random oracle model, but focus only on finding preimages for the last iteration step. In this paper we complete the picture by providing attacks and matching upper bounds for preimage and collision resistance of an iterated random function (H^k), where (H olon [n] o [n]) is modelled as a random oracle. While collision resistance is essentially unaffected by iterations, we prove that the situation is very different in the case of preimage resistance. Specifically, we present a concrete attack on preimage resistance of (H^k) with advantage (Omega(frac{qk}{n})) assuming (q = Omega(k)), where (q) denotes the number of (H)-oracle queries made by the adversary. We complement our attack with an upper bound (O(frac{qk+k^2}{n})), which is tight in the (q = Omega(k)) regime. Finally, we show that iteration weakens preimage resistance only for random functions: when (H) is a permutation, preimage resistance remains essentially unaffected.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1923) | 2026-09-08
