---
title: "Structural Cryptanalysis of the Eevee AEAD Family"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2496"
summary: "Eevee is a family of three AEAD modes, Umbreon, Jolteon, and Espeon, proposed at CCS 2023 for IoT-to-cloud secure computation. We analyze structural flaws in the algorithms of the supplied full-versio"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Eevee is a family of three AEAD modes, Umbreon, Jolteon, and Espeon, proposed at CCS 2023 for IoT-to-cloud secure computation. We analyze structural flaws in the algorithms of the supplied full-version specification and the proof steps underlying their online authenticated-encryption claims. An AD-free, two-encryption prefix distinguisher has advantage 1-2^{-n} in the ideal-forkcipher model, contradicting the specified online ideal object. Independently, the separable associated-data transform yields a four-encryption nonce-misuse distinguisher with advantage 1-2^{-n}, a deterministic AD-only forgery, and nonempty-message forgeries obtained from cross-domain state differences. These attacks contradict the advertised nonce-misuse bounds of Umbreon and Espeon. With nonce-respecting encryption queries, one two-block Jolteon encryption permits a fresh one-block forgery with the same tag, while Espeon's short-message path permits arbitrary AD substitution. We trace these counterexamples to failures of online-prefix consistency, conditional transcript distributions, domain separation, and checksum freshness in the original proof. The authenticity attacks follow from deterministic identities, and the privacy counterexamples persist with an ideal forkcipher. We derive corresponding requirements for AD processing and message finalization, and briefly summarize supporting checks of the published C routines. The central failures concern the mode design and cannot be resolved solely by correcting implementation encodings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2496) | 2026-10-15
