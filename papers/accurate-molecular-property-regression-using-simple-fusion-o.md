---
title: "Accurate Molecular Property Regression Using Simple Fusion of Complementary Classical and Graph Predictors"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.07678"
summary: "arXiv:2610.07678v1 Announce Type: new Abstract: Accurate prediction of continuous molecular properties supports chemical discovery and design. Many recent approaches combine multiple molecular represe"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07678v1 Announce Type: new Abstract: Accurate prediction of continuous molecular properties supports chemical discovery and design. Many recent approaches combine multiple molecular representations within increasingly complex neural architectures, aiming to achieve higher accuracy. However, classical machine-learning models remain competitive when trained on chemically meaningful molecular representations. We therefore constructed a chemistry-guided classical branch from Morgan fingerprints, RDKit molecular descriptors, and conformer-derived geometric features selected to provide complementary views of molecular structure. We combined four tree learners trained on these representations with a CoMPT graph predictor and integrated their out-of-fold predictions using Ridge regression. Across ESOL, FreeSolv, and Lipophilicity datasets, the fused model achieved lower mean root-mean-square error (RMSE) than Chemprop and competitive graph and multimodal methods, including CoMPT, MoleSG, KFLM2, and MCMPP. After retraining on the separately curated AqSolDB dataset, the same approach, without redesign or retuning, reduced mean absolute error (MAE) relative to the classical ensemble and achieved lower mean MAE than Chemprop. These results show that accurate and transferable molecular property regression does not necessarily require a complex joint multimodal architecture: classical learning remains competitive when chemical insight guides the choice of molecular representations, and a graph model can add complementary information through simple prediction-level fusion.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.07678) | 2026-10-07
