---
title: "Mind Small Integers in MDS Matrix: Collision Attacks on Round-Reduced Reinforced Concrete"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2031"
summary: "The rapid advancement of Zero-Knowledge Proofs (ZKP) has motivated the design of ZK-friendly hash functions. A relatively new design strategy for ZK-friendly hash functions is using the composition of"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

The rapid advancement of Zero-Knowledge Proofs (ZKP) has motivated the design of ZK-friendly hash functions. A relatively new design strategy for ZK-friendly hash functions is using the composition of small look-up tables (LUTs) to build a nonlinear transform (called Bars layer) over a large prime field F_p. This not only improves the plain performance but also enhances its security against algebraic attacks since the Bars layer is equivalent to a complex and high-degree polynomial over F_p. This design strategy was first proposed at CCS 2022 for the ZK-friendly hash function Reinforced Concrete. However, there has been no third-party collion attacks of Reinforced Concrete since then, and all existing attacks on such LUT-based ZK-friendly ciphers like Tip5, Monolith and Skyscraper mainly exploit the differential or linear properties of Bars. In this paper, we demonstrate that the Bars layer surrounded by MDS matrices (called Concrete layers) with small integers, i.e., Concreteirc Barsirc Concrete, might lead to weaker differential properties of the round function. This key observation leads to a novel collision attack on 4.5 out of 7 rounds of Reinforced Concrete, successfully bypassing the Bars layer as well as the subsequent Concrete layer and power-map-based nonlinear layer (called Bricks layer). The attack is verified by providing a practical collision for 3.5-round Reinforced Concrete where the last 4 layers are Bricks irc Concrete irc Barsirc Concrete. Furthermore, we provide constructive countermeasures by designing an algorithm to generate an improved Concrete layer that thwarts this specific attack while preserving the efficiency of the original design. Finally, we also applied our framework to Tip5 but found that its MDS matrix can effectively prevent this attack. This is the first time to exploit the weak combination of Bars layer and Concrete layer to mount efficient attacks on LUT-based ZK-friendly hash functions. We believe that it sheds new insight into the security of these hash functions.



## Related
- [[a-better-bivariate-resultant-attack-on-round-reduced-poseido|A Better Bivariate Resultant Attack on Round-Reduced Poseidon]]
- [[from-round-skipping-to-s-box-skipping-attacking-poseidons-pa|From Round Skipping to S-Box Skipping: Attacking Poseidon's Partial Layer via Subspace Restriction]]
- [[arion-arithmetization-oriented-hashing-for-zero-knowledge-pr|Arion: Arithmetization-Oriented Hashing for Zero-Knowledge Proof Systems]]
- [[beyond-linear-subspace-trails-nonlinear-subspaces-for-grobne|Beyond Linear Subspace Trails: Nonlinear Subspaces for Grobner Basis Attacks on Poseidon/Poseidon2 and Neptune]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2031) | 2026-09-14
