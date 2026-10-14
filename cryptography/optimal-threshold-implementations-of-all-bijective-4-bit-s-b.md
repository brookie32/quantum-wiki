---
title: "Optimal Threshold Implementations of all bijective 4-bit S-boxes and new Infinite Families"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2449"
summary: "Threshold implementations (TIs) are now an established class of side-channel countermeasures. Their underlying idea is simple and compelling: under mild, practical assumptions, they provide protection"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Threshold implementations (TIs) are now an established class of side-channel countermeasures. Their underlying idea is simple and compelling: under mild, practical assumptions, they provide protection against glitches and allow composability. Yet our understanding of one-stage TIs with a minimal number of shares remains limited, both for cryptographically relevant families—particularly power functions—and for concrete small functions. In particular, until now, except for Feistel-constructions, no optimal TI had been found for families of mathematically well-structured and cryptographically non-trivial functions, especially power functions. In small dimensions, many functions - particularly cryptographically interesting ones — were not known to admit an optimal TI. This was especially true for the 4-bit S-boxes frequently used in practical lightweight ciphers. Optimal refers to share-optimal, direct one-stage, uniform, first-order TI. Here, we introduce new families of TIs, including the first infinite families of cryptographically nontrivial power permutations. Moreover, every four-bit permutation of algebraic degree t admits a direct, uniform TI with t+1 shares and no fresh randomness. Those results prove several previous conjectures and claims wrong. Since such permutations are widely used in symmetric ciphers, our constructions offer new implementation options.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2449) | 2026-10-12
