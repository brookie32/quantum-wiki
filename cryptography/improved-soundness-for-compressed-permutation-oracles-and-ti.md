---
title: "Improved Soundness for Compressed Permutation Oracles and Tight Quantum Preimage and Collision Bounds for the Sponge"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2135"
summary: "We give a sharper bound on the error introduced by replacing a random permutation oracle with Carolan’s compressed permutation oracle. Building on Rosmanis’s representation-theoretic approach, we repr"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We give a sharper bound on the error introduced by replacing a random permutation oracle with Carolan’s compressed permutation oracle. Building on Rosmanis’s representation-theoretic approach, we represent exact permutation states in the compressed oracle’s database space, allowing a direct comparison of the two query operations. For a uniform permutation on N points, this comparison bounds the soundness error by 4q/√N after q ≤ N/4 queries. As the main application, we obtain tight query complexity for constant success probability in sponge preimage and collision search by substituting this bound into Carolan’s search reductions. The same analysis improves bounds for the one-more problem and cycle finding, and gives tight query complexity for constant success probability in keyless Davies–Meyer collision search

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2135) | 2026-09-21
