---
title: "Associated-Data Correlations in Eevee: Deterministic Forgeries against Nonce-Misuse Security"
date: "2026-10-17"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2518"
summary: "Eevee's Umbreon and Espeon modes claim online authenticated-encryption security under nonce reuse. We give an independent analysis of associated-data correlations that yield probability-one non-empty-"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Eevee's Umbreon and Espeon modes claim online authenticated-encryption security under nonce reuse. We give an independent analysis of associated-data correlations that yield probability-one non-empty-message forgeries with three encryption queries and one verification query. Two AD-only tags reveal a mask difference that translates a ciphertext to another AD value. The basic attacks and their proof diagnosis overlap with independent and concurrent work by Mao et al. Our complementary contribution is a systematic affine treatment of partial final message blocks. For any admissible fixed final-fragment length r, n-r+3 encryption queries suffice; allowing the forged length to be r or r-h for a chosen 1 <= h < r < n, while choosing the source plaintext adaptively, reduces this to n-r+2. Both constructions satisfy the padding check and succeed with probability one. They apply to general message lengths, with at least one preceding complete block for Espeon. We also analyze the published short-message Espeon AD omission, validate the published complete-block Umbreon attack using the official ForkSkinny primitive in a specification adapter, and report a separate two-query attack accepted by the unmodified public C modes. Finalization is discussed only as an unproved countermeasure direction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2518) | 2026-10-17
