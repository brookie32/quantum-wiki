---
title: "Suiren-1.0 Technical Report: A Family of Molecular Foundation Models"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2603.21942"
summary: "arXiv:2603.21942v4 Announce Type: replace Abstract: We introduce Suiren-1.0, a family of molecular foundation models for the accurate modeling of diverse organic systems. Suiren-1.0 comprising three s"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2603.21942v4 Announce Type: replace Abstract: We introduce Suiren-1.0, a family of molecular foundation models for the accurate modeling of diverse organic systems. Suiren-1.0 comprising three specialized variants (Suiren-Base, Suiren-Dimer, and Suiren-ConfAvg) is integrated within an algorithmic framework that bridges the gap between 3D conformational geometry and 2D statistical ensemble spaces. We first pre-train Suiren-Base (1.8B parameters) on a 70M-sample Density Functional Theory dataset using spatial self-supervision and SE(3)-equivariant architectures, achieving robust performance in quantum property prediction. Suiren-Dimer extends this capability through continued pre-training on 13.5M intermolecular interaction samples. To enable efficient downstream application, we propose Conformation Compression Distillation (CCD), a diffusion-based framework that distills complex 3D structural representations into 2D conformation-averaged representations. This yields the lightweight Suiren-ConfAvg, which generates high-fidelity representations from SMILES or molecular graphs. Our extensive evaluations demonstrate that Suiren-1.0 establishes state-of-the-art results across a range of tasks. All models and benchmarks are open-sourced.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2603.21942) | 2026-04-29
