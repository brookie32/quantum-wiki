---
title: "VEDA: Generation of 3D Molecules via Variance-Exploding Diffusion with Annealing"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2511.09568"
summary: "arXiv:2511.09568v3 Announce Type: replace Abstract: Diffusion models show promise for 3D molecular generation, but face a fundamental trade-off between sampling efficiency and conformational accuracy."
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2511.09568v3 Announce Type: replace Abstract: Diffusion models show promise for 3D molecular generation, but face a fundamental trade-off between sampling efficiency and conformational accuracy. While flow-based models are fast, they often produce geometrically inaccurate structures, as they have difficulty capturing the multimodal distributions of molecular conformations. In contrast, denoising diffusion models are more accurate but suffer from slow sampling, a limitation attributed to sub-optimal integration between diffusion dynamics and SE(3)-equivariant architectures. To address this, we propose VEDA, a unified SE(3)-equivariant framework that combines variance-exploding diffusion with annealing to efficiently generate conformationally accurate 3D molecular structures. Specifically, our key technical contributions include: (1) a VE schedule that enables noise injection functionally analogous to simulated annealing, improving 3D accuracy and reducing relaxation energy; (2) a novel preconditioning scheme that reconciles the coordinate-predicting nature of SE(3)-equivariant networks with a residual-based diffusion objective, and (3) a new arcsin-based scheduler that concentrates sampling in critical intervals of the logarithmic signal-to-noise ratio. On the QM9 and GEOM-DRUGS datasets, VEDA matches the sampling efficiency of flow-based models, achieving state-of-the-art valency stability and validity with only 100 sampling steps. More importantly, VEDA's generated structures are remarkably stable, as measured by their relaxation energy during GFN2-xTB optimization. The median energy change is only 1.72 kcal/mol, significantly lower than the 32.3 kcal/mol from its architectural baseline, SemlaFlow. Our framework demonstrates that principled integration of VE diffusion with SE(3)-equivariant architectures can achieve both high chemical accuracy and computational efficiency.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2511.09568) | 2026-10-15
