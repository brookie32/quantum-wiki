---
title: "ML-DSA masking sweetened with SUCRE: Shuffle-and-Unmask Countermeasure for REjection sampling"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2248"
summary: "We present SUCRE, a novel countermeasure designed to physically protect the rejection sampling step of ML-DSA, one of the post-quantum signature schemes standardized by NIST. At the core of SUCRE is a"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

We present SUCRE, a novel countermeasure designed to physically protect the rejection sampling step of ML-DSA, one of the post-quantum signature schemes standardized by NIST. At the core of SUCRE is a masking gadget that securely unmasks a vector while simultaneously applying a random permutation of its coefficients. This lightweight mechanism preserves the vector’s infinity norm, enabling rejection sampling to proceed as usual without requiring any complex mask conversions. We formally prove that a d-probing adversary can learn at most some permuted rejected values---information which, we show, should remain insufficient to endanger the security of the signature scheme. This security argument relies on a new variant of the Module Learning with Rounding (MLWR) assumption, for which we provide a dedicated concrete security analysis to assess its hardness relative to the standard MLWR assumption. Our implementation of SUCRE achieves a significant performance improvement over previous masked non-bitsliced implementations of rejection sampling---delivering four to six times faster execution than Coron et al. (TCHES 2024)---albeit at the cost of increased memory usage. Since the rejection step accounts for approximately 25% of the total runtime in masked ML-DSA implementations, and given the expected adoption of ML-DSA on embedded platforms, this speedup could significantly enhance efficiency in real-world applications.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2248) | 2026-09-28
