---
title: "Relect: Single Secret Leader Election via FHE with Reduced Computation and Communication and Transparent Setup"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1619"
summary: "In a single secret leader election (SSLE) protocol, all parties collectively and obliviously elect one leader. Parties other than the selected leader should not be able to learn the identity of the le"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

In a single secret leader election (SSLE) protocol, all parties collectively and obliviously elect one leader. Parties other than the selected leader should not be able to learn the identity of the leader unless it is revealed by the leader itself. The problem is first formalized by Boneh extit{et al.} (AFT 2020), and the first concretely feasible lattice-based SSLE with proof-of-concept implementations, mathsf{Qelect}, was recently introduced by Wang and Zhang (USENIX 2025). In this work, we present mathsf{Relect}, an efficient SSLE protocol, based on the Ring Learning with Error assumption. We build it by leveraging the algebraic structure of the underlying threshold Fully Homomorphic Encryption (FHE) and by designing tailored homomorphic circuits. Compared to prior works, mathsf{Relect} (1) achieves substantially higher efficiency and (2) removes the strong environment assumption in mathsf{Qelect} (a trusted setup), and thereby also allows dynamic leader selection for each round. Concretely, for 32 -- 2048 parties, our local FHE computation runtime (a major efficiency bottleneck for SSLE) achieves 7.15 -- 42.4imes faster than mathsf{Qelect} for a single thread and 7.10 -- 48imes faster for 16 threads. Furthermore, we show that for the same parameters, our communication cost is also 1.14 -- 2imes smaller. As mentioned, this is achieved while removing the trusted setup. In terms of end-to-end runtime, following mathsf{Qelect}, we tested 2 -- 128 parties. We show that under the LAN setting, mathsf{Relect} is 2.77 -- 345imes faster than mathsf{Qelect} per round. Under the WAN setting, mathsf{Relect} is 1.94 to 17.2imes faster than mathsf{Qelect}. Note that these performance gains are all achieved while removing the trusted assumption and achieving dynamic leader selection for each round.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1619) | 2026-08-05
