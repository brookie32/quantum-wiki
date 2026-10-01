---
title: "ProtScape: A molecular structure and energy-aware representation for protein conformation generation"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2410.20317"
summary: "arXiv:2410.20317v2 Announce Type: replace-cross Abstract: Molecular dynamics (MD) simulations are a principled but computationally expensive approach for studying protein conformational variability, m"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2410.20317v2 Announce Type: replace-cross Abstract: Molecular dynamics (MD) simulations are a principled but computationally expensive approach for studying protein conformational variability, making it challenging to generate large ensembles of structures or characterize transitions between metastable conformations. AI methods for upsampling MD simulations have been developed recently but struggle due to difficulties of sampling complex, high-dimensional molecular distributions. One avenue these methods overlook is to learn a latent space where such sampling becomes easier. To address this, we introduce ProtScape, a generative geometric deep learning framework that learns structure and energy-aware representations of protein conformational landscapes from MD simulations. ProtScape represents protein conformations using an equivariant graph neural network and a multiscale deep wavelet transform that captures local geometric interactions and nonlocal collective motions. This latent representation is dual-organized: 1) by structure captured by wavelet transform layers, via reconstruction error; 2) by energy using a Laplacian energy smoothness penalty. This structured latent space enables meaningful generation and exploration of protein conformations. ProtScape supports multiple generative modes: 1) ensemble generation, which upsamples ensembles given limited MD trajectories flow matching from noise to the organized manifold of conformations, 2) minimum-energy path generation between two high-energy conformations, guided by energy using a nudged elastic band, and 3) energy-descent, which generates trajectories toward lower energies from a high-energy conformation using gradient descent, thereby hypothesizing folding or other stabilizing trajectories. Organizing a latent space by structure and energy lets one representation support ensemble sampling, minimum-energy path finding and energy-guided descent on the same conformational landscape.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2410.20317) | 2026-10-01
