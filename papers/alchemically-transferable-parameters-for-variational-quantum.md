---
title: "Alchemically Transferable Parameters for Variational Quantum Eigensolvers"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.11445"
summary: "arXiv:2611.11445v1 Announce Type: cross Abstract: Machine-learned circuit parameters could remove one of the main bottlenecks of variational quantum eigensolvers: the classical optimization loop, with"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.11445v1 Announce Type: cross Abstract: Machine-learned circuit parameters could remove one of the main bottlenecks of variational quantum eigensolvers: the classical optimization loop, with its typical barren plateaus, local minima, and costly energy and gradient evaluations, is replaced by a direct prediction. Prior work showed that machine-learning models paired with a structured circuit design can transfer across system size and structure within hydrogenic systems. The next step: Extending them to organic molecules would seem to require re-training on use-case-specific training sets. In this work, we show that this is not necessary by establishing an alchemical approach. A geometric projection places surrogate hydrogen atoms along the bond directions of the target molecule and so maps its local bonding environment onto small hydrogenic fragments. Existing hydrogenic solvers can then be reused as they are. The only new quantity is a single projection radius per bond type, which is fitted once on a small reference molecule and reused unchanged thereafter. We demonstrate the approach on the separable-pair circuit designs that have been used in prior work and extend the approach to multi-circuit approaches that span effective bases for quantum subspaces.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.11445) | 2026-11-11
