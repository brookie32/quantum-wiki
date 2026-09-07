---
title: "Hessian-based molecular conformation augmentation for a scalable and efficient strategy of machine learning interatomic potentials"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.05233"
summary: "arXiv:2609.05233v1 Announce Type: cross Abstract: While machine-learning interatomic potentials (MLIPs) have successfully learned potential energy surfaces (PES) and atomic forces, many practical appl"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.05233v1 Announce Type: cross Abstract: While machine-learning interatomic potentials (MLIPs) have successfully learned potential energy surfaces (PES) and atomic forces, many practical applications, such as vibrational analysis and transition state search, rely heavily on the PES Hessian. Yet, standard MLIPs tend to be trained on energy and forces alone, leaving Hessian information largely unexploited. Meanwhile, existing methods that explicitly incorporate the Hessian into training objectives require architectural modifications and introduce significant computational and memory overheads due to higher-order backpropagation. To address these limitations, we propose two Hessian-derived data augmentation schemes: isotropic Gaussian displacement (extbf{UniAug}) and normal mode-weighted displacement (extbf{ModeAug}). Both methods utilize simple Taylor expansions, achieving effective augmentation without altering training objectives or extending the autograd graph. This allows seamless, plug-and-play integration with existing architectures and training pipelines. Comprehensive evaluations across non-equilibrium and equilibrium datasets demonstrate that our approach enhances model accuracy while providing practical, task-specific guidelines.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.05233) | 2026-09-07
