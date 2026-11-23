---
title: "A Two-Party Threshold Signature Scheme for Aigis-sig"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2987"
summary: "Aigis-sig uses Fiat--Shamir with aborts. Its rejection step depends on the full response, which complicates threshold signing. We present ThAigis-2P, a two-party threshold signature scheme whose outpu"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Aigis-sig uses Fiat--Shamir with aborts. Its rejection step depends on the full response, which complicates threshold signing. We present ThAigis-2P, a two-party threshold signature scheme whose outputs are accepted by the unmodified Aigis-sig verifier. The parties sample their secret shares independently from the Aigis-sig key distribution, subject to a spectral screening condition. Each party samples masks from a scaled hyperball and performs rejection sampling locally. The protocol runs K candidates per attempt. The spectral screening condition bounds the secret shift for every challenge and contributes approximately one bit of conditioning loss to the security reduction. The protocol has a three-round interactive mode and a preprocessing mode that exchanges commitments offline and requires one online round trip per attempt using committed salts and single-use records. In the random oracle model, the security analysis relates unforgeability to AMLWE under the Aigis-sig key distribution, MLWE under hyperball distributions, and the unforgeability of native Aigis-sig. The preprocessing mode also assumes a rollback-resistant state service. Experiments with a single-process C reference implementation based on PQMagic yield success probabilities of 0.22--0.25 per candidate and above 0.92 per attempt with K = 10. All 39,000 generated threshold signatures pass Aigis-sig verification. Canonical lossless encoding reduces partial response sizes by 21/%--25/% relative to transmitting raw coefficients. The evaluation covers all three Aigis-sig parameter sets and measures computation in a single-process prototype.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2987) | 2026-11-22
