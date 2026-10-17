---
title: "DPA-style Attacks on VOLE-in-the-Head Signature Schemes"
date: "2026-10-17"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2519"
summary: "VOLE-in-the-Head (VOLEitH) has emerged as a promising paradigm for the design of post-quantum signatures, as it enables efficient signing and verification while also achieving small signature sizes. I"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

VOLE-in-the-Head (VOLEitH) has emerged as a promising paradigm for the design of post-quantum signatures, as it enables efficient signing and verification while also achieving small signature sizes. In the ongoing NIST PQC standardization process for additional digital signatures, two VOLEitH signature schemes, namely FAEST and SDitH, have advanced to the third round. Regarding their practical security, especially resistance to power side-channel attacks, existing studies have focused on only a few specific operations, and thus a comprehensive analysis remains lacking. To address this gap, we present, to the best of our knowledge, the first DPA-style attack framework against VOLEitH signatures. Our framework targets the secret witness, whose recovery permits the generation of valid signatures for arbitrary messages. Based on this framework, we systematically analyze the leakage stemming from the computation of sensitive intermediate values involved in VOLE correlations, and characterize how such leakage can be linked to secret witness hypotheses for mounting DPA-style attacks. As a consequence, we propose six classes of DPA-style attacks on FAEST and SDitH, including two vertical and four horizontal attacks. Finally, the proposed attacks are validated using both simulated leakage under varying noise conditions and practical measurements on three ARM Cortex-M4 devices, demonstrating their effectiveness in both settings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2519) | 2026-10-17
