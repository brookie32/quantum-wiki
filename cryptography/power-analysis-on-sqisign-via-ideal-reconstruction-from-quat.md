---
title: "Power Analysis on SQIsign via Ideal Reconstruction from Quaternion Leakages"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2508"
summary: "SQIsign is an isogeny-based signature scheme, which is one of the Round-3 candidates for NIST's additional post-quantum digital signature standardization. NIST considers resistance to side-channel att"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

SQIsign is an isogeny-based signature scheme, which is one of the Round-3 candidates for NIST's additional post-quantum digital signature standardization. NIST considers resistance to side-channel attacks as one important factor in evaluating digital signature schemes. However, side-channel analysis of SQIsign remains very limited. To the best of our knowledge, all existing studies target the Round-1 version, so their applicability to the substantially revised Round-3 SQIsign has not been established. Moreover, existing studies either provide experimental validation only for toy parameters or assume exploitable leakage without demonstrating its extraction in practice, leaving their applicability to realistic implementations unclear. In this work, we identify five side-channel vulnerabilities in the signing procedure of Round-3 SQIsign and provide polynomial-time algebraic algorithms that recover the secret key from the corresponding leaked intermediate values. Additionally, we further provide algorithms that enable the reconstruction of the complete secret key even when the side-channel leakage reveals only partial bits of an algebraic value, for each vulnerability. Finally, we further perform power analysis attack on the SQIsign source code, extracting the necessary leakage or its partial information for each vulnerability.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2508) | 2026-10-16
