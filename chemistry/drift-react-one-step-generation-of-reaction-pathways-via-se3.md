---
title: "Drift-React: One-step Generation of Reaction Pathways via SE(3) Drifting Fields"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2605.22990"
summary: "arXiv:2605.22990v2 Announce Type: replace Abstract: Mapping reaction pathways and transition states (TS) is fundamental to chemistry but computationally expensive at scale. The minimum energy pathway "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2605.22990v2 Announce Type: replace Abstract: Mapping reaction pathways and transition states (TS) is fundamental to chemistry but computationally expensive at scale. The minimum energy pathway (MEP) dictates reaction rates and mechanisms, yet recovering it via electronic-structure methods requires thousands of costly force evaluations. Recent generative models accelerate TS identification but rely on iterative inference and only predict isolated saddle-point snapshots, missing the continuous reaction trajectory. We introduce Drift-React, an SE(3)-equivariant generative framework that predicts complete reaction pathways in a single forward pass from only reactant and product geometries. By shifting distribution evolution to training via a Sinkhorn-weighted drifting field, Drift-React eliminates both the iterative force evaluations of NEB-style methods and the sequential ODE/SDE integration of diffusion and flow matching models. Evaluated on the Transition1x and Halo8 datasets, our one-step model generates physically consistent MEPs that accurately capture energetic bottlenecks and enable arbitrary-resolution sampling along the reaction coordinate. For isolated TS prediction, Drift-React matches the sub-{AA}ngstrom accuracy of state-of-the-art iterative models while delivering orders-of-magnitude acceleration, clearing a major computational bottleneck for large-scale reaction network exploration.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2605.22990) | 2026-11-05
