---
title: "MAST: Motif-Augmented Diffusion with Search Tree for Spectroscopic Molecular Structure Elucidation"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.12067"
summary: "arXiv:2610.12067v1 Announce Type: new Abstract: Elucidating molecular structures from spectra is a foundational problem in chemical and materials characterization, yet remains challenging due to spect"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12067v1 Announce Type: new Abstract: Elucidating molecular structures from spectra is a foundational problem in chemical and materials characterization, yet remains challenging due to spectral ambiguity and the vast molecular space. Although recent diffusion-based generators show strong promise for spectra-conditioned elucidation, existing methods struggle to learn robust spectra-structure relationships from limited paired data when relying solely on global spectral representation. Moreover, the repeated full sampling inference strategy incurs substantial computation overhead. To address these limitations, we propose extbf{MAST}, a extbf{M}otif-extbf{A}ugmented diffusion framework with extbf{S}earch extbf{T}ree, for joint 2D-3D spectroscopic molecular structure elucidation. MAST introduces explicit, interpretable motif priors as intermediate evidences throughout denoising, reducing conditional ambiguity and facilitating spectra-conditioned optimization. We further cast diffusion sampling as reward-guided tree search to prioritize high-reward denoising trajectories, yielding a compact set of spectra-consistent candidates under limited budgets. On the QM9S multi-spectra benchmark, MAST achieves extbf{94.89%} exact recovery and improves 3D fidelity, while preserving high chemical validity and stability. Code is available at https://github.com/Jia040223/MAST.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.12067) | 2026-10-09
