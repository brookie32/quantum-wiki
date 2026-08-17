---
title: "DumboMix: Robust Asynchronous Anonymous Broadcast Made Practical"
date: "2026-08-15"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1699"
summary: "We present a practical framework mathsf{DumboMix} for asynchronous anonymous broadcasts with guaranteed output delivery (G.O.D., a.k.a. robustness), enabling a set of n servers to privately solicit N "
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

We present a practical framework mathsf{DumboMix} for asynchronous anonymous broadcasts with guaranteed output delivery (G.O.D., a.k.a. robustness), enabling a set of n servers to privately solicit N messages from distinct clients, such that these messages remain secret until they are simultaneously revealed in a uniformly random order. Here, asynchronous G.O.D. ensures that all solicited messages will eventually be randomly mixed despite (i) arbitrary malicious behaviors by up to n/3 Byzantine servers and (ii) unpredictable network delays and jitters. At the core of mathsf{DumboMix}, we first propose a couple of practical arithmetic circuits mathsf{DumboMix1} and mathsf{DumboMix2} for mixing in Shamir-secret-shared multi-party computation (MPC) over Z_p, along with their server-optimized variants. When randomly mixing N messages, their online phases require only O(1) multiplicative depth, expected O(N^2) scalar multiplications (between public and shared values), and up to O(N) MPC multiplications (between shared values). Moreover, assuming a robust underlying MPC framework, they guarantee that all revealed inputs are uniformly shuffled. In contrast, existing techniques fail to achieve all these performance and functionality features: The DC-net variant mathsf{Blinder} (CCS’20) may reveal a non-negligible fraction of inputs without shuffling them; Butterfly switching networks in secret-shared MPC (CCS’19) incur O(log^2 N) multiplicative depth; RabbitMix (Security’24) requires O(N^2) MPC multiplications; and PowerMix (CCS’19) incurs N^{3}/2 scalar multiplications. We also implement our mixing methods within mathsf{DumboMPCext{++}}, our computation-optimized implementation of the state-of-the-art robust AMPC framework mathsf{DumboMPC} (Security’25), which provides more concretely efficient offline preprocessing while preserving asynchronous G.O.D. and optimal resilience. We then conduct extensive evaluations with n=4 to 31 servers under varying network settings, revealing that our new mixing circuits achieve 44.8--65.9× (resp. 37.1--52.7×), 4.8--7.1× (resp. 3.9--5.5×), and 2.7--4.0× (resp. 5.1--7.2×) speedups over RabbitMix, PowerMix, and the butterfly switching network, respectively, when shuffling 1024 messages in LAN (resp. WAN).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1699) | 2026-08-15
