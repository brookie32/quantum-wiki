---
title: "Quantum Approximate Optimisation Algorithm for Protein Sidechain Packing"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31077"
summary: "arXiv:2609.31077v1 Announce Type: new Abstract: Sidechain packing is a critical stage in protein folding, with direct implications for structure-based drug discovery. Google DeepMind's tool, AlphaFold"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2609.31077v1 Announce Type: new Abstract: Sidechain packing is a critical stage in protein folding, with direct implications for structure-based drug discovery. Google DeepMind's tool, AlphaFold2, predicts protein backbone reliably but sidechain positioning less accurately. Recovering the lowest-energy rotamer assignment over a fixed backbone is NP-hard. We present a hybrid quantum-classical pipeline that repacks sidechains on the AlphaFold backbone using the Quantum Approximate Optimisation Algorithm (QAOA), encoding the one- and two-body energies as a quadratic unconstrained binary optimisation (QUBO) problem. We introduce a constraint-preserving ansatz, pairing a W-state initialisation with a cyclic XY ring mixer, that enforces one-hot rotamer validity without penalty terms while keeping two-qubit gate scaling linear in the rotamer count. We also define an asymptotic shot-scaling metric, measured against the experimentally resolved conformation, that fixes optimiser quality independently of the baseline; its fitted growth stays below the classical exhaustive-search rate at moderate rotamer flexibility. Evaluated on bovine pancreatic trypsin inhibitor (5PTI) across high- and moderate AlphaFold-confidence regions, the pipeline lowers conformational energy against the AlphaFold baseline.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31077) | 2026-09-28
