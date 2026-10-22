---
title: "Mamba Quantum Eigensolver (MQE): A Selective State Space Model for Scalable Ground State Simulations in Quantum Chemistry"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29779"
summary: "arXiv:2610.29779v1 Announce Type: cross Abstract: Predicting molecular electronic structure using Quantum Computing approaches is a challenge in Computational Chemistry. Traditional Variational Quantu"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29779v1 Announce Type: cross Abstract: Predicting molecular electronic structure using Quantum Computing approaches is a challenge in Computational Chemistry. Traditional Variational Quantum Eigensolvers (VQEs) are typically hindered by optimization challenges. The alternative Generative Quantum Eigensolver (GQE) mitigates this by reformulating ground-state search as discrete sequence generation, but its Transformer backbone suffers from quadratic computational complexity, bottlenecking scalability for larger molecules. To address this, we introduce the Mamba Quantum Eigensolver (Mamba-QE), which replaces the Transformer with a Selective State Space Model (SSM) to process operator sequences with linear O(L) complexity. Additionally, we integrate a distance-conditioned mechanism enabling the direct prediction of complete potential energy surfaces (PES). Evaluated on the H_2 molecule, Mamba-QE reproduces Full Configuration Interaction (FCI) reference energies well within chemical accuracy, achieving an energy error below 3imes10^{-6} Ha across 16 geometries with zero variational violations. Mamba-QE maintains high expressive power while establishing a robust, scalable foundation for quantum simulations of complex molecular systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29779) | 2026-10-22
