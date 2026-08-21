---
title: "DPA4: Pushing the Accuracy-Cost Frontier of Interatomic Potentials with EMFA SO(2) Convolution"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2606.02419"
summary: "arXiv:2606.02419v4 Announce Type: replace Abstract: Machine-learning interatomic potentials now approach quantum-mechanical accuracy, but the most expressive equivariant architectures are costly to ev"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2606.02419v4 Announce Type: replace Abstract: Machine-learning interatomic potentials now approach quantum-mechanical accuracy, but the most expressive equivariant architectures are costly to evaluate, and the leading ones depend on auxiliary denoising or direct-force pretraining. We introduce DPA4, an SE(3)-equivariant architecture spanning six size classes from 0.48 to 25 million parameters and reaching the accuracy of the strongest published models at several-fold to an order-of-magnitude higher inference throughput. Its convolution couples edge and node features across all angular degrees in an edge-local frame, and its Wigner bilinear nonlinearity is universal in its full form and, on an exact quadrature grid, equivariant to machine precision. On Matbench Discovery, DPA4 leads every ranked metric, and every variant evaluated lies on the accuracy--throughput Pareto frontier of the compliant leaderboard. DPA4-Pro attains the lowest energy error on OMat24 and lower total-energy and force errors than the strongest conservative baseline on the OMol25 composition-validation split. All variants are trained through the conservative energy-gradient path alone, made practical by a threefold-faster compiled implementation. DPA4 thus brings leaderboard-class accuracy within the routine compute budgets of molecular-dynamics and materials-screening workflows, for both inorganic crystals and organic molecules.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2606.02419) | 2026-08-21
