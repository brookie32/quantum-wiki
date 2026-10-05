---
title: "Revisiting Partitioning: Output-Adaptive ABE for Circuits from LWE"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2305"
summary: "We introduce Output-Adaptive Security, a new intermediate security notion for Attribute-Based Encryption (ABE) that bridges the gap between selective and full adaptive security. In our model, the adve"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We introduce Output-Adaptive Security, a new intermediate security notion for Attribute-Based Encryption (ABE) that bridges the gap between selective and full adaptive security. In our model, the adversary selectively commits to a policy function structure f but adaptively chooses a long target output value y during the challenge phase. We construct the first Output-Adaptive ABE scheme for general circuits from the standard Learning With Errors (LWE) assumption by revisiting classical partitioning techniques and applying them to the output space of circuit evaluation. Our result demonstrates that adaptivity for expressive policies can be achieved from standard lattices without complexity leveraging or heavy tools like witness encryption and indistinguishability obfuscation. Furthermore, we show that output-adaptivity is sufficient for many real-world applications, including biometric matching, weighted thresholds, and wildcard search, where system architecture is static while policy targets remain dynamic.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2305) | 2026-10-02
