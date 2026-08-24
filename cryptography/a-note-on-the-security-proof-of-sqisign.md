---
title: "A Note on the Security Proof of SQIsign"
date: "2026-08-22"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1775"
summary: "Aardal et al. (CRYPTO 2025) provided the first complete security proof of SQIsign; however, their reduction incurs a square-root loss in the prime characteristic due to the application of a loose boun"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Aardal et al. (CRYPTO 2025) provided the first complete security proof of SQIsign; however, their reduction incurs a square-root loss in the prime characteristic due to the application of a loose bound on the min-entropy. For instance, at NIST security level I, an adversary making 2^{64} signing queries renders the security proof vacuous. In this note, we show that the min-entropy of SQIsign is optimal, namely O(1/p). Although this improvement does not yield full lambda-bit security, we show that it preserves two-thirds of the expected bit-security. We show that this artifact comes from an information-theoretic loss in the zero-knowledge simulation of SQIsign, suggesting a new proof technique is needed to achieve full lambda-bit security at the current parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1775) | 2026-08-22
