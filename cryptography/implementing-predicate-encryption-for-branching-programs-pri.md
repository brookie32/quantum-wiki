---
title: "Implementing Predicate Encryption for Branching Programs: Private Computation over Key-Homomorphic Encodings Without FHE"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2539"
summary: "Predicate encryption (PE) encrypts a message under an attribute that the ciphertext hides, allowing a secret key for a predicate to recover the message only when the attribute satisfies the predicate."
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Predicate encryption (PE) encrypts a message under an attribute that the ciphertext hides, allowing a secret key for a predicate to recover the message only when the attribute satisfies the predicate. Existing public-key implementations support useful specialized predicates, but enforcing heterogeneous conditions with one key requires an attribute representation fixed before encryption, which grows with the supported types of conditions and cannot express types it does not anticipate, such as regular expressions. Lattice-based PE for general circuits is far more expressive, but existing constructions rely on fully homomorphic encryption (FHE), typically evaluated as a Boolean circuit over key-homomorphic encodings, which expands the computation and amplifies noise growth and leads to impractically large parameters. Existing PE thus offers either practicality for restricted predicates or expressiveness at an impractical cost. We present a lattice-based PE scheme for branching programs that avoids FHE entirely and combines heterogeneous conditions in a single predicate over a common attribute representation. It rests on two techniques: asymmetric multiplication, which multiplies a hidden program state by an encrypted attribute symbol through decryption inside an encoding, and lookup tables over exponents, which evaluate arbitrary state transitions on a single encoding by ring automorphisms. Under circular Ring-LWE, the scheme is selectively weakly attribute-hiding against polynomially many colluding unauthorized keys. We give, to our knowledge, the first implementation of PE for a predicate class as expressive as branching programs. On a single NVIDIA A100 GPU, for a predicate that combines a range check and a regular-expression check on a 10-bit attribute, with parameters targeting 128-bit security against known Ring-LWE attacks, encryption takes 4.06 hours, key generation 4.70 hours, and decryption 4.23 hours, with 342.25 GB ciphertexts. These costs remain large, but compared with a single FHE multiplication evaluated as a Boolean circuit over encodings, the basic step of PE that evaluates FHE over encodings, whose ciphertexts alone occupy tens of exabytes per attribute bit, our ciphertexts are at least 2imes10^9 times smaller per attribute bit, and our decryption needs at least 2imes10^{16} times fewer 64-bit integer multiplications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2539) | 2026-10-19
