---
title: "Evaluating Electrostatic Embedding MLIP/MM for Relative Binding Free Energy Calculations"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.13355"
summary: "arXiv:2608.13355v1 Announce Type: new Abstract: Alchemical relative binding free energy (RBFE) calculations are limited by the fixed-charge approximation of classical force fields. Hybrid machine lear"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.13355v1 Announce Type: new Abstract: Alchemical relative binding free energy (RBFE) calculations are limited by the fixed-charge approximation of classical force fields. Hybrid machine learning interatomic potential/molecular mechanics (MLIP/MM) schemes correct ligand strain, but under mechanical embedding still describe ligand--environment electrostatics with static point charges. Electrostatic embedding schemes coupling machine-learned charges to the MM environment have been proposed and validated against QM/MM for simple systems, but not tested in a production alchemical workflow. We take the electrostatic embedding scheme of Semelak et al. and evaluate it on protein--ligand RBFE. We trained a TensorNet2 model, exttt{AceFF-2-RESP-1}, on 10^{6} conformations from the AceFF dataset, jointly predicting energies, forces and Restrained Electrostatic Potential (RESP) charges. We chose RESP over MBIS for commensurability with the AMBER-family force field it couples to. The predicted charges enter the short-range direct-space part of the particle mesh Ewald sum, with Thole damping to prevent polarization catastrophes during alchemical transformations. We tested the scheme across five targets from the Wang et al. benchmark set, fixed in advance by a prior study, with three replicates per edge and matched protocols. Electrostatic embedding improved every accuracy and correlation metric for TYK2 (DeltaDelta G RMSE 0.86 rightarrow 0.45~kcal/mol against GAFF2), but performed comparably to the classical and mechanical-embedding baselines for CDK2, thrombin, p38 and JNK1. Standard single-molecule energy and charge benchmarks were not good predictors of this target-dependent outcome. TYK2 combined good DeltaDelta G accuracy with the lowest force error on the Schrodinger benchmark, but this pattern did not hold for the other targets.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.13355) | 2026-08-14
