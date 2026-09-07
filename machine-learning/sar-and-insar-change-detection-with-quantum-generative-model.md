---
title: "SAR and InSAR Change Detection with Quantum Generative Models"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05313"
summary: "arXiv:2609.05313v1 Announce Type: new Abstract: Change detection in synthetic aperture radar (SAR) and interferometric synthetic aperture radar (InSAR) underpins disaster response, infrastructure moni"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.05313v1 Announce Type: new Abstract: Change detection in synthetic aperture radar (SAR) and interferometric synthetic aperture radar (InSAR) underpins disaster response, infrastructure monitoring and land-use enforcement. Detection is limited by the background estimator, which conventionally forms a conditional expectation directly from observed pixel statistics and degrades where those statistics are sparse, including the regime produced by the heavy-tailed marginals of sub-meter-resolution radars. In this work, we integrate state-of-the-art satellite imagery with quantum machine learning on IonQ trapped-ion-based quantum processors. By replacing the empirical conditional with a quantum circuit Born machine (QCBM)-sampled generative model in Copula space, we substantially improve change detection on sparse real-world images. On Capella Space satellite image acquisitions, the generative estimator matches conventional methods when the observed statistics are adequate, and substantially outperforms them when they are not. Executing the trained model on IonQ trapped-ion based hardware reproduces the results of the ideal and noisy simulations and demonstrates up to par, or even better, performance with the classical state-of-the-art methods. For a SAR dataset of an airport, QPU circuit evaluations for both training and inference achieved a maximized filtered F1 score of 0.32, compared with 0.16 and 0.24 for the two classical baselines. For an InSAR dataset of a volcanic lava flow, all three methods reached a maximum filtered F1 of approximately 0.66. These experiments demonstrate the feasibility of executing a QCBM-based background estimator on trapped-ion hardware. We further demonstrate that the QCBM method successfully extends to interferometric coherence data, achieving performance comparable to classical approaches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05313) | 2026-09-07
