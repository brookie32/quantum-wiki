---
title: "Construction and Classification of Minimum-Latency 5-Bit APN S-Boxes"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2719"
summary: "S-boxes serve as essential nonlinear building blocks in symmetric-key cryptography, where their cryptographic properties and hardware implementation costs jointly dictate the security and efficiency o"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

S-boxes serve as essential nonlinear building blocks in symmetric-key cryptography, where their cryptographic properties and hardware implementation costs jointly dictate the security and efficiency of lightweight primitives. This paper studies the construction and classification of minimum-latency 5-bit APN (Almost Perfect Nonlinear) permutations under a prescribed gate-delay model, using exact minimum latencies of Boolean component functions. Under the fixed gate-delay model of the NanGate 45nm standard cell library, we partition the search space into input-variable permutation (IP) equivalence classes to establish a comprehensive minimum-latency database covering all 5-input balanced nonlinear Boolean functions. This database delivers exact minimum latencies and gate-level implementations for all equivalence classes up to a latency of 150ps, while guaranteeing strict lower bounds on latency for classes exceeding that threshold, combining property filtering with circuit synthesis. We search the five affine equivalence classes of 5-bit APN permutations. For each affine transformation of the input, we use exact component-function latencies to select components with linearly independent masks and choose their polarities, obtaining S-box circuits without repeating gate-level synthesis for each candidate. Exhaustive search with latency-preserving input-variable permutation reduction establishes a minimum latency of 126.745ps over all 5-bit APN permutations under the prescribed gate-delay model, with explicit constructions attaining this minimum in every class.The classification results give the optimized latency distributions and numbers of optimal IP classes of input-affine transformations within each affine class. Comparisons with selected 5-bit S-box implementations under the same model show simultaneous reductions in some cases: latency decreases by 10.20%--29.18% and normalized gate area by 5.37%--27.69%, while preserving the original S-box mappings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2719) | 2026-11-02
