---
title: "Practical Fixed-Plaintext Key Collisions on Reduced-Round AES"
date: "2026-11-23"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3009"
summary: "We study chosen-key collisions on reduced-round AES under the fixed zero plaintext P = 0^{128}, i.e., key pairs K neq K' with AES_K^{(R)}(0^{128}) = AES_{K'}^{(R)}(0^{128}). This setting directly affe"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

We study chosen-key collisions on reduced-round AES under the fixed zero plaintext P = 0^{128}, i.e., key pairs K neq K' with AES_K^{(R)}(0^{128}) = AES_{K'}^{(R)}(0^{128}). This setting directly affects the key-committing security of AES-based authenticated encryption and corresponds to one-block collisions on AES in Davies-Meyer mode with IV = 0^{128}. Fixing the plaintext locks the Round-1 input to K^0, coupling the cipher state to the key schedule in non-linear cycles that stall standard guess-and-determine rebound solvers. On 4-round AES-128 and 7-round AES-256, we break these cycles using linear combinations of MixColumns rows and key-schedule columns that cancel coupled inactive S-boxes and isolate one- and two-byte non-linear equations solvable via small lookup tables. Combining this elimination with an 8-dimensional truncated differential space yields the first practical one-block collision on 4-round AES-128 with a fixed 0 plaintext in approx 2^{43.7} AES evaluations. On 7-round AES-256, eliminating all five internal conflicts together with truncated Round-7 matching reduces the classical cost from 2^{70} to approx 2^{38.3} AES evaluations. On 6-round AES-192, where the 6-word key schedule prevents sparse eliminations, we combine F_2-linearization of active DDT entries with an interleaved meet-in-the-middle list-merging tree, achieving the first classical one-block collision below the 2^{64} birthday bound. We verify all three attacks experimentally and provide a colliding key pair for each variant.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3009) | 2026-11-23
