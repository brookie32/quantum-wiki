---
title: "Derivation of the Sample-Size Scaling of TWO-NN Intrinsic-Dimension Estimates from Molecular Dynamics Trajectories"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.04914"
summary: "arXiv:2609.04914v1 Announce Type: new Abstract: The intrinsic dimension of a dataset is the number of independent directions needed to describe the space occupied by its data. Estimators based on near"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.04914v1 Announce Type: new Abstract: The intrinsic dimension of a dataset is the number of independent directions needed to describe the space occupied by its data. Estimators based on nearest neighbors infer this number from how the probability to find a neighbor point grows around each sampled point. Because the distances r between neighbor points decrease as the sample grows, the estimated dimension can depend strongly on the number of available points. Here, we derive the large-sample behavior of the TWO-NN estimator for data drawn from a smooth d-dimensional space. The typical nearest-neighbor distance scales as N^{-1/d}, and smooth deviations from a locally uniform distribution produce successive corrections proportional to N^{-2/d}. We test this result using the trajectories coming from ten independent 100~mus simulations of alanine dipeptide. Configurations are represented by all pairwise distances among the ten heavy atoms. This representation has a known geometric dimension of 3n_{at}-6=24. Over the investigated range, the TWO-NN estimate shows no systematic dependence on the temporal spacing between configurations, but increases from approximately 7.5 to 15.6 as the sample size grows from 10^2 to 2imes10^5. Extrapolations that retain corrections through r^2, r^4, and r^6 give limiting dimensions of 25.23, 22.89, and 27.00, respectively. All three estimates lie close to the known dimension and collectively bracket it, supporting the proposed scaling. Their spread provides a direct estimate of the systematic uncertainty associated with the truncation. The derived scaling therefore explains the strong sample-size dependence of TWO-NN and provides a practical route from finite sample estimates to the underlying geometric dimension.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.04914) | 2026-09-07
