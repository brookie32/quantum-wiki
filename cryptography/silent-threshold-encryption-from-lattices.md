---
title: "Silent Threshold Encryption from Lattices"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1716"
summary: "Silent threshold encryption is a generalization of threshold encryption where the public encryption key associated with a group of users is a deterministic function of their individual public keys. Th"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

Silent threshold encryption is a generalization of threshold encryption where the public encryption key associated with a group of users is a deterministic function of their individual public keys. The main efficiency requirement is that the ciphertext size should be sublinear in (and ideally, independent of) the size of the decryption quorum N. Existing constructions of silent threshold encryption for arbitrary threshold policies have either relied on bilinear maps or on heavyweight tools such as witness encryption and indistinguishability obfuscation. Recently, several works have shown how to support constant thresholds from the decomposed learning with errors (LWE) problem. In this work, we show how to construct a silent threshold encryption scheme from the decomposed LWE assumption where the ciphertext size for encrypting a single bit is ilde{O}(T) + mathsf{poly}(lambda, log N). Here, N is the total number of users, T is the threshold, and lambda is the security parameter. Our scheme achieves non-trivial succinctness for all thresholds T = N^arepsilon for any constant arepsilon < 1. More generally, our scheme extends beyond threshold policies to any monotone policy family that has a succinct (computational) secret sharing scheme; the ciphertext in this case scales with the maximum number of corrupted shares. The core building block in our work is a new bounded-collusion registered functional encryption (FE) scheme with succinct ciphertexts. Specifically, for N users and a collusion bound Q, we obtain a registered FE scheme that supports depth-d Boolean circuits on ell-bit inputs and single-bit output with ciphertext size Q dot ilde{O}(d) + ell dot mathsf{poly}(lambda, d, log N). Security relies on the decomposed LWE assumption in the random oracle model. Previously, bounded-collusion registered FE for general circuits was known only from bilinear maps, evasive LWE, or indistinguishability obfuscation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1716) | 2026-08-17
