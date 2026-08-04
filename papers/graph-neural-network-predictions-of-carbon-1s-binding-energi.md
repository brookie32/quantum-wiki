---
title: "Graph Neural Network Predictions of Carbon 1s Binding Energies with Near-Experimental Accuracy"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.27070"
summary: "arXiv:2604.27070v2 Announce Type: replace Abstract: Graph neural networks are promising architectures for fast, accurate and transferable predictions of core-electron binding energies, which depend on"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2604.27070v2 Announce Type: replace Abstract: Graph neural networks are promising architectures for fast, accurate and transferable predictions of core-electron binding energies, which depend on the local bond environment. Here we present a graph neural network model for predicting carbon 1s core-electron binding energies in organic molecules. The model is trained with multiconfiguration pair-density functional theory on 8637 carbon atoms in 2116 molecules with 4-16 atoms and evaluated against 570 experimental values in 113 different molecules containing 3-45 atoms. Previous work benchmarked a mean absolute error of 0.27 eV to experiment for the training data level of theory [J. Phys. Chem. A 2025, 129, 36, 8419-8431] and the present model demonstrates an experimental evaluation error of 0.33 eV with good size transferability to larger organic molecules. An equivariant graph neural network is benchmarked against its rotationally invariant analogue and a model comprised of the smooth overlap of atomic positions descriptors and kernel ridge regression for training data efficiency and stability to non-equilibrium geometries absent from the training data. All models show good training data efficiency and the graph based models have improved transferability to non-equilibrium geometries. The use of chemically informed, graph-normalized node features reduces the graph neural network's dependence on message passing depth. A case study on the 45 atom avobenzone tautomers demonstrates the model's ability for instant and precise analysis of complex molecules. The software and data are provided by the open-source AugerNet package at https://doi.org/10.5281/zenodo.19689244.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.27070) | 2026-08-04
