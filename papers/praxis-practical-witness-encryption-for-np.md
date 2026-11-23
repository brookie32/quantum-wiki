---
title: "Praxis: Practical Witness Encryption for NP"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2971"
summary: "Witness encryption encrypts a message to an NP statement so that whoever holds a witness can decrypt. Over a decade after its introduction, known constructions for general NP statements are far from p"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Witness encryption encrypts a message to an NP statement so that whoever holds a witness can decrypt. Over a decade after its introduction, known constructions for general NP statements are far from practical or rest on heuristic or broken assumptions. We propose Praxis, a practical scheme for NP, and prove it extractable in the bilinear generic group and random oracle models under Module-SIS. Our instantiation encrypts to a Groth16 verifier on BN254, set up honestly, which serves every NP relation at the same cost: at 100-bit security, its ciphertext is 7.88 GiB, encryption takes 2^{34.2} base-field multiplications, and decryption with a Groth16 proof 2^{33.0} on average. We give Lean 4 proofs of correctness and extraction at this instantiation’s parameters. Praxis starts from the rank-gap template of the recent feasibility result [Hair and Sahai, arXiv 2026]. Where they raise the gap to keep decryption polynomial, we fix it, so decryption ends with a search that is exponential but concretely fast: O(2^{lambda/4} N^{1/4}) expected operations for a statement in N Boolean unknowns at lambda-bit security. A quadratic arithmetic program makes our hidden matrix low rank, so where their ciphertext encodes a basis of a matrix space, ours holds factors of width two, which a pairing multiplies. Weights and identities from an extension field tie copies of this matrix, so an adversary telling encryptions apart yields a witness or a Module-SIS solution. For the same Groth16 statement and 100-bit security level, Praxis reduces the ciphertext size and the cost of encryption of either of their constructions by over ten orders of magnitude, and that of decryption by over six.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2971) | 2026-11-21
