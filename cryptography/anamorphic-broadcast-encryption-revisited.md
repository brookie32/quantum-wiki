---
title: "Anamorphic Broadcast Encryption, Revisited"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3045"
summary: "Anamorphic encryption lets ordinary ciphertexts carry an additional message whose presence remains hidden even when the ordinary decryption key is exposed. We revisit this goal in the broadcast settin"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Anamorphic encryption lets ordinary ciphertexts carry an additional message whose presence remains hidden even when the ordinary decryption key is exposed. We revisit this goal in the broadcast setting studied by Do et al. (EUROCRYPT 2025) and give a distinguishing attack against their Dual-Regev construction. Given one encryption query and the ordinary secret key, an adversary distinguishes ordinary and anamorphic ciphertexts with non-negligible advantage by testing the decryption residual before rounding. We construct an anamorphic broadcast channel for the Dual-Regev public key encryption scheme that delivers a common L-bit message to a fixed group in one ordinary ciphertext. Using only public information from the ordinary setup, the sender samples encryption randomness correlated with the recipients' anamorphic public keys, leaving ordinary decryption and its residual distribution unchanged. We prove anamorphic security and anamorphic-message privacy with the ordinary secret key exposed, and joint message privacy for both messages when that key is not exposed. These guarantees follow from LWE in the standard model. We instantiate the channel in the batched laconic encryption core of registration-based encryption (Klooß et al., S&P 2026) and in the encryption layer of Epoque (Boyen et al., EuroS&P 2021). These instantiations illustrate the broader applicability of our embedding technique to schemes built on Dual-Regev encryption. We implement the basic construction and both applications in Rust and demonstrate ordinary and anamorphic message recovery from the same ciphertext using the corresponding decryption keys. With the same parameters for the ordinary layer, both modes have comparable encryption times after a one-time preprocessing of the group members' anamorphic public keys.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3045) | 2026-11-25
