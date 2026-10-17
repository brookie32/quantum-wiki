---
title: "Aerie: Efficient Aggregation of Falcon Signatures"
date: "2026-10-15"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2501"
summary: "The post-quantum signatures selected by NIST are ten to over a hundred times larger than the elliptic-curve signatures they replace. Moreover, unlike the BLS signatures that blockchains use to aggrega"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The post-quantum signatures selected by NIST are ten to over a hundred times larger than the elliptic-curve signatures they replace. Moreover, unlike the BLS signatures that blockchains use to aggregate validator votes, they do not aggregate natively. Both problems can be addressed with a SNARK: a short proof that a batch of signatures is valid, replacing the signatures themselves. The prevailing approach, central to Ethereum's roadmap, pairs hash-based signatures with hash-based SNARKs. This is slow because the prover must prove many hash evaluations per signature. We instead aggregate lattice-based signatures with a lattice-based SNARK. We present Aerie, a proof system for aggregating Falcon-512 and Falcon-1024 signatures. By retaining each signature's short random salt in the aggregate, Aerie lets the verifier compute the hashes directly. The proof then covers only algebraic and norm checks. Aerie combines protocols tailored to these checks with the Akita polynomial commitment scheme. Unlike prior Falcon aggregation schemes, it also proves that the signatures satisfy Falcon's byte-format requirements. On an Apple M4 Max laptop without GPU acceleration, Aerie aggregates 32,768 Falcon-512 signatures, roughly the number of validator votes in one Ethereum slot, in 0.65 seconds. A single proof covers the whole batch, with no recursion. The aggregate is 42.1 bytes per signature including the salts, or about 66 KiB in total if the signatures share one salt. It verifies in 54 milliseconds on one core, 10× faster than checking the signatures individually. On one core, proving takes only about 8× as long as individual verification. We prove knowledge soundness of Aerie in the classical random-oracle model and derive aggregate unforgeability from Falcon's security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2501) | 2026-10-15
