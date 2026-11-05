---
title: "Challenge Binding in FRESCO SPDZ2k: A Message-Level Case Study"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2743"
summary: "FRESCO's SPDZ2k suite derives its batched MAC-check coefficients from a setup-time public seed, making the stream predictable before opening shares are sent. We examine this implementation path at a p"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

FRESCO's SPDZ2k suite derives its batched MAC-check coefficients from a setup-time public seed, making the stream predictable before opening shares are sent. We examine this implementation path at a pinned revision. A source-level derivation accounts for low-limb carries and high-bit corrections and shows that the value-share shifts e=(r_j,-r_i) preserve the check residual while retaining the original MAC shares. A message-level harness executes this deviation against unmodified honest opening code. The recorded sum/product outputs violate a relation required for every possible input of the corrupt party, and the test framework records normal completion. The retained evidence includes two-, three-, and four-party executions with dummy preprocessing. The predictable-seed attack template appears in Rushing at SPDZ, and FRESCO's issue tracker recorded the per-check randomness requirement in 2018; our contribution is the SPDZ2k public-seed path, its explicit kernel witness, and the implementation evidence. We also give a conditional single-opening analysis and assess a four-file candidate mitigation that rejects seven recorded tampering scenarios while preserving four honest baselines. Audit tools and descriptive corpora provide context. The proof concerns the specified value-share deviation; unrestricted malicious behavior, production preprocessing, and a complete mitigation argument remain outside the established result.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2743) | 2026-11-03
