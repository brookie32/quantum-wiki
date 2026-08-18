---
title: "A Generative Deep Learning Workflow for Inverse Molecular Design of Fuels"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2504.12075"
summary: "arXiv:2504.12075v4 Announce Type: replace-cross Abstract: In the present work, a generative deep learning framework combining a Co-optimized Variational Autoencoder (Co-VAE) with quantitative structur"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2504.12075v4 Announce Type: replace-cross Abstract: In the present work, a generative deep learning framework combining a Co-optimized Variational Autoencoder (Co-VAE) with quantitative structure-property relationship (QSPR) techniques is developed to enable inverse molecular design of fuels. The Co-VAE approach integrates an auxiliary fuel property prediction regression head with the VAE latent space, enhancing molecular reconstruction and accurate property estimation (Research Octane Number (RON) chosen as the fuel property of interest for demonstration studies). A subset of the GDB-13 database, combined with a curated RON database, is used for the Co-VAE training. Hyperparameter tuning is further utilized to optimize the balance among reconstruction fidelity, chemical validity, and RON prediction. Subsequently, an independent regression model is trained to further improve RON prediction accuracy, and a differential evolution algorithm is employed to efficiently navigate the Co-VAE latent space and identify promising fuel molecule candidates with RON greater than a chosen threshold. The overall generative deep learning framework captures complex structure-property relationships within a latent representation, and can be readily extended to different or multiple fuel properties, allowing exploration of large chemical spaces relevant to fuel design. Furthermore, the framework can be further augmented by incorporating additional synthesizability criteria to improve applicability and reliability for de novo design of novel high-performance fuels.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2504.12075) | 2026-08-18
