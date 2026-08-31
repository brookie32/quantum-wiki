---
title: "A reaction volume bias Monte Carlo trial for sampling chemisorption in confinement"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.28516"
summary: "arXiv:2608.28516v1 Announce Type: new Abstract: Molecular modeling of chemisorption with Monte Carlo requires the development of new trial moves to efficiently sample complex fluids such as water in B"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.28516v1 Announce Type: new Abstract: Molecular modeling of chemisorption with Monte Carlo requires the development of new trial moves to efficiently sample complex fluids such as water in Bronsted acid zeolites. Here, we develop a reaction volume bias (RxVB) Monte Carlo trial for modeling chemisorption by combining identity-switch and aggregation-volume-bias (AVB) moves. This method aims to promote the sampling of reactions by choosing reactive pairs that are within an arbitrarily specified reaction volume. The RxVB move achieves up to a 90-fold increase in accepted reaction events over unbiased moves in a single-site slit-pore model, corresponding to a 70-fold gain in statistical efficiency after accounting for computational overhead. But when the same move is applied to water in a Bronsted acid zeolite without orientational bias, there is no measurable speedup for a single MFI unit cell. We demonstrate a simple expression that predicts the maximum efficiency increase in the simplest case where selecting reactants that are near each other is the major sampling bottleneck. Dense water systems may require additional configuration-bias or orientational bias to improve sampling of the hydrogen bond network in order to increase acceptance. This new RxVB trial was made available with examples in the open-source Free Energy and Advanced Sampling Simulation Toolkit (FEASST) simulation package.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.28516) | 2026-08-31
