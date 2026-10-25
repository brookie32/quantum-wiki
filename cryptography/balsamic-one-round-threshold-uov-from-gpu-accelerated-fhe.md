---
title: "Balsamic: One-round Threshold UOV from GPU-Accelerated FHE"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2604"
summary: "Universal thresholdizers offer one-round threshold signatures, but require evaluating an entire signer under fully homomorphic encryption (FHE). We present Balsamic, a complete homomorphic Unbalanced "
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Universal thresholdizers offer one-round threshold signatures, but require evaluating an entire signer under fully homomorphic encryption (FHE). We present Balsamic, a complete homomorphic Unbalanced Oil and Vinegar (UOV) signer and its application to one-round threshold UOV signature. UOV's short salted target hash shifts the encrypted workload to finite-field linear solving, which we integrate with coin derivation and hashing in a packed discrete-CKKS circuit. Our paired-pivot solver selects both pivots before first-pivot normalization, then applies their coupled update with one inversion stage per pair and cubic field work. Pivot-success certificates enable encrypted retry selection without residual evaluation. In 2-out-of-3 semihonest threshold UOV signing, each partial signing (online) takes 10.7 seconds on NVIDIA RTX 6000 Ada and 7.77 seconds on NVIDIA GB300, with 5.25 MB per response. These measurements demonstrate that complete homomorphic signing can provide the computational core of one-round threshold signatures without intermediate openings or per-signature interactive preprocessing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2604) | 2026-10-22
