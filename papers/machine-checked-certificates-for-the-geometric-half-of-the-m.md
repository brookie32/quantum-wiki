---
title: "Machine-Checked Certificates for the Geometric Half of the Minimum Kochen-Specker Bound"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26413"
summary: "arXiv:2607.26413v1 Announce Type: cross Abstract: The best known lower bound for the minimum Kochen-Specker vector system in R^3 -- 24 vectors -- rests on a computational proof whose combinatorial hal"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26413v1 Announce Type: cross Abstract: The best known lower bound for the minimum Kochen-Specker vector system in R^3 -- 24 vectors -- rests on a computational proof whose combinatorial half emits DRAT proofs but whose geometric half does not: the non-embeddability of thousands of candidate graphs is established by Z3's nonlinear real arithmetic, which produces no checkable proof objects. We close this gap for the proof's blocking database. We introduce exact rational case-tree certificates of real non-embeddability, whose splits are polynomial factorizations and rational sum-of-squares decompositions and whose leaves are discharged by injectivity, ideal-membership, or Positivstellensatz-shaped positivity arguments, and we certify all 291 source lines (180 distinct graphs) of the published pipeline's order-10 to order-13 blocking lists. Certificates are replayed by two independent checkers that share no code with the generator: a pure-Python replay over exact fractions, and a total checker implemented and proved sound in Lean 4. The soundness theorem -- acceptance implies that no injective-on-rays, orthogonality-respecting assignment of nonzero real vectors realizes the graph -- is kernel-checked with axiom closure {propext, Classical.choice, Quot.sound}, and a gcd-free rational arithmetic layer makes the entire verdict computation kernel-reducible, so each per-graph non-embeddability result is a closed kernel theorem proved by decide. The formalization surfaced findings about the published pipeline, including a load-bearing injectivity side condition in its embeddability notion, hidden WLOG case obligations invisible to Z3-based workflows, and an unreproducible candidate count that we resolve against the published artifacts. All certificates, checkers, and proofs are available and replayable from a single build.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26413) | 2026-07-30
