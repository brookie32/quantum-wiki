---
title: "Optimal Amplification via Bias-Resilient Combiners"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2025"
summary: "Cryptographic combiners take n candidate schemes for some primitive P, and realize it securely provided that at least k candidates are secure. Intuitively, we expect that if we plug n independent inst"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Cryptographic combiners take n candidate schemes for some primitive P, and realize it securely provided that at least k candidates are secure. Intuitively, we expect that if we plug n independent instances of a elta-weak candidate for P into the combiner, assuming elta ll (n-k)/n, security should be amplified and the resulting candidate should exhibit a significantly smaller weakness. This intuition relies on the implicit “all-or-nothing” assumption that each candidate fails with probability elta and is otherwise perfectly secure, allowing us to bound the failure probability of the combiner using a simple binomial tail bound. However, this intuition often fails for standard security notions where, for example, a weak candidate may consistently leak partial information rather than exhibit a clean all-or-nothing failure. Recently, Applebaum, Bitansky and Geier (CRYPTO 2026) showed that indistinguishability combiners inherently act as security amplifiers. However, this general result incurs a multiplicative loss of roughly 2^{n-k} in the error parameter relative to the natural all-or-nothing bound. Moreover, the combiner-is-amplifier approach is fundamentally restricted to the regime elta < 0.5. Consequently, both the resulting error rate and the amplification threshold elta_0 are suboptimal. In this work, we overcome these limitations by establishing a new specialized framework of bias-resilient indistinguishability combiners. This formulation allows us to achieve the optimal all-or-nothing bound without the exponential penalty. We observe that bias-resilience provides a unifying abstraction for security amplification across different primitives, neatly capturing prior ad hoc results such as those for weak PRGs and weak NIZK. As our main application, we use this framework to establish a generalized XOR lemma over prime fields F_p, showing that the sum modulo p of independent weakly pseudorandom elements becomes computationally indistinguishable from uniform. This improves upon a recent work by Shimizu and Yasunaga (STOC 2026) by achieving a sample complexity that is independent of the field size. Finally, we explore the idealized notion of an all-or-nothing amplifier. We establish a tight characterization of the multiplicative penalty incurred when applying such an amplifier to candidate schemes that only guarantee standard weak indistinguishability error.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2025) | 2026-09-14
