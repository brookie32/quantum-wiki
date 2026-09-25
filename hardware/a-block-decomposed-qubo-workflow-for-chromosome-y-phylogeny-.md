---
title: "A Block Decomposed QUBO Workflow for Chromosome-Y Phylogeny Reconstruction"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29856"
summary: "arXiv:2609.29856v1 Announce Type: cross Abstract: This paper sets out a computational workflow that reconstructs the phylogeny of human Y-chromosome populations from a Variant Call Format (VCF) file o"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29856v1 Announce Type: cross Abstract: This paper sets out a computational workflow that reconstructs the phylogeny of human Y-chromosome populations from a Variant Call Format (VCF) file of biallelic Single Nucleotide Polymorphisms (SNP). The two classical phylogenetic decisions - topology selection and root placement - are cast as Quadratic Unconstrained Binary Optimisation (QUBO) problems. The workflow combines two QUBO formulations with an Alternating Direction Method of Multipliers (ADMM) decomposition strategy and a plug-in Digitized Counter-Diabatic Quantum Optimization (DCQO) solver, enabling large phylogenetic optimization problems to be executed across multiple classical or quantum computing resources. The DCQO gate-based optimizer drives each ADMM-block QUBO with short-depth counter-diabatic circuits in the impulse regime, without the necessity for an outer variational loop. The combination of ADMM decomposition and the DCQO block solver facilitates problem sizes that surpass the qubit budget of any individual digital quantum processing unit call, while maintaining the integrity of the original objective. The workflow extracts genotype information from VCF files, reconstructs topology and rooting through two QUBO formulations, and annotates the resulting tree using PhyloTree. The resultant data set comprises a Nexus-annotated rooted tree, in addition to diagnostic figures. The workflow demonstrates the potential of modest-scale QUBO formulations combined with ADMM decomposition to serve as a scalable alternative to greedy heuristics in the domain of population genomics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29856) | 2026-09-25
