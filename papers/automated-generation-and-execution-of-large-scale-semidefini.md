---
title: "Automated generation and execution of large-scale semidefinite programs for variational two-electron reduced density matrix theory"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.30278"
summary: "arXiv:2610.30278v1 Announce Type: new Abstract: The variational two-electron reduced density matrix (v2RDM) method provides a wave-function-free approach to the description of strong electron correlat"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30278v1 Announce Type: new Abstract: The variational two-electron reduced density matrix (v2RDM) method provides a wave-function-free approach to the description of strong electron correlation whose computational cost scales polynomially with the number of correlated orbitals. Here, we present an automated pipeline for the generation and execution of semidefinite programs (SDPs) associated with the v2RDM problem. Algebraic constraints encoding ensemble N-representability conditions are generated via the p^aggerq second-quantized algebra package, and the p^aggerq-generated expressions are automatically translated into a sparse-matrix representation that can be digested by an appropriate SDP solver. We have implemented a boundary-point SDP (BPSDP) solver in the libsdp package that can execute the v2RDM SDPs on either CPU or GPU hardware. We apply the code in several contexts. First, two-particle conditions are used to describe the 76-orbital model of the iron-molybdenum cofactor (FeMoco) of nitrogenase, the simulation of which requires roughly 25 hours of compute time on a single Nvidia H100 GPU. Second, the performance of high-order (four-particle positivity) conditions is evaluated on a challenging two-dimensional H_{10} cluster problem. Lastly, new classes of positivity constraints for mixed fermion-boson systems are generated and applied within the context of ab initio cavity quantum electrodynamics simulations.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.30278) | 2026-10-23
