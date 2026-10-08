---
title: "SkrrtPIR: Doubly-Stateless Batch PIR from Single-Key RLWE Unpacking"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2385"
summary: "Batch Private Information Retrieval (Batch PIR) allows a client to privately retrieve multiple entries from a public database while amortizing query costs. However, concretely efficient schemes typica"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Batch Private Information Retrieval (Batch PIR) allows a client to privately retrieve multiple entries from a public database while amortizing query costs. However, concretely efficient schemes typically rely on per-client server state, such as client-specific evaluation keys, which makes queries linkable across sessions and complicates deployment. In this work, we initiate the study of doubly-stateless Batch PIR, where the server stores no per-client state and the client maintains no database-dependent hint. For this model, we construct a communication-efficient scheme that substantially reduces communication compared with the natural baseline of adapting off-the-shelf Batch PIR schemes by sending fresh evaluation keys with each batch query. The core technical ingredient is a single-key RLWE unpacking procedure that replaces the traditional tree-based approach, which requires logarithmically many Galois keys, with a linear walk over a cyclic Galois subgroup requiring only a single Galois key.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2385) | 2026-10-06
