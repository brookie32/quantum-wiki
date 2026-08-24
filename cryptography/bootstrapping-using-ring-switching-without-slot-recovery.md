---
title: "Bootstrapping using Ring Switching without Slot Recovery"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1779"
summary: "Bootstrapping is a performance bottleneck in most ring-based FHE schemes, and ring switching can reduce its cost by moving computation from a large ring to smaller rings. However, for SIMD-packed ciph"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Bootstrapping is a performance bottleneck in most ring-based FHE schemes, and ring switching can reduce its cost by moving computation from a large ring to smaller rings. However, for SIMD-packed ciphertexts, ring switching is usually followed by a slot recovery step to restore the original slot layout, which consumes much “noise capacity”, leaving the remaining capacity insufficient for subsequent operations and impeding parallelism. In this paper, we show that slot recovery is not indispensable. For CKKS and BGV/BFV bootstrapping, we prove that their ring-switched realizations operate correctly without slot recovery. More generally, for CKKS over arbitrary real inputs, we prove that a continuous slotwise function can be evaluated independently on the ring-switched leaves without slot recovery if and only if the function is affine. Our results substantially improve bootstrapping performance by exploiting the inherent parallelism across the smaller rings, lowering the correction bounds, and reducing the complexity of CoeffToSlot and SlotToCoeff as the number of slots decreases. For CKKS with (N=2^{17}) and (n=2^{16}), our implementation outperforms direct bootstrapping in throughput by (99.7%)–(113.5%) with sparse-secret encapsulation and by (121.3%) with an alternative dense-key bootstrapper. For BGV at (p=65537), (N=2^{16}), and (n=2^{15}), our implementation achieves (3.16imes) and (1.46imes) speedups over partition-matched and capacity-comparable baselines, respectively. Furthermore, server key sizes are reduced by (16.4%)–(57.6%).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1779) | 2026-08-23
