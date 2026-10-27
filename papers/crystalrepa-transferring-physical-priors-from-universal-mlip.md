---
title: "CrystalREPA: Transferring Physical Priors from Universal MLIPs to Crystal Generative Models"
date: "2026-10-27"
updated: "2026-10-27"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2605.08960"
summary: "arXiv:2605.08960v2 Announce Type: replace-cross Abstract: Crystal generative models mainly learn what stable crystals look like, with little explicit supervision for what makes them stable. We reveal "
last_verified: "2026-10-27"
review_by: "2027-01-25"
stale: false
---

arXiv:2605.08960v2 Announce Type: replace-cross Abstract: Crystal generative models mainly learn what stable crystals look like, with little explicit supervision for what makes them stable. We reveal a substantial representation gap between state-of-the-art crystal generative models and pretrained universal machine learning interatomic potentials (MLIPs) via energy probing, and show this gap can be closed by a simple training-time alignment. We propose Crystal REPresentation Alignment (CrystalREPA), a plug-and-play framework that aligns the atom-wise hidden states of generative encoders with frozen MLIP representations through an element-aware contrastive objective, transferring stability-aware atomistic priors with marginal training overhead and no additional inference cost. Across three generative frameworks, ten MLIP teachers, and two benchmark datasets, CrystalREPA consistently improves the thermodynamic stability, structural validity, and structural fidelity of generated crystals. Equally important, we find that an MLIP's transfer effectiveness is poorly predicted by its accuracy on standard leaderboards (e.g., Matbench Discovery) but strongly predicted by the distinguishability of its atom-wise representation space, yielding a practical, accuracy-independent criterion for selecting MLIP teachers for generative transfer. Code is available at https://github.com/Chengqian-Zhang/CrystalREPA.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2605.08960) | 2026-10-27
