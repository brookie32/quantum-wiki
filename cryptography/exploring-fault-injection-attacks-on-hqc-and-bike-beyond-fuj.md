---
title: "Exploring Fault Injection Attacks on HQC and BIKE Beyond Fujisaki-Okamoto Verification"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2492"
summary: "Fault injection attacks have been extensively studied in the context of post-quantum cryptography, yet existing analyses on code-based KEMs largely focus on faults targeting the Fujisaki-Okamoto trans"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Fault injection attacks have been extensively studied in the context of post-quantum cryptography, yet existing analyses on code-based KEMs largely focus on faults targeting the Fujisaki-Okamoto transform. This work presents new fault injection attacks against BIKE and HQC that operate beyond this commonly protected component and target less obvious instructions within the decapsulation process. The proposed attacks achieve full key recovery using only valid ciphertexts under NIST Level 1 parameters, requiring 17392 and approximately 3 million decapsulation queries for HQC and BIKE, respectively. In addition, we introduce a general approach to identify effective fault locations by analyzing decoder behavior under perturbed conditions. The attacks are experimentally validated on an STM32H7 microcontroller using laser fault injection, demonstrating high repeatability. These results reveal a broader attack surface and provide a foundation for more efficient fault attack analyses in future work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2492) | 2026-10-15
