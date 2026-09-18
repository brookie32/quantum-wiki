---
title: "Machine-Learned Dynamical Representations for Accelerated RiteWeight Convergence"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.19388"
summary: "arXiv:2609.19388v1 Announce Type: new Abstract: The increasing use of generative models has made ensembles of short molecular dynamics trajectories increasingly common, creating a growing need for met"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19388v1 Announce Type: new Abstract: The increasing use of generative models has made ensembles of short molecular dynamics trajectories increasingly common, creating a growing need for methods that can recover physically meaningful steady-state populations and kinetics from improperly weighted conformational ensembles. Randomized Iterative Trajectory Reweighting (RiteWeight) addresses this problem through repeated random clustering and iterative reweighting, without requiring the fixed Markovian discretization used in conventional Markov state models (MSM). However, the choice of reduced feature space in which RiteWeight performs random clustering has not been systematically investigated. Here, we compare two machine-learned representations, DeepTICA and SPIB-VAE, with linear TICA for recovering steady-state observables from flawed distributions. DeepTICA learns nonlinear coordinates by targeting slow transfer-operator eigenmodes, whereas SPIB-VAE compresses configurations into a low-dimensional latent space while retaining information predictive of future metastable states. DeepTICA provided a comparatively robust RiteWeight representation under limited hyperparameter exploration, whereas SPIB-VAE benefited more strongly from broader optimization. Moreover, a kinetic score computed from a coarse MSM at a resolution comparable to that used for RiteWeight random clustering provided a useful criterion for efficiently selecting reduced representations and their hyperparameters for RiteWeight.



## Related
- [[selftica-contrastive-learning-of-dynamical-representations-f|SelfTICA: contrastive learning of dynamical representations for rare-event sampling and characterization]]
- [[machine-learning-kinetics-from-molecular-dynamics-data|Machine learning kinetics from molecular dynamics data]]
- [[derivation-of-the-sample-size-scaling-of-two-nn-intrinsic-di|Derivation of the Sample-Size Scaling of TWO-NN Intrinsic-Dimension Estimates from Molecular Dynamics Trajectories]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.19388) | 2026-09-18
