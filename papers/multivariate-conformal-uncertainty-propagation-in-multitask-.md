---
title: "Multivariate conformal uncertainty propagation in multitask atomistic simulation: Successes and pitfalls"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.31384"
summary: "arXiv:2609.31384v1 Announce Type: new Abstract: Machine learning has become the standard tool for the design of interatomic potentials which balance efficiency and accuracy, but uncertainty quantifica"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31384v1 Announce Type: new Abstract: Machine learning has become the standard tool for the design of interatomic potentials which balance efficiency and accuracy, but uncertainty quantification remains an open problem. Multiscale simulations introduce an additional challenge: robust uncertainty quantification across scales. Even within one scale, computations are often multistage, producing a sequence of target quantities, each dependent on the previous, and each with some uncertainty. Conformal methods have emerged as a model agnostic framework for recalibrating surrogate predictions to produce sets which contain the truth at a user-specified rate. For multistage workflows, we require uncertainty calibration for multiple chemical properties and atomistic configurations, and we want to propagate uncertainty sets to downstream quantities of interest. Such propagation should capture the error cancellations which occur in many downstream targets in materials science; for instance, an approximate energy difference is often more accurate than individual energy predictions. We present the first exploration of multivariate conformal methods for chemical properties, including Bonferroni-corrected hyperrectangles, hyperellipsoidal sets based on the Mahalanobis distance, and custom loss functions within conformal risk control. Calibration is applied directly to predicted energies, atomic forces, and virial stresses, then propagated to elastic constants and vacancy formation energies employing a variety of commonly considered approximate protocols in materials modeling. We highlight the benefits of building correlation predictions into the conformal procedure, making it possible to build sets which capture near symmetries and error cancellation. We conclude with a discussion of the interplay of the employed approximate computational protocol and conformal guarantees.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.31384) | 2026-09-28
