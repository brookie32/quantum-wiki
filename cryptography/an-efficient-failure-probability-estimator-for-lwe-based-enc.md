---
title: "An efficient Failure Probability Estimator for LWE-based encryption, and application to IBE"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2751"
summary: "In recent years, lattice-based cryptography has proven to be a source of post-quantum cryptosystems. In particular, the blueprint of Learning With Errors (LWE) encryption enabled the creation of Kyber"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

In recent years, lattice-based cryptography has proven to be a source of post-quantum cryptosystems. In particular, the blueprint of Learning With Errors (LWE) encryption enabled the creation of Kyber, chosen by NIST to be standardized as ML-KEM. Because of the structure of LWE encryption, the decryption of a ciphertext can give an incorrect plaintext. This event (a decryption failure) happens randomly with some probability. Since this is a problem for both functionality and security, we must ensure that this failure probability is cryptographically negligible. Usually, this is assessed with theoretical approximations and upper-bounds. The authors of Kyber used a Python program to compute that probability more precisely, enabling to fine-tune the compression of the ciphertext, hence reducing its size. However, because of its performances, this program has been limited to Kyber, and all the other schemes are still studied theoretically. In this paper, we design a more efficient Failure Probability Estimator, that we implement in low-level languages (C and CUDA C++), to reach higher parameters used in real schemes based on structured LWE. We illustrate some benefits of our tool with two Identity-Based Encryption schemes. For the first scheme, our tool allows to reduce the size of the ciphertext by about 20%. For the second one, we reduce the failure probability (thus improving security) without impacting the scheme (key size, ciphertext size, etc.).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2751) | 2026-11-03
