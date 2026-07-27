---
title: "Catching Many Traitors in Threshold Traitor Tracing: Lower Bounds and Constructions"
date: "2026-07-24"
updated: "2026-07-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1523"
summary: "A t-out-of-n threshold decryption scheme distributes decryption key shares among n parties so that any t of them can jointly decrypt a ciphertext, while fewer than t learn nothing about the plaintext."
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

A t-out-of-n threshold decryption scheme distributes decryption key shares among n parties so that any t of them can jointly decrypt a ciphertext, while fewer than t learn nothing about the plaintext. Traditional threshold schemes provide no accountability: a coalition of t or more parties can combine their key shares and construct a pirate decoder that decrypts arbitrary well-formed ciphertexts, without any risk of being traced. To address this, Boneh, Partap, and Rotem [CRYPTO '24] introduced the notion of threshold traitor tracing (TTT), where a tracing algorithm that is given black-box access to the pirate decoder can identify at least one of the colluding parties. Many subsequent threshold traitor tracing schemes similarly find only a single traitor, even though the decoder must have been constructed using at least t keys. While some constructions can find multiple traitors, they do so at the cost of large ciphertexts or only achieving a weak form of correctness. In this work, we make the following contributions: - Lower bounds: We show that for all existing traitor tracing techniques, the ciphertext must be large to allow tracing close to t traitors. In particular, to trace t-O(1) traitors, the ciphertext size must be at least Omega(t). To trace a leq t- omega(1) traitors, the ciphertext size must scale with Omega(frac{a-1}{t-a+1}). For schemes that rely on fingerprinting codes, we show an even stronger lower bound. - Upper bounds: We present two generic compilers that construct traitor tracing for general access structures (beyond threshold) from two building blocks: attribute based encryption for general access structures and sufficiently-expressive policies and mixed functional-encryption. We also present two concrete instantiations. Under exponential security assumptions, we construct a pairings-based threshold traitor tracing scheme that can trace t traitors with ciphertext size O(t^2). We also construct an LWE-based traitor tracing scheme for a DNF access structure, that can trace an authorized subset of traitors with ciphertext size O(hat{t}^2), where hat{t} denotes the size of the largest unauthorized subset in the access structure. - A Candidate Theoretical Instantiation: We present a new tracing mechanism that can trace t(1-1/lambda^c) traitors with mathsf{poly}(lambda) size ciphertext, public key, and secret keys. We prove security assuming ideal (black box) obfuscation. Our work raises several open questions in the context of tracing multiple parties in a threshold traitor tracing scheme.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1523) | 2026-07-24
