---
title: "KORD: Breaking the Key-Generation Bottleneck in Dealerless Function Secret Sharing via Protocol–Hardware Co-Design"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1615"
summary: "Function secret sharing (FSS) has become a core primitive in privacy‑preserving computation. However, each FSS invocation requires a fresh pair of function keys, typically produced by a trusted dealer"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Function secret sharing (FSS) has become a core primitive in privacy‑preserving computation. However, each FSS invocation requires a fresh pair of function keys, typically produced by a trusted dealer—a dependency that expands the system's trust boundary and hinders practical deployment. Existing dealerless protocols eliminate this dependency, but incur substantial communication and a number of interaction rounds that grows linearly with the input bit‑width, making key generation a major bottleneck. This paper presents KORD, a protocol–hardware co‑design that dramatically reduces the cost of dealerless FSS key generation. At its core is a pair of chips that establish a common root of trust through mutual attestation and, within it, reconstruct FSS keys—eliminating the need for a dealer. This root of trust further forms a security boundary within which KORD restructures the generation protocol, collapsing the interaction of prior dealerless protocols into a single round, independent of GGM depth. A cross‑key scheduling scheme then interleaves independent GGM‑tree traversals, sustaining high computational throughput. KORD reduces key‑generation communication per operation by 7{,}633–70{,}274imes over the state‑of‑the‑art distributed FSS protocol. On a ZCU102 FPGA, cross‑key interleaving lifts AES lane utilization from 8.3% to a board‑measured 99.0%, for 11.60 million 32-bit DPF keys per second at 187.5,ext{MHz} on a 21.5,ext{K} LUT engine (12.38,ext{M} at the separately validated 200,ext{MHz} operating point). On private ResNet‑18 inference, key generation's share of end‑to‑end time falls to 10.1%, from 82.6% under a trusted dealer and over 96% under the dealerless baseline.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1615) | 2026-08-05
