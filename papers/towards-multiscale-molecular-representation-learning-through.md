---
title: "Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.07998"
summary: "arXiv:2611.07998v1 Announce Type: cross Abstract: It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains "
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.07998v1 Announce Type: cross Abstract: It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains often playing dominant roles. Fragment-based representations have therefore emerged as an effective strategy for incorporating chemically meaningful inductive biases, as exemplified by molecular fingerprints and fragment-based attention mechanisms. However, many existing fragmentation-based machine learning methods rely on predefined chemical rules, which may yield suboptimal fragmentation for previously unseen or chemically unfamiliar structures and often overlook the importance of multiscale molecular representations. To address these limitations, we formulate molecular fragmentation as a radius-constrained optimization problem inspired by the k-center formulation, where the number of clusters is not fixed a priori but emerges from the specified radius, and propose a geometry-based fragmentation method that partitions arbitrary molecular or material structures using largely geometric information, without relying on predefined chemical fragmentation rules. The method provides flexible control over fragment size, enabling the construction of multiscale fragment representations for scale-adaptive modeling. Building on this framework, we develop a geometric fragment-based attention mechanism that integrates multiscale structural information and incorporate it into a multimodal machine learning model combining p-SMILES representations with three-dimensional (3D) conformational information. Experiments on a benchmark polymer dataset show that incorporating 3D conformational information improves prediction accuracy for several properties over models based exclusively on p-SMILES representations. Explainable artificial intelligence analyses further provide insights into the physical relevance of the learned representations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.07998) | 2026-11-06
