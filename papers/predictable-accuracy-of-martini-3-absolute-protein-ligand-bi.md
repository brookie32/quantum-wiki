---
title: "Predictable Accuracy of Martini 3 Absolute Protein-Ligand Binding Free Energies across 15 Targets"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.11714"
summary: "arXiv:2610.11714v1 Announce Type: new Abstract: Alchemical free-energy calculations predict protein-ligand binding affinities with close-to-experimental accuracy, but their cost restricts them to smal"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.11714v1 Announce Type: new Abstract: Alchemical free-energy calculations predict protein-ligand binding affinities with close-to-experimental accuracy, but their cost restricts them to small sets of ligands. Coarse-grained (CG) models such as Martini 3 retain a rigorous statistical-mechanical treatment at a fraction of this cost, yet their accuracy for protein-ligand binding has not been assessed systematically. Here, we compute absolute binding free energies for 172 ligands across 15 protein targets with a Martini 3 double-decoupling protocol and compare them against atomistic FEP+ and OpenFE references. Martini underbinds for every target, by 2.7 to 8.7 kcal/mol. This offset is systematic: it comprises a uniform contribution that grows with the number of charged pocket residues. A linear model in this number, which requires only the protein structure, reduces the mean absolute error from 5.7 to 1.2 kcal/mol in leave-one-out cross-validation, close to the 1.0 kcal/mol obtained with exact per-target offsets. The ranking of ligands within a target varies more widely (median Spearman rho of 0.32, from -0.41 to 0.89) and is rationalized by the structure-activity relationship of each series: Martini ranks ligands well when their affinity is driven by hydrophobicity, pi-stacking, or size, and poorly when it is driven by hydrogen bonding or charge. Both trends follow from Martini's calibration against bulk partitioning, which captures neither the dielectric environment of a binding pocket nor the directionality of hydrogen bonds. While MMGBSA retains the atomistic detail needed to rank congeneric ligands, Martini yields physically meaningful free energies, and its coarse-graining maps many atomistically distinct molecules onto one representation, making it a complementary tool for rapidly spanning chemical space.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.11714) | 2026-10-09
