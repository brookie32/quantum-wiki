---
title: "A New Class of PRFs and Efficient VRFs from Isogeny-based Group Actions"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2856"
summary: "Polynomial-in-exponent pseudorandom functions (Poly-style PRFs) based on group actions have recently emerged as a promising framework for post-quantum cryptography, offering compact keys and efficient"
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

Polynomial-in-exponent pseudorandom functions (Poly-style PRFs) based on group actions have recently emerged as a promising framework for post-quantum cryptography, offering compact keys and efficient verifiability. However, the security of these constructions over composite-order class groups remains poorly understood. Prior work suggested that security is governed by the largest prime factor of the group order. In this work, we show that this intuition is flawed. We present two generic attacks demonstrating that the effective security of Poly-style PRFs is determined instead by the smallest prime factor of the group order. As a consequence, existing parameter choices, including CSIDH-512 and SCALLOP-based settings used in recent VRF constructions, are insecure. Our enhanced attack achieves advantage close to one with complexity O(sqrt{p}), where p is the smallest prime factor of the group order. To address this inherent vulnerability, we introduce a new design paradigm, {em restrict-then-expand}, and formalize a general class of multivariate polynomial PRFs (extsf{MP}-PRFs) from group actions. The key idea is to eliminate exploitable structure via carefully restricted input domains, and then recover expressiveness through a provably secure expansion technique. We show that extsf{MP}-PRFs unify and generalize existing constructions, including Naor-Reingold-style and Poly-style PRFs (with restricted input domains), while achieving security in the generic group action model with twists (GGAM^{mathsf{T}}) for arbitrary composite-order groups. In addition to this, our construction supports flexible polynomial-size input spaces with fixed output length and admits efficient and compact proofs of correct evaluation. Building on this framework, we obtain new group-action-based VRFs that are both practical and provably secure. At a proof-soundness level close to 128 bits, our VRF instantiation requires 320 group-action evaluations for either proof generation or verification, compared with approximately 69,000--109,500 group-action evaluations in prior work, while retaining short keys and proofs. Overall, our results establish a robust and efficient approach to constructing post-quantum PRFs and VRFs from group actions, resolving fundamental limitations of existing Poly-style designs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2856) | 2026-11-10
