---
title: "The Mechanics of Delta Learning: Target Design for Generalizable Scientific Machine Learning"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.28782"
summary: "arXiv:2609.28782v1 Announce Type: cross Abstract: In scientific machine learning, Delta-learning trains models on residual errors relative to physical baselines, assuming that more accurate baselines "
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.28782v1 Announce Type: cross Abstract: In scientific machine learning, Delta-learning trains models on residual errors relative to physical baselines, assuming that more accurate baselines with smaller residual scales inherently improve downstream performance. Here, we demonstrate that residual scale alone is an insufficient heuristic for learnability. Evaluating molecular graph neural networks on total energy targets, we show that complex local descriptor baselines can yield small residual targets that are disproportionately rough within architecture-informed proxy spaces and harder to learn relative to their scale. Conversely, semi-empirical baseline reduces both scale and normalized roughness, improving in-domain and out-of-domain prediction. We introduce scale-normalized graph Dirichlet roughness (D_{ext{IQR}}) as a pre-training diagnostic for residual learnability and establish baseline complementarity as a core target-design principle, elevating target space formulation alongside model architecture as a key axis for scientific machine learning.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.28782) | 2026-09-25
