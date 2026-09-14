---
title: "Refining Leakage Diagram Analyses for Random Probing Security"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2016"
summary: "Masking is a widely used countermeasure against side-channel attacks, where sensitive variables are split into randomized shares in order to prevent information leakage from intermediate computations."
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Masking is a widely used countermeasure against side-channel attacks, where sensitive variables are split into randomized shares in order to prevent information leakage from intermediate computations. Its security is commonly analyzed in the random probing model, in which each internal variable leaks independently with some probability p. Constructing large masked circuits that achieve random probing security (RPS) is challenging, and a common approach is to rely on composability frameworks ensuring that suitable local gadget-level properties imply circuit-level guarantees. Recent works have introduced compositional frameworks based on leakage diagrams to derive security guarantees in the random probing model. While elegant and scalable, these approaches rely on conservative analyses and security proofs tailored to specific gadget constructions. In this work, we revisit and refine a leakage-diagram approach published in TCHES 2023. We formalize and generalize the proof to show that the probability of an orbit in the leakage diagram upper bounds the adversary's RPS advantage. Our analysis identifies the local gadget-level conditions needed for this composition result, refines the analysis of edge inclusion probabilities in leakage diagrams for the underlying multiplication gadgets, leading to tighter final security bounds, and improves the combinatorial analysis of orbits through a detailed study of small cases and new structural properties for larger ones. We evaluate the resulting constructions on AES. Our results significantly improve the concrete security guarantees compared to previous leakage diagram analyses, while also improving the randomness complexity compared to existing composable approaches.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2016) | 2026-09-14
