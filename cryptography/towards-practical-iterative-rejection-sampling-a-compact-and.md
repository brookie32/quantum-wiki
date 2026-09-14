---
title: "Towards Practical Iterative Rejection Sampling: A Compact and Efficient Signature over Module Lattices"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1991"
summary: "Lattice signatures face a strict trade-off among compactness, implementation simplicity, and reliance on standard lattice assumptions: ML-DSA-44 requires a 2420-byte signature (3732 bytes combined) an"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Lattice signatures face a strict trade-off among compactness, implementation simplicity, and reliance on standard lattice assumptions: ML-DSA-44 requires a 2420-byte signature (3732 bytes combined) and HAETAE-120 takes 1474 bytes (2466 bytes combined), while Falcon-512 achieves 555 bytes but relies on complex floating-point arithmetic. We propose SHUTTLE, a compact Fiat–Shamir signature built on a standard MLWE public-key structure with unforgeability bound to MSIS in the random oracle model. At NIST Level I, SHUTTLE achieves a signature size of 1175 bytes (and 2167 bytes combined)—a 51% reduction in signature size over ML-DSA-44 and 20% smaller than HAETAE-120 using purely integer arithmetic. SHUTTLE resolves prior compact schemes’ limitations via three core techniques: (1) replacing secret-dependent rejection in the iterative sampling loop with a deterministic transition bounded by Rényi divergence, relegating restarts solely to public bounds and encoding checks (occurring with negligible probability approx 2^{-30}); (2) reformulating transition logic in the logarithmic domain into simple integer interval comparisons; and (3) employing an asymmetric stretch-and-compress mechanism to offset MLWE parameter expansion. By eliminating secret-dependent rejection from the inner loop, SHUTTLE achieves constant-time execution with fast signing (1406k cycles, about 3imes faster than HAETAE-120) and verification faster than ML-DSA-44.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1991) | 2026-09-12
