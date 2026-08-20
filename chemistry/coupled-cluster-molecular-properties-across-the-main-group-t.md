---
title: "Coupled-cluster molecular properties across the main group that extrapolate beyond training size"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.18346"
summary: "arXiv:2608.18346v1 Announce Type: new Abstract: Coupled-cluster theory defines the accuracy standard for molecular electronic-structure properties but scales too steeply for routine application, where"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18346v1 Announce Type: new Abstract: Coupled-cluster theory defines the accuracy standard for molecular electronic-structure properties but scales too steeply for routine application, whereas density-functional theory is affordable yet systematically biased. We resolve this trade-off with a single equivariant network, MEHnet-MG, that predicts an effective one-electron Hamiltonian from one inexpensive B3LYP/def2-SVP calculation and derives a broad suite of properties from it (energy, optical gap, dipole, quadrupole, polarizability, Mulliken atomic charges, and Mayer bond orders) at coupled-cluster accuracy across nine main-group elements, including the under-served phosphorus, sulfur, and chlorine chemistries. The model is trained on a new in-house dataset of multi-property labels computed at the CCSD(T) level for all nine elements. On a held-out test set, it reduces the error of every property by a factor of 3.8 to 230 relative to semi-local, hybrid, and double-hybrid DFT (referenced to composite CCSD(T)/cc-pVTZ; Methods), while adding only ~25 ms wall time per molecule, delivering coupled-cluster-quality predictions at the cost of a single DFT calculation. Critically, deriving every property from a predicted Hamiltonian rather than pooling per-atom features builds the correct size-scaling into the model architecture: on pi-conjugated oligothiophenes it matches finite-field CCSD polarizability and the EOM-CCSD optical gap to ~2% at the largest sizes where those references remain affordable (44 and 37 atoms, where a single CCSD field point already costs ~500x the model's entire inference) and extrapolates the corrected trends to 58-atom chains, a regime where pooling-based architectures fail by construction. Accurate extrapolation is therefore set by the model's inductive bias rather than by the training data.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.18346) | 2026-08-20
