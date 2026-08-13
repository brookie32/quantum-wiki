---
title: "A Quantum Circuit Framework for Protein Ensemble-Level Energetics"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05491"
summary: "arXiv:2608.05491v1 Announce Type: cross Abstract: Proteins occupy heterogeneous free-energy landscapes in which high-entropy ensembles converge toward compact, low-energy basins with multiple sub-stat"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.05491v1 Announce Type: cross Abstract: Proteins occupy heterogeneous free-energy landscapes in which high-entropy ensembles converge toward compact, low-energy basins with multiple sub-states. Molecular dynamics can access these landscapes at atomic resolution, but exhaustive sampling remains computationally demanding. Meanwhile, most quantum approaches target only single optimal structures, leaving full ensemble energetic heterogeneity unexplored. We introduce a residue-level, gate-based quantum circuit framework for coarse-graining protein thermodynamics. Each amino acid is represented as a two-state qubit (stabilised vs. excited solvation state) based on residue solvation energetics. A structure-informed entanglement block then encodes covalent and non-covalent contacts using parameterised controlled gates, embedding correlations across the residue-interaction network. Sampling the circuit (sim 10^6 measurements) yields binary thermodynamic microstates used to compute protein energy distributions, residue-level statistical couplings, energetic sensitivities, and information gains relative to total free energy. We showcase the framework on the benchmark Trp-cage miniprotein 1L2Y (TC5b) and 9GDL, a disulfide-stabilised Trp-cage-fortified exenatide chimera. For 1L2Y, the circuit reproduces a structured, folding-funnel-like energy distribution. Comparative analysis with 9GDL reveals shifts in global energy distributions and residue-level stability profiles. Coupling and information-theoretic analyses localise residues associated with ensemble reorganisation, while multi-body couplings show the circuit resolves both direct and indirect statistical correlations. This framework expands quantum protein modelling beyond single-structure optimisation toward ensemble-level characterisation, capturing key features of rugged energy landscapes to guide protein design, mutation mapping, and allosteric pathway identification.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05491) | 2026-08-13
