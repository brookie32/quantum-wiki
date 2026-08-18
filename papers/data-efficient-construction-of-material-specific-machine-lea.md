---
title: "Data-Efficient Construction of Material-Specific Machine-Learning Interatomic Potentials from Ab Initio Molecular Dynamics Trajectories"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.14899"
summary: "arXiv:2608.14899v1 Announce Type: cross Abstract: Pretrained machine-learning interatomic potentials, so-called universal or foundation models offer an appealing starting point for atomistic simulatio"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.14899v1 Announce Type: cross Abstract: Pretrained machine-learning interatomic potentials, so-called universal or foundation models offer an appealing starting point for atomistic simulations, but their accuracy for material-specific observables often remains limited without additional reference data (fine-tuning). Here, we systematically quantify how much first-principles data are required to convert universal models into ab initio-accurate material-specific potentials, and ask whether fine-tuning is necessarily preferable to training from scratch. We compare five universal MLIP frameworks, MACE-MP-0, SevenNet-0, GRACE-1L-OAM, MatterSim-v1-5M and ORB-v2, across seven chemically diverse systems incorporating rare and reactive events. Fine-tuning on only 10 AIMD-derived configurations is insufficient for the investigated systems; 200 configurations succeed in favorable cases, but the outcome remains strongly system-dependent. By contrast, 2000 AIMD configurations constitute a robust default, yielding low force and energy errors and reproducing the target material-specific observables. Moderately dense sub-sampling of the AIMD trajectory reduces the required trajectory length tenfold with little loss in model quality. Training from scratch on the same datasets is competitive with, and often slightly more accurate than, naive fine-tuning for MACE and SevenNet, whereas GRACE requires more data. The energy profile for a sulfur-vacancy jump in MoS_2 reveals that low trajectory-level errors do not guarantee a correct reaction profile, highlighting the need for observable-level validation. Finally, we show that averaging independently trained models improves predictions in scarce-data regimes at no additional first-principles cost. Together, these results provide practical guidelines for converting limited AIMD reference data into reliable material-specific MLIPs for nanosecond-timescale simulations at near-DFT accuracy.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.14899) | 2026-08-18
