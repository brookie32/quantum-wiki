---
title: "The Cost of Rewinding for Succinct Arguments: Strict-Time Barriers and Expected-Time Security"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2209"
summary: "Succinct arguments are central cryptographic objects, underlying various applications such as blockchains and image authentication. Almost all succinct arguments used in practice follow the commit-and"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Succinct arguments are central cryptographic objects, underlying various applications such as blockchains and image authentication. Almost all succinct arguments used in practice follow the commit-and-open paradigm introduced by Kilian (STOC 1992): commit to a probabilistic proof, then open the few locations the verifier queries. Decades of work have generalized and optimized this paradigm, yet its exact provable security in the standard model remains unclear. Existing analyses proceed by rewinding, and they leave gaps: strict-time analyses lose an inverse-polynomial factor, while expected-time analyses are sharper but apply only to special cases of this paradigm. We resolve both gaps. On the negative side, we show that the strict-time loss is inherent: no strict polynomial-time reduction relying on a black-box extractor can achieve negligible knowledge error (unless the underlying language is easy). On the positive side, we give a new expected-time analysis, achieving negligible soundness and knowledge errors via an expected polynomial-time reduction against expected polynomial-time adversaries, at the full generality of the paradigm, capturing multi-round and functional variants such as polynomial and linear IOPs compiled with the corresponding commitments. This is the first standard-model analysis to reach this regime for succinct arguments deployed in practice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2209) | 2026-09-25
