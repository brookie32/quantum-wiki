---
title: "Integrated Alchemical and Conformational Enhanced Sampling for Solvation Free Energy Calculations"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.12691"
summary: "arXiv:2608.12691v1 Announce Type: new Abstract: Accurate solvation free energies from molecular dynamics simulations require efficient sampling of coupled slow variables, including solvent coordinates"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12691v1 Announce Type: new Abstract: Accurate solvation free energies from molecular dynamics simulations require efficient sampling of coupled slow variables, including solvent coordinates, solute conformational modes, and the alchemical coordinate lambda. Here, we develop a lambda-dynamics framework that combines mass scaling, on-the-fly probability enhanced sampling (OPES), and driven adiabatic free energy dynamics (d-AFED) to address these sampling challenges within a unified protocol. For rigid organic solutes, Hamiltonian replica exchange with mass scaling is first used to quantify the effect of octanol solvent relaxation. Reducing all octanol atomic masses by a factor of ten accelerates convergence by more than fivefold while preserving equilibrium solvation free energies. These calculations then provide reference benchmarks for lambda-OPES, a dual-bias lambda-dynamics strategy that combines the "standard" and "explore" variants of OPES to promote transitions along the alchemical coordinate. This approach reaches convergence on timescales comparable to replica exchange, but without predefined lambda windows or multiple parallel simulations. For flexible N-acetyl amino-acid amide solutes, lambda-OPES is coupled with d-AFED on selected backbone and side-chain dihedrals to enable simultaneous alchemical and conformational enhanced sampling. This combined strategy improves agreement with experimental octanol-water partition coefficients and reduces the mean absolute error from 0.75 log units with lambda-OPES alone to 0.30 log units with lambda-OPES-d-AFED. Overall, this work establishes an integrated enhanced sampling protocol for solvation free energy calculations across rigid organic solutes and flexible peptide-like solutes, and provides a foundation for the application of alchemical free energy methods to larger and more conformationally complex systems.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.12691) | 2026-08-14
