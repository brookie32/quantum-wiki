---
title: "One Unverified Coordinate Is Enough: Key Recovery from Faulty Fujisaki–Okamoto Rejection Checks in ML-KEM"
date: "2026-09-27"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2239"
summary: "The Fujisaki-Okamoto (FO) transform makes ML-KEM IND-CCA secure by re-encrypting the decrypted message and returning an implicit-rejection value on any mismatch. Deployed implementations of ML-KEM and"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The Fujisaki-Okamoto (FO) transform makes ML-KEM IND-CCA secure by re-encrypting the decrypted message and returning an implicit-rejection value on any mismatch. Deployed implementations of ML-KEM and its predecessor Kyber have realized this check incorrectly: a skipped conditional move (pqc_kyber/cosmian_kyber, RUSTSEC-2026-0290/-0288) and truncated ciphertext comparisons (wolfSSL, CVE-2026-10097 and CVE-2026-6330). We ask how much of the check must be broken before the key is recoverable, and show that one unverified ciphertext coordinate suffices. For a valid ciphertext the adversary knows the encryption randomness, so sweeping an unverified v-coordinate over the compression grid measures the decryption noise there, a known short-coefficient linear form in the secret; one bounded-error observation per message, solved by least squares, recovers the key. Under a regularity assumption we prove that O(kn log kn) observations identify the key, and we demonstrate full recovery from a single unverified coordinate on all three parameter sets in a few times 10⁵ decapsulation queries against a simulated incomplete comparison built on the kyber-py implementation, with ML-KEM-1024 cheapest owing to its finer compression grid. Sessions fall inversely with the number of unverified coordinates but query cost does not: one unverified coordinate costs what a leaked tail of fifty does. The skipped conditional move yields a complete plaintext-checking oracle and Θ(kn) queries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2239) | 2026-09-27
