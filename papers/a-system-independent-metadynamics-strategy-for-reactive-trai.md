---
title: "A System-Independent Metadynamics Strategy for Reactive Training Data: Application to Gas-Phase Organic Reactions"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.29105"
summary: "arXiv:2609.29105v1 Announce Type: new Abstract: General-purpose machine-learning interatomic potentials (MLIPs) for organic reactions need to be accurate on both the minimum energy path (MEP) for stat"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29105v1 Announce Type: new Abstract: General-purpose machine-learning interatomic potentials (MLIPs) for organic reactions need to be accurate on both the minimum energy path (MEP) for static evaluation of basic properties and the broader configurational space for simulating reaction dynamics. Existing general datasets for gas-phase organic reactions rely on quasi-static relaxation that confines configurations to the MEP vicinity, so models trained on them could fail on direct molecular-dynamics trajectories; the gap is methodological, not a question of dataset size. We introduce a spatiotemporally resolved, system-independent collective variable (CV): Cartesian RMSD within randomly partitioned local domains against an expanding list of time-averaged reference geometries. The CV drives metadynamics as the main exploration engine, supplemented by structural relaxation towards transition state (TS) to augment the coverage around TS. Within a concurrent-learning workflow, this produces OpenRxn26, a dataset of 1.8~M DFT-labeled configurations covering neutral singlet unimolecular reactions in the H/C/N/O chemical space (N_heavy leq 30), containing reactive atomic environments underrepresented in community datasets. Trained on OpenRxn26, a DPA3 model (denoted DPA3_rxn) achieves transferable accuracy on barrier heights and reaction energies. On off-MEP reactive trajectories, DPA3_rxn is the only model in the benchmark suite to reach 1.0 kcal/mol energy accuracy compared with the labeling method, where the domain MLIP leading on static benchmarks degrades several-fold (e.g. MACE_OMol25), showing the insufficiency of quasi-static sampling and MEP-anchored benchmarks for guaranteeing dynamics reliability of MLIPs. OpenRxn26 thus provides MD-ready reactive training data for gas-phase neutral singlet organic reactions, verifying the generality and efficiency of the sampling strategy.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.29105) | 2026-09-25
