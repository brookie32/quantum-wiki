---
title: "Quantum-Informed Regularized Poisson Learning for Graph-Based Semi-Supervised Classification"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27609"
summary: "arXiv:2611.27609v1 Announce Type: cross Abstract: We introduce IPQSSL, a quantum-informed regularized Poisson framework for graph-based semi-supervised classification under scarce labels. Local graph "
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27609v1 Announce Type: cross Abstract: We introduce IPQSSL, a quantum-informed regularized Poisson framework for graph-based semi-supervised classification under scarce labels. Local graph feature contexts are QR factorized, lifted to unitary encodings, and processed by a shared variational circuit whose measurements yield node wise diagonal weights that stabilize a symmetrized Poisson system. We establish positive definiteness of the symmetrized, regularized operator under explicit spectral conditions and derive a Hermitian, block encoding compatible formulation that separates the classical NISQ oriented implementation from a future fault-tolerant pathway. Across seven benchmarks spanning tabular data and a citation network, the effect of regularization is dataset- and budget-dependent: IPQSSL improves over the Poisson baselines on Iris and Wine at all but the single-label budget, reaching 0.946 accuracy on Iris at ten labels per class and at every budget on German Credit, where, however, all methods remain below the majority class rate. Original Poisson remains preferable on Breast Cancer, Heart Disease, Optdigits, and Cora, with the deficit narrowing as the label budget grows on the two largest graphs. Ablations attribute the gains to diagonal stabilization rather than variational training. The result is a resource transparent bridge between Poisson graph learning and quantum linear algebra, with an explicit empirical delineation of when diagonal regularization helps.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27609) | 2026-11-23
