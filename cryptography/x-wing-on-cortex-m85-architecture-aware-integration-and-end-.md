---
title: "X-Wing on Cortex-M85: Architecture-Aware Integration and End-to-End Evaluation"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2352"
summary: "X-Wing combines ML-KEM-768 and X25519 for hybrid key establishment. On Cortex-M85, we adapted the coefficient representation and storage order of an MVE NTT to the existing ML-KEM path and optimized d"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

X-Wing combines ML-KEM-768 and X25519 for hybrid key establishment. On Cortex-M85, we adapted the coefficient representation and storage order of an MVE NTT to the existing ML-KEM path and optimized data-format transformations and X25519 arithmetic while preserving draft-10. During encapsulation, the two X25519 results share an inversion. We compared the eight-technique integrated implementation B8 with the baseline A0 in the same executable. Across ten paired comparisons from five independent reflashes of one EK-RA8M1 board, the minimum reported cycle reductions were 18.61% for key generation, 18.89% for encapsulation, 12.25% for decapsulation reusing an expanded key, and 15.22% for decapsulation including seed expansion. Nonvolatile storage increased by 35,692 B, including a 33,024 B fixed-base table. We separately report the cost and validation of B8S, which corrects identified secret-sign-dependent operand-address selections in B8. Some key-varying tests retained timing signals after this correction. Their causes remained partly unresolved, so no whole-program constant-time pass is claimed for B8S.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2352) | 2026-10-05
