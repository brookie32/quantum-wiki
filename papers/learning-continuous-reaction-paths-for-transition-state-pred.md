---
title: "Learning continuous reaction paths for transition-state prediction"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.25523"
summary: "arXiv:2609.25523v1 Announce Type: cross Abstract: Transition states are defined by reaction pathways, yet most machine-learning methods predict them as isolated geometries. We introduce MARC-TS, a two"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25523v1 Announce Type: cross Abstract: Transition states are defined by reaction pathways, yet most machine-learning methods predict them as isolated geometries. We introduce MARC-TS, a two-stage framework that learns a continuous, endpoint-conditioned path, queries it at any resolution and uses local path context to refine a transition-state candidate. We construct T1x-IRC-8K, a dataset of 8,209 reactions and 1,088,725 path-resolved geometries. On held-out reactions, the path model reduced complete-path error by 48.4% relative to endpoint interpolation, and the localizer achieved a mean aligned structural error of 0.127 {AA}. Quantum-chemical optimization and vibrational analysis yielded 405 frequency-confirmed first-order saddle-point candidates from 410 predictions. In a 100-reaction nudged elastic band comparison, learned-path initialization reached a joint geometry-and-force target for 66% of reactions, compared with 12% for geometric interpolation after 100 optimizer steps. By treating the path as a reusable representation rather than an auxiliary output, MARC-TS connects transition-state prediction, mechanistic interpretation and quantum-chemical refinement.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.25523) | 2026-09-23
