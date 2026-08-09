---
title: "Adaptive-Input-Secure Updatable Private Set Union"
date: "2026-08-06"
updated: "2026-08-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1626"
summary: "In multi-epoch deployments, private set union~(PSU) operates in an adaptive-input loop: after observing the union at epoch t, the receiver may choose its next input for epoch t+1. Liu et al.~(EUROCRYP"
last_verified: "2026-08-09"
review_by: "2026-11-07"
stale: false
---

In multi-epoch deployments, private set union~(PSU) operates in an adaptive-input loop: after observing the union at epoch t, the receiver may choose its next input for epoch t+1. Liu et al.~(EUROCRYPT 2026) formalized this multi-epoch adaptive-input setting for updatable private set intersection and provided an instantiation, but their framework does not extend to PSU. Meanwhile, existing PSU protocols are analyzed only in the single-shot setting. We present the first semi-honest, adaptive-input-secure updatable PSU protocol supporting two-sided add/delete updates in the multi-epoch adaptive-input setting of Liu et al. Our construction is built around a new primitive, the updatable oblivious key-value store (uOKVS). Its defining rule, distributional erasure, requires each refresh to be distributed identically to a fresh static encoding of the current key set, rather than merely indistinguishably. We realize uOKVS by combining the Band-OKVS of Bienstock et al. with a PRF under a persistent key. The resulting refresh reuses a cached factorization, so its per-epoch encoding cost scales linearly rather than quadratically in the band width w. Building on this layer, we obtain a multi-epoch PSU protocol whose leakage is limited to set and update cardinalities, even against adaptive-input adversaries. We implement the protocol and benchmark it in a single-threaded setting. At n = 2^{20} with per-epoch updates Delta = 55 over 10 epochs, the online per-epoch wall-clock time is 1.41 s on LAN, yielding a 30.9imes--98.9imes speedup over prior static PSU protocols re-executed from scratch at each epoch.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1626) | 2026-08-06
