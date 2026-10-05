---
title: "The Power of Permutable PRPs: Towards Trapdoor Permutations with Full Key and Message Domains"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2333"
summary: "Shmueli and Zhandry introduced permutable pseudorandom permutations (PRPs) and used them to construct trapdoor permutations with a full message domain but a sparse public-key space. We extend this app"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Shmueli and Zhandry introduced permutable pseudorandom permutations (PRPs) and used them to construct trapdoor permutations with a full message domain but a sparse public-key space. We extend this approach to construct puncturable trapdoor permutations with full message and per-instance key domains in the common-reference-string (CRS) model. Our construction assumes a secure permutable PRP for general swaps, indistinguishability obfuscation, and an injective length-doubling pseudorandom generator, all secure against polynomial-time adversaries. Instantiating the underlying permutable PRP from indistinguishability obfuscation and one-way functions requires subexponential security. A one-time setup produces a CRS and a master trapdoor. For every honestly generated CRS, every bit string of the prescribed key length indexes a permutation of the full message space, allowing uniform public-key sampling without validation or rejection. The master trapdoor derives an inversion trapdoor for every key. The family supports two-level puncturing: the master trapdoor can be punctured at a key, and an individual trapdoor can be punctured at an output. For a uniformly sampled challenge key and output, recovering the missing preimage remains hard even when both punctured trapdoors are revealed. To our knowledge, this is the first family combining these full-domain properties, master trapdoor derivation, and two-level punctured security. We give three applications. In the random-oracle model, the family yields deterministic identity-based encryption with zero ciphertext expansion and adaptive weak-source pseudorandomness under a computational hardness condition on message sources. Security holds even given a key that decrypts every ciphertext except the challenge under the selected identity. The family also yields identity-based signatures with perfect uniqueness and adaptive unforgeability in the random-oracle model. Finally, puncturable trapdoors give a direct construction of hard-on-average End-of-Line instances, establishing PPAD hardness without passing through Sink-of-Verifiable-Line.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2333) | 2026-10-04
