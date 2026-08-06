---
title: "Triple Cryptanalysis of Isogeny-Based VRFs from Asiacrypt 2025"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1623"
summary: "Levin and Pedersen proposed at Asiacrypt2025 a new verifiable random function (VRF) based on a CGL-analogue hash function constructed from radical isogenies. Their construction applies the same secret"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Levin and Pedersen proposed at Asiacrypt2025 a new verifiable random function (VRF) based on a CGL-analogue hash function constructed from radical isogenies. Their construction applies the same secret radical-CGL walk to a public starting curve and a message-dependent curve, and uses an R1CS proof relation to show that the two walks use the same secret key. We present a two-stage attack on this construction. The first stage concerns the unspecified representation of the public key. The reported key size indicates that the public curve is stored as a (j)-invariant, whereas both the specified radical-CGL computation use two coefficients to represent a curve. By exploiting this form we can produce two different VRF outputs under the same public key and message, breaking the unique provability. Hence, the output of the radical-CGL computation must follow the specification. In the second stage, we exploit these coefficients to recover the VRF secret key. With (1536) queries, our implementation recovers the complete (256)-bit secret in 30 minutes, thereby breaking residual pseudorandomness. Interestingly, we also observe that the using public key alone without queries can sometimes reveal one or two bits of the secret walk. Besides, we extend Lai's observation to obtain a one-query attack on the group-action-based VRF proposed in the same paper with advantage closed to 1/2. Together, these constitute three attacks on their work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1623) | 2026-08-05
