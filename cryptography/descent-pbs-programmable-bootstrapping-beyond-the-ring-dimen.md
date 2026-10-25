---
title: "Descent-PBS: Programmable Bootstrapping beyond the Ring Dimension"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2616"
summary: "Programmable bootstrapping (PBS) in FHEW/TFHE evaluates a lookup table (LUT) while refreshing a ciphertext, but a t-entry negacyclic table must fit, with redundancy, into the 2N signed rotation positi"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Programmable bootstrapping (PBS) in FHEW/TFHE evaluates a lookup table (LUT) while refreshing a ciphertext, but a t-entry negacyclic table must fit, with redundancy, into the 2N signed rotation positions of a ring accumulator. Module bootstrappings, namely extended bootstrapping (PKC'23), monomial-matrix bootstrapping (TCC'25) and their successors, rotate a redundant table once in a module of rank tau, at a cost linear in both the rank and the redundancy. Meta-PBS (CCS'26) removes the redundancy by iterating the rotation in the ring, but supports plaintext moduli only up to 2N, and running it inside the module pays the rank in every rotation. We present Descent-PBS, which pays the module rank of a large table only in its first rotation. We prove that for a module secret embedded from the subring, truncation commutes with the secret, so one public functional key switch with merged columns repacks all tau_0 components of a module accumulator into the ring and removes the per-component factor tau_0 of repacking. The bootstrapping then continues with Meta-PBS refinements in the ring, at tau_0 + K instead of (K'+1) tau_0 external products per key. For block one-hot secrets, the first-rotation exponents are multiples of tau_0, so every combined key is a scalar matrix: the tau_0 components share one key per block, and since all exponents are public in advance, one pass over the bootstrapping key builds the keys of all rotations of a negacyclic table. Ties-to-even gadget rounding removes a refinement bias that we trace to half-up rounding on the FFT grid. In a TFHE-rs-based engine, Descent-PBS evaluates a 16-bit negacyclic LUT in 196 ms on one thread at 128-bit security and a model-predicted failure probability below 2^-64. With the same keys and failure budget, the descent alone makes it 1.44-2.40x faster than Meta-PBS run inside the module for dense secrets; for block one-hot secrets, the descent and the shared keys together make it 1.51-3.32x faster, and 1.37-3.57x against the same baseline re-planned for more conservative 131-bit parameters. General 13-16-bit LUTs take 179-368 ms, 3.8-6.6x faster than WoP-PBS in its authors' configuration on the same single-ciphertext interface, at about twice its memory. The failure probabilities are predictions of a model that we validate where failures are observable, and the 16-bit keys take 1,208 MB.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2616) | 2026-10-23
