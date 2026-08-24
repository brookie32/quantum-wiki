---
title: "Accurate and Transferable Intermolecular Potential Based on Machine-Learned Molecular Electron Density"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.20753"
summary: "arXiv:2608.20753v1 Announce Type: new Abstract: Machine-learned force fields (MLFFs) contain many learnable parameters and therefore require large training datasets. This poses a challenge for develop"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.20753v1 Announce Type: new Abstract: Machine-learned force fields (MLFFs) contain many learnable parameters and therefore require large training datasets. This poses a challenge for developing highly accurate, general-purpose MLFFs because generating high-quality ab initio reference data is computationally expensive. Classical empirical potentials offer a potentially inexpensive source of synthetic training data, but existing models often lack the accuracy needed to provide useful reference energies. Here, we introduce the density-based intermolecular potential (DensIP), a physics-based model of intermolecular interactions that uses machine-learned electron densities and only four universal parameters. We train and test DensIP on CCSD(T)/CBS interaction energies from DES15K, a dataset of dimers of small organic molecules. DensIP achieves sub-kcal/mol errors for dimers containing molecules absent from the training set, including molecules in non-equilibrium conformations, demonstrating strong transferability. We further show that DensIP can be applied to molecules as large as drug ligands. Notably, DensIP outperforms state-of-the-art general-purpose MLFFs for long-range interactions, making it a promising approach for generating accurate synthetic training data at scale.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.20753) | 2026-08-24
