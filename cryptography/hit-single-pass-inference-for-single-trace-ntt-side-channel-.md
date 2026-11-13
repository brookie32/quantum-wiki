---
title: "HIT: Single-Pass Inference for Single-Trace NTT Side-Channel Attacks"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2865"
summary: "In physical implementations of the post-quantum standards ML-KEM and ML-DSA, the Number-Theoretic Transform (NTT) directly processes secret polynomials and is a primary target for single-trace side-ch"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

In physical implementations of the post-quantum standards ML-KEM and ML-DSA, the Number-Theoretic Transform (NTT) directly processes secret polynomials and is a primary target for single-trace side-channel key recovery. Existing Soft Analytical Side-Channel Attacks (SASCA) apply loopy Belief Propagation (BP) over cyclic Z_q factor graphs, where BP fails under high noise and O(q^2) updates make ML-DSA infeasible. We present the Hierarchical Inference Tree (HIT), a framework built on the insight that small secret inputs deterministically fix all NTT intermediates across the recursive butterfly network. Instead of loopy BP, HIT merges and prunes candidate inputs from leaves to root in a single pass on an acyclic binary tree. This approach eliminates belief oscillation, guarantees a constant runtime, and decouples complexity from q. On ML-KEM-768, HIT runs over 900imes faster than state-of-the-art SASCA and more than doubles noise tolerance. HIT also enables the first single-trace analytical attack on the ML-DSA NTT and recovers each polynomial in under one second. On physical ARM Cortex-M4 targets, HIT achieves over 98% polynomial recovery across both standards with only 20 to 80 profiling traces.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2865) | 2026-11-11
