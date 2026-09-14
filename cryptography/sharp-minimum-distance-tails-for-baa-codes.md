---
title: "Sharp Minimum-Distance Tails for BAA Codes"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2007"
summary: "Fast randomized linear codes used in pseudorandom correlation generators and code-based proof systems require quantitative guarantees on the probability of sampling a code with insufficient distance. "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Fast randomized linear codes used in pseudorandom correlation generators and code-based proof systems require quantitative guarantees on the probability of sampling a code with insufficient distance. For chosen-block Block--Accumulate--Accumulate (BAA) codes, prior work provides finite-length upper bounds, sparse failure mechanisms, and permutation obstructions that persist under every nonzero coordinate scaling. We determine the global minimum-distance lower tail across field sizes. For a fixed-length constituent of minimum distance dge2, sufficiently small fixed elta>0, and Q=q-1, we prove, uniformly over finite fields and constituent coefficients, [ PP[d_{min}lefloor{elta N}] =Theta!left(N^{1-d} +N^{1-eil{d/2}}Q^{-floor{d/2}}right). ] A support-dependent weighted-gap estimate controls every active-block count and every cancellation layer. It identifies linear field growth as the exact order needed for the N^{1-d} law. Certified extensions reach distance 0.30 for [16,8,9]_q MDS blocks and 0.60 for [16,4,13]_q MDS blocks over all qge2^{20}; binary instances reach their stated useful thresholds. For the two MDS families, when Q/Noinfty, we further prove that the known marked one-block coefficient is the leading constant of the actual failure probability. Grouping full-block gap events and bounding their dependence gives near-exact two-sided finite certificates at the published large-field benchmarks. These show that the existing numerical guarantees are essentially optimal for the unchanged ensemble. keywords{Random linear codes and BAA codes and Minimum distance and Pseudorandom correlation generators and Sampling failure}

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2007) | 2026-09-13
