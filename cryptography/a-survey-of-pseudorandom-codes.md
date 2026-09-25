---
title: "A Survey of Pseudorandom Codes"
date: "2026-09-22"
updated: "2026-09-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2162"
summary: "A pseudorandom code (PRC) is a cryptographic primitive combining pseudorandom encryption and error-correcting codes (Christ and Gunn, CRYPTO 2024). That is, any polynomial number of codewords are pseu"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

A pseudorandom code (PRC) is a cryptographic primitive combining pseudorandom encryption and error-correcting codes (Christ and Gunn, CRYPTO 2024). That is, any polynomial number of codewords are pseudorandom, and decryption tolerates a constant rate of bit-flips. Although this might seem like a natural combination of standard properties, it is a fundamentally new object: PRCs are black-box separated from many primitives, including one-way functions, public-key encryption, and even virtual black-box obfuscation (Döttling et al., Garg et al., TCC 2025). Pseudorandom codes were introduced to build watermarks for AI-generated content. In particular, they imply watermarks that preserve the model's quality in a strong sense and withstand modification of the content. This relationship makes pseudorandom codes an inviting area for researchers: improvements to this simple theoretical object yield better watermarks. Beyond watermarks, PRCs have been used to construct error-correcting codes against computationally bounded channels (Lu et al., CRYPTO 2026), and techniques underlying them have led to new public-key encryption schemes (Döttling et al., CRYPTO 2026, Dyseryn et al. ASIACRYPT 2026). This survey aims to equip the interested researcher with tools to make progress in the area. We detail the current landscape of definitions, techniques, and applications. A main contribution is introducing new tricks and assembling existing tricks to generically strengthen PRCs (e.g., from substitution-robustness to random-deletion-robustness). We also show natural weakenings of PRCs that can be constructed from OWFs or even unconditionally. We conclude with a number of concrete open questions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2162) | 2026-09-22
