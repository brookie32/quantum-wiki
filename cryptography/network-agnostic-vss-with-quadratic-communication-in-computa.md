---
title: "Network-Agnostic VSS with Quadratic Communication in Computational Setting"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1993"
summary: "Verifiable secret sharing (VSS) is a core primitive in multiparty computation (MPC). Bhimrajka et al. [PKC'24, TIT'26] proposed the first computationally network-agnostic VSS and VSS-based MPC, which "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Verifiable secret sharing (VSS) is a core primitive in multiparty computation (MPC). Bhimrajka et al. [PKC'24, TIT'26] proposed the first computationally network-agnostic VSS and VSS-based MPC, which seamlessly accommodate both synchronous and asynchronous network models. However, their VSS requires Byzantine Agreement (BA) and incurs O(n^5) bits of communication per sharing among n parties, and their MPC requires honest participation from nearly all parties. We revisit the network-agnostic VSS architecture and propose a more efficient and general network-agnostic VSS structure. Our key technique is a new virtual-party strategy, which introduces more parties for reconstruction. With this technique, network-agnostic VSS is BA-free and performs as efficiently as synchronous VSS. Specifically, in terms of communication, our VSS costs O(n^2) bits in the one-shot case and O(n) bits in the round-by-round case with the dispute-control technique, yielding the first computationally network-agnostic VSS protocols with amortized linear communication complexity. Besides, we further address a series of subtle yet necessary hurdles in adapting existing results to network-agnostic models, including the erasure coding techniques in Reliable Broadcast (RBC), packed secret sharing techniques in VSS, and the correlated polynomial techniques in MPC.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1993) | 2026-09-12
