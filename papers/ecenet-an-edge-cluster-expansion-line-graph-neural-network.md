---
title: "ECENet: An Edge Cluster Expansion Line-Graph Neural Network"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.23134"
summary: "arXiv:2609.23134v1 Announce Type: new Abstract: Machine-learned interatomic potentials (MLIPs) have emerged as a promising alternative to classical force fields and first-principles theory for predict"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.23134v1 Announce Type: new Abstract: Machine-learned interatomic potentials (MLIPs) have emerged as a promising alternative to classical force fields and first-principles theory for predicting the properties of chemical and material systems. Many MLIPs are graph neural networks with O(3)-equivariant features, whose accuracy comes at substantial computational cost. Here we introduce the edge cluster expansion (ECE), an analogue of the atomic cluster expansion in which the environment is expanded around edges between atom pairs rather than single atoms, and build upon it to develop the line-graph neural network ECENet. ECENet uses O(2)-equivariant features that persist on the edges between atoms, giving it natural access to O(2) operations that are cheaper and less restrictive than their O(3) counterparts. ECENet performs at the state of the art on the MD22 benchmark and lies on the accuracy-cost Pareto frontier when trained on the SPICE-MACE-OFF dataset. Furthermore, with long-range electrostatics implemented via latent Ewald summation, ECENet accurately predicts molecular dipole moments and the infrared spectrum of liquid water. The frontier ECENet architecture establishes equivariant edge-centered representations as an efficient and physically expressive foundation for equivariant MLIPs.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.23134) | 2026-09-22
