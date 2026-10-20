---
title: "CHARRM - Characterizing Hardware Leakage in the Robust Random Probing Model"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2552"
summary: "Masking is a prevalent countermeasure against passive physical implementation attacks such as Side-Channel Analysis (SCA). Despite its theoretical soundness, the practical application of masking is of"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Masking is a prevalent countermeasure against passive physical implementation attacks such as Side-Channel Analysis (SCA). Despite its theoretical soundness, the practical application of masking is often fraught with complexity and prone to errors, underscoring the necessity for automated security verification. This paper presents a comprehensive methodology for efficient security verification in the (g, t, c)-robust (p, epsilon)-random probing model. In particular, we advance the state-of-the-art concept of leakage characteristics to account for robust probe extension schemes across arbitrary circuit structures, enabling efficient leakage probability bound computation for glitch-extended and transition-extended robust probing scenarios. By further linking the leakage characteristic to the Set of Input Shares (SIS) function, we extend our verification methodology to established composability notions. Our automated reasoning framework demonstrates practicality and superior performance and accuracy for larger circuits in comparative evaluations with ironmask as state-of-the-art competitor. For the first time, our method allows for the exact verification of larger, composed circuit structures, validated by corresponding case studies. Consequently, this work advances the state-of-the-art in automated hardware security verification, providing a versatile tool for evaluating the security of masked cryptographic implementations against SCA in the presence of transient physical effects.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2552) | 2026-10-19
