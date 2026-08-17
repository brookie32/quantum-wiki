---
title: "On the Impossibility of Robust Combiners for Cryptographic Groups"
date: "2026-08-15"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1695"
summary: "A (k,n)-robust combiner for a primitive P combines n candidate instantiations of P into a single scheme that remains secure as long as at least k of them remain secure. Robust combiners have been exte"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

A (k,n)-robust combiner for a primitive P combines n candidate instantiations of P into a single scheme that remains secure as long as at least k of them remain secure. Robust combiners have been extensively studied for primitives such as hash functions, public-key encryption, and oblivious transfer, but much less is known in the setting of cryptographic groups. In this work, we initiate the study of robust combiners for cryptographic groups in Maurer's generic group model (GGM), where algorithms access group elements only through abstract algebraic operations. We ask whether one can combine n candidate groups into a single group that remains secure provided that at least k of the underlying groups remain secure. A natural baseline is the direct-product construction, which preserves search hardness but fails for decisional assumptions and incurs substantial representation overhead. We show that these limitations are in fact inherent. Our first result is a complete impossibility for the decisional Diffie--Hellman assumption: for every polynomially bounded n and k with k<n, there is no generic (k,n)-robust combiner for cryptographic groups that preserves DDH security. Our second result gives a tight threshold for search assumptions in the regime where n and k are fixed constants. For the discrete logarithm problem, robust generic combination is possible when the combined group order is large enough to encode the secrets of n-k+1 components; concretely, if log N ge (n-k+1)lambda, where the component groups have distinct lambda-bit prime order, then a robust combiner exists. Conversely, if log N le (n-k)lambda, then no generic (k,n)-robust DLog-secure combiner exists. These results identify a fundamental limitation of robust hedging at the group level. Decisional assumptions such as DDH cannot be robustly combined in the GGM, while search assumptions admit robustness only at essentially optimal representation cost. Consequently, robustness for group-based cryptography must in general be achieved at higher layers, such as protocol design or key derivation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1695) | 2026-08-15
