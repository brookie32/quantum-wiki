---
title: "Bayesian Sampling of Structural Ensembles: The Role of Ensemble-Counting Measures"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2606.18495"
summary: "arXiv:2606.18495v2 Announce Type: replace Abstract: Structural ensemble refinement is widely used to integrate molecular simulations with experimental measurements. While most applications focus on th"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2606.18495v2 Announce Type: replace Abstract: Structural ensemble refinement is widely used to integrate molecular simulations with experimental measurements. While most applications focus on the maximum-a-posteriori (MAP) ensemble, Bayesian sampling of the posterior distribution can provide uncertainty estimates and posterior averages for arbitrary observables. A notable step in this direction was introduced by the Bayesian Energy Landscape Tilting (BELT) framework, where sampling is performed on a family of maximum-entropy ensembles parametrized by Lagrange multipliers. Here, we show that Bayesian sampling in this setting requires an explicit choice of ensemble-counting measure. In particular, the flat measure in Lagrange-multiplier space used in the original BELT formulation leads to a posterior distribution that is formally non-normalizable for finite reference trajectories. We propose the Jeffreys measure as an invariant ensemble-counting prescription, restoring normalizability in the finite-sample situations considered here, and providing a consistent definition of posterior averages. Using both an analytically tractable Gaussian model and maximum-entropy refinement of RNA oligomer simulations, we compare different ensemble-counting measures and show that they can significantly affect Bayesian estimates. The resulting methodology has been implemented in the exttt{MDRefine} software package.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2606.18495) | 2026-10-12
