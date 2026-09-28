---
title: "Scaling Density Functional Theory with Gaussian Splatting"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.31483"
summary: "arXiv:2609.31483v1 Announce Type: new Abstract: Density functional theory (DFT) strikes a practical balance between accuracy and computational cost in many problems of computational chemistry and mate"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31483v1 Announce Type: new Abstract: Density functional theory (DFT) strikes a practical balance between accuracy and computational cost in many problems of computational chemistry and materials science. However, many DFT calculations are limited by fixed atom-centered basis sets, which dictate how accuracy and cost scale with system size. We propose Gaussian Splatting for Density Functional Theory (GS-DFT), which represents molecular orbitals as a cloud of Gaussians whose positions, shapes, and mixing coefficients are optimized jointly by gradient descent to minimize the energy without training data. Conceptually, GS-DFT is 3D Gaussian splatting with the renderer replaced by quantum mechanics. We introduce two key solver components: adaptive density fitting with screening for efficient evaluation of two-electron integrals, and a regularized differentiable orthogonalization of the molecular orbitals. Empirically, the optimized basis reaches the accuracy of the largest conventional basis sets with a fraction of the parameters, converging systematically in energy, density, and nuclear forces. At equal parameter count, it captures the stretched-bond and anion physics that fixed bases only recover with specialized basis augmentation. The resulting solver exhibits quadratic peak memory scaling in the cloud size, allowing us to simulate systems of up to 2,742 atoms (10,406 electrons) without any modifications at triple-zeta scale using a single four-GPU node.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.31483) | 2026-09-28
