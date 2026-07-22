---
title: "Predicting Activities in Aqueous Electrolyte Solutions with Hybrid Machine Learning"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.19114"
summary: "arXiv:2607.19114v1 Announce Type: cross Abstract: Activities in aqueous electrolyte solutions, usually described by ionic activity and osmotic coefficients, are important properties for modeling many "
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2607.19114v1 Announce Type: cross Abstract: Activities in aqueous electrolyte solutions, usually described by ionic activity and osmotic coefficients, are important properties for modeling many processes in industry and nature. Established activity models, such as those of Pitzer or Bromley, require fitting to experimental data for each electrolyte of interest and thus cannot predict properties for unstudied systems. While some predictive approaches exist, they are typically limited in scope and rely on additional ion-specific descriptors. In this work, we introduce a new hybrid model that combines the physics-based Bromley model with a matrix completion method (MCM) from machine learning. The MCM is employed to predict the electrolyte-specific parameters of the Bromley model, exploiting the fact that these parameters can be arranged in a matrix with cations and anions as rows and columns, respectively. Due to the lack of experimental data for many electrolytes, the initial parameter matrix is sparsely populated, making the prediction of the Bromley parameters for unstudied electrolytes a matrix completion problem. The hybrid model, Bromley-MCM, was trained end-to-end on experimental data for mean ionic activity coefficients and osmotic coefficients of aqueous solutions of 478 electrolytes at 298 K from the Dortmund Data Bank. As output, we obtain a completed matrix of Bromley parameters for 83 cations and 112 anions, enabling consistent prediction of concentration-dependent activities in aqueous solutions of 9,296 electrolytes at 298~K. This substantially extends the applicability of the Bromley model while maintaining high predictive accuracy, as demonstrated through evaluations on electrolytes excluded from model training.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.19114) | 2026-07-22
