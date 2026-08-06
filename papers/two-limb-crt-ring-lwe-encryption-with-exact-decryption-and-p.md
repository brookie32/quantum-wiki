---
title: "Two-Limb CRT Ring-LWE Encryption with Exact Decryption and Public Re-randomization"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1618"
summary: "Anonymity infrastructures such as mix networks, anonymous storage, and privacy-preserving replication rely on public re-randomization: any party holding only public information can transform a ciphert"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Anonymity infrastructures such as mix networks, anonymous storage, and privacy-preserving replication rely on public re-randomization: any party holding only public information can transform a ciphertext into a fresh-looking encryption of the same plaintext, hiding the linkage between the two. Classical ElGamal-based solutions are broken by quantum adversaries, while existing lattice-based alternatives carry very large ciphertexts with unanalyzed noise growth, rely on heavyweight homomorphic-encryption stacks with approximate (rounded) decryption, or lack a precise analysis of how many re-randomizations are safe. We address this gap with a practical Ring Learning with Errors (Ring-LWE) public-key encryption scheme supporting public re-randomization without ciphertext growth. Our construction is Lyubashevsky–Peikert–Regev / Fan–Vercauteren (LPR/BFV)-style encryption over R=Z[x]/(x^n+1) with n=4096, engineered around a two-limb Chinese Remainder Theorem (CRT) modulus q=tdot q_2 with 32-bit primes. Embedding plaintext as Delta M = q_2 M makes the message vanish modulo q_2, so the q_2-limb carries only the decryption noise, enabling exact message recovery without rounding. We prove correctness with explicit decryption-failure bounds that remain valid under repeated re-randomization, via an aggregation lemma showing that arbitrarily many re-randomizations affect decryption only through a single aggregated randomness triple. We also prove that two-limb ciphertexts are pseudorandom (indistinguishable from uniform, IND) under Decision Ring-LWE over the combined modulus q=tq_2$; security against chosen-plaintext attack (IND-CPA) and re-randomization unlinkability follow. A constant-time Rust implementation encrypts in 0.80 ms, re-randomizes in 0.51 ms, and decrypts in 0.21 ms per 64 KiB ciphertext carrying 15.5 KiB of payload on a fixed-frequency 3.8 GHz CPU—on par with a modulus-matched Microsoft SEAL baseline—and passes timing-leakage tests. Empirical noise simulations validate the analysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1618) | 2026-08-05
