---
title: "Tamper Sensing Meshes in Payment Terminals and Beyond"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2475"
summary: "Card Payment Terminals commonly use tamper sensing meshes to deter physical attacks on devices handling sensitive data such as cryptographic keys. Although their use of such meshes is frequently refer"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Card Payment Terminals commonly use tamper sensing meshes to deter physical attacks on devices handling sensitive data such as cryptographic keys. Although their use of such meshes is frequently referenced in research literature, the public record contains little research on their construction. Addressing this gap, in this paper we present the first comprehensive analysis of the practical implementation of tamper sensing meshes across a wide range of payment terminals, and some other devices such as ATM key pads and a data center HSM. We provide detailed photos of critical features. Based on our observations, we construct a taxonomy of mesh construction techniques. Our analysis reveals that most commercial devices use surprisingly simple construction techniques, and their structure size rarely approaches manufacturing limits. Based on our analysis, we identify a concise set of design patterns for the construction of secure tamper sensing meshes. We conclude that designing tamper sensing meshes that exceed the industrial state of the art is viable even using inexpensive and easily available manufacturing processes. Our set of design recommendations creates a foundation for both the practical tamper sensing mesh implementations and for future research into their design. Our results enable researchers to base test specimens on concrete evidence of industrial practice.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2475) | 2026-10-14
