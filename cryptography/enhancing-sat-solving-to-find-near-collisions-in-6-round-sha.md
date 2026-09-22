---
title: "Enhancing SAT Solving to Find (Near) Collisions in 6-Round SHA-3 Variants"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2107"
summary: "The Keccak hash function, designed by Bertoni et al., was selected as the new generation of Secure Hash Algorithm (SHA-3) in 2012. For NIST-standardized SHA-3 instances (SHA3-224/256/384/512, SHAKE128"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The Keccak hash function, designed by Bertoni et al., was selected as the new generation of Secure Hash Algorithm (SHA-3) in 2012. For NIST-standardized SHA-3 instances (SHA3-224/256/384/512, SHAKE128, SHAKE256), practical collision attacks have reached five rounds; six-round SHAKE128 was known only as a theoretical attack with cost 2^{123.5} six-round evaluations~ite{tuyi2022sha3}. In this paper, we present the first classical practical collision attack on six-round SHAKE128 with d{=}160 and total complexity about 2^{47.82}. Building on the Dinur-framework Dinur et al.~ite{dinur2012new} and the SAT tooling of Guo et al.~ite{tuyi2022sha3}, we introduce a parameterized colliding-trail SAT model--- collision length in digest and weight bounds are chosen at setup together with leaner differential encodings. Specifically, we introduce an enhanced heuristic strategy to identify suitable differential trails and employ multiple techniques to optimize the connectors: for the connector phase, we minimize weighted propagation cost of second round and third round, and penalize costly DDT{=}2 transitions; candidate hi-compatible equations are chosen by a bit-granular greedy routine that maximizes connector degrees of freedom. In addition to SHAKE128, we report six-round extbf{near}-collisions on SHA3-224 and SHA3-256 (four and six differing digest bits, respectively), and practical collisions on four- and five-round SHAKE256 with the full 512-bit digest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2107) | 2026-09-19
