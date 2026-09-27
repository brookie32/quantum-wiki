---
title: "A Fiat-Shamir Transformation for Private-Coin Protocols"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2227"
summary: "The Fiat--Shamir transformation is a fundamental paradigm in cryptography for compiling interactive public-coin protocols into non-interactive arguments. While this transformation has been extensively"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

The Fiat--Shamir transformation is a fundamental paradigm in cryptography for compiling interactive public-coin protocols into non-interactive arguments. While this transformation has been extensively studied for public-coin protocols, the setting of private-coin protocols, where the verifier's messages depend on secret randomness, remains largely unexplored. To date, there are no candidate transformations for private-coin protocols, neither in the standard model nor in idealized settings. In this work, we present a generic transformation that compiles any 3-message private-coin interactive proof into a non-interactive argument in the standard model, while preserving zero-knowledge. Our construction relies on sub-exponentially secure indistinguishability obfuscation, pseudorandom functions, and input-hiding obfuscation (IHO). As a corollary, this rules out the existence of 3-message weak zero-knowledge proofs with small enough soundness error. We complement this positive result by showing that the reliance on IHO is inherent: any secure Fiat--Shamir transformation for general private-coin protocols necessarily implies the existence of IHO. Finally, we rule out Fiat--Shamir transformations for multi-round private-coin protocols. Specifically, assuming the existence of collision-resistant hash functions, we prove that no such transformation exists in the multi-round setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2227) | 2026-09-26
