---
title: "Default Correct: A New Fault Surface in the Comparison Booleanisation of Kyber-KEM"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2069"
summary: "The Fujisaki–Okamoto (FO) transform protects Kyber-KEM against chosen- ciphertext attacks and is based on a ciphertext comparison step. This comparison is usually treated as a single atomic check. How"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

The Fujisaki–Okamoto (FO) transform protects Kyber-KEM against chosen- ciphertext attacks and is based on a ciphertext comparison step. This comparison is usually treated as a single atomic check. However, in every mainstream implementation it is a short pipeline of independently faultable stages. It comprises a byte-wise mismatch accumulation, a two’s-complement Booleanisation, and a conditional move (cmov). In this work, we expose a previously unexamined stage of this pipeline, the Booleanisation, as a new attack surface. Our research reveals that a single sub-instruction clock glitch forces the mismatch flag fail to 0, so decapsulation accepts any ciphertext. Every prior fault attack on this comparison targets the equality test or the conditional move. So does the only countermeasure proposed for it: the default-fail cmov ordering of Xagawa et al. Our surface sits upstream of that move, so it escapes both. We instantiate this Default Correct fault on an ARM Cortex-M4 (ChipWhisperer-Lite) and demonstrate it across the pqm4, PQClean, and reference implementations of Kyber-512/768/1024 at all optimisation levels (-O0–O3). Crucially, every one of these implementations already carries Xagawa’s default-fail ordering, yet the fault succeeds on all of them: the surface is therefore not merely new but structurally beyond the reach of the state-of-the-art defence for this comparison. The Booleanisation is thus a single point of failure common to all three code bases. Leveraging the accept-everything behaviour, we use the standard plaintext-checking oracle and recover the full secret key of Kyber-512, Kyber-768, and Kyber-1024 in a single on-device run each. Finally, we analyse why defences that protect only the cmov or a single fail flag cannot address a fault that targets an upstream stage of the comparison, and we propose a producer-side countermeasure: an integrity-checked Booleanisation that computes the same flag while folding in an execution counter, so that any partial instruction skip is detected, at negligible overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2069) | 2026-09-17
