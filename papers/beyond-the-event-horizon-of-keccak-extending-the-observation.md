---
title: "Beyond the Event Horizon of Keccak, Extending the Observation from 2011 and applications"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2671"
summary: "In 2011 we observed that a single path in the Keccak sponge from a state whose capacity has all zero bits back to such a state yields an explicit, infinite family of second preimages for every message"
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

In 2011 we observed that a single path in the Keccak sponge from a state whose capacity has all zero bits back to such a state yields an explicit, infinite family of second preimages for every message of at least one full rate block. Finding such a path costs about 2^(c/2), which lies "beyond the event horizon" for SHA3-256 (c=512). In this paper we give three novel theorems around that observation. First, the capacity can have any value x: a two-block meet-in-the-middle loop from x back to x, found at heuristic cost about 2*2^(c/2), gives the same unlimited family of second preimages requiring no further search, with connectors to and from x at about the same cost again (Theorem 1). Theorem 2 extends this to k-block loops and to cycles of the capacity map. A single-state bridge, a state S with cap(f(S)) = cap(f^-1(S)), where cap denotes the capacity part of the state, also gives such a family but costs about 2^c. Theorem 3 gives cheap collisions and a bridge-amplified multicollision: one inner collision and one connector yield equal-length Joux-style 2^k-multicollisions for every k, instead of Joux's k collision searches; to our knowledge this is the first such construction for generic sponges with search cost independent of k. We give verified full-round examples on Keccak-f[200] and on Keccak-f[1600] with c=32. The second part of the paper offers novel protocols built on the asymmetry between minting and forging Keccak bridges. They include proof of work with hardness-adaptive capacity, dual-capacity commitments anchored by the real SHA3-256 digest, bridges as zero-knowledge-committed tokens, and a self-enforcing bounty market for reduced-round security. To our knowledge, these are the first unkeyed Keccak-based protocols that deliberately set the capacity so that the generic bridge cost is a feasible, tunable hardness parameter. We prove the three theorems, machine-check the stated algebraic results in Lean 4, and provide reproducible experiments and open-source proof-of-concept code. The applications are design proposals whose end-to-end security remains open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2671) | 2026-10-28
