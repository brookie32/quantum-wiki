---
title: "PhysECD: A Physics-Constrained E(3)-Equivariant Framework for Electronic Circular Dichroism Spectrum Prediction"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.21892"
summary: "arXiv:2608.21892v1 Announce Type: new Abstract: The electronic circular dichroism (ECD) spectrum is a primary experimental probe for assigning the absolute configuration of chiral molecules, yet inter"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.21892v1 Announce Type: new Abstract: The electronic circular dichroism (ECD) spectrum is a primary experimental probe for assigning the absolute configuration of chiral molecules, yet interpreting a measured spectrum requires time-dependent density functional theory (TDDFT) calculations that can cost hours per molecule and must be repeated for every candidate stereoisomer and conformation. We present PhysECD, a physics-constrained, parity-aware E(3)-equivariant framework that bypasses computationally expensive TDDFT and predicts ECD spectra directly from the 3D structure of an individual conformer. Instead of regressing the spectrum as an opaque sequence, PhysECD predicts the physical quantities that generate it: per-state excitation energies and electric and magnetic transition dipoles. These quantities determine the rotatory strength R -- the dot product of the two dipoles, a pseudoscalar that reverses sign under mirror reflection -- and yield the final spectrum through a differentiable Gaussian-broadening formula derived from the underlying physics. The parity structure of the equivariant features guarantees the correct chiroptical symmetry: reflecting a molecule exactly negates the predicted spectrum. On the CMCDS dataset, PhysECD attains a per-molecule spectral Pearson correlation of 0.642 (mean) / 0.822 (median), substantially exceeding prior learned predictors while remaining physically interpretable. Experiments across multiple backbones further show that the framework is backbone-agnostic, paving the way for real-time assignment of absolute configuration.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.21892) | 2026-08-25
