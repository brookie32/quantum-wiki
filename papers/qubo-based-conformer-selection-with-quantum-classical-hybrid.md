---
title: "QUBO-Based Conformer Selection with Quantum-Classical Hybrid Optimization for Multiconformer Ligand Modeling"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29058"
summary: "arXiv:2610.29058v1 Announce Type: new Abstract: A ligand can adopt multiple conformations within the same binding site, and these conformations can interact differently with the surrounding protein. M"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29058v1 Announce Type: new Abstract: A ligand can adopt multiple conformations within the same binding site, and these conformations can interact differently with the surrounding protein. Multiconformer modeling must therefore determine which candidate conformations to retain and what occupancies to assign to them. An established automated approach uses mixed-integer quadratic programming (MIQP) with hard occupancy and conformer-count limits for this selection. Here, we reformulated conformer selection as a quadratic unconstrained binary optimization (QUBO) problem with finite penalties and discrete occupancies. We solved the QUBO using a quantum-classical hybrid solver. We compared this workflow with the MIQP-based qFit-ligand workflow across 83 paired X-ray ligand entries using the same experimental inputs and the same qFit-ligand processing protocol. For each entry, both final models were evaluated against the same composite-omit map generated from the common input structure before the two workflows diverged. Quantum-qFit produced higher ligand-region real-space correlation coefficients (RSCC) in 62 entries 74.7% and lower occupancy-weighted torsional strain in 66 entries 79.5%. Similar directional trends remained in the 28 entries with matched final conformer counts. The molecular Electron Density for Individual Atoms score (EDIAm) decreased in most entries. This result shows that higher regional map agreement did not necessarily correspond to stronger atom-level density support. Overall, the results show that the conformer-selection formulation can change which ligand states are represented from the same experimental data and provide a QUBO framework for studying multiconformer ligand selection.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29058) | 2026-10-22
