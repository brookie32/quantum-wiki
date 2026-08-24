---
title: "HIP: Hessian Interatomic Potentials without derivatives"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2509.21624"
summary: "arXiv:2509.21624v4 Announce Type: replace-cross Abstract: Molecular Hessians, the second derivatives of the potential energy, are fundamental to many workflows in computational chemistry. Usually, acc"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2509.21624v4 Announce Type: replace-cross Abstract: Molecular Hessians, the second derivatives of the potential energy, are fundamental to many workflows in computational chemistry. Usually, accurate Hessians are computationally expensive to calculate and scale poorly with system size, whether computed using quantum chemistry methods or machine-learning interatomic potentials (MLIPs). In this work, we introduce Hessian interatomic potentials (HIPs), a deep learning model that directly predicts Hessians without relying on automatic differentiation or finite differences. To do so, we construct SE(3)-equivariant, symmetric Hessians from irreducible representation (irrep) features up to degree l=2, computed by a graph neural network. HIP Hessians are one to two orders of magnitude faster, more accurate, more memory efficient, easier to train, and exhibit more favourable scaling with system size. We validate our predictions across a wide range of downstream tasks, demonstrating consistently superior performance in transition state search, geometry optimization, zero-point energy corrections, and vibrational analysis. We open-source the HIP code and model weights.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2509.21624) | 2026-08-24
