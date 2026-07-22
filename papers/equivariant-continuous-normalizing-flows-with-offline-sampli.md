---
title: "Equivariant Continuous Normalizing Flows with Offline Sampling for Fermionic Ground State Estimation"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.18486"
summary: "arXiv:2607.18486v1 Announce Type: new Abstract: We introduce a framework for fermionic variational Monte Carlo (VMC) in which a continuous normalizing flow (CNF) refines a fixed antisymmetric base wav"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2607.18486v1 Announce Type: new Abstract: We introduce a framework for fermionic variational Monte Carlo (VMC) in which a continuous normalizing flow (CNF) refines a fixed antisymmetric base wavefunction. The flow is implemented as a permutation-equivariant neural ODE, a smooth, topology-preserving map that learns correlations not captured by the base; equivariance preserves the antisymmetry of the base, so the flow can in principle improve any antisymmetric ansatz that can be sampled efficiently. We demonstrate this using Slater and Jastrow-Slater bases, though more expressive choices are admissible. Exact samples from the flow's Born distribution are obtained by pushing pre-cached base samples through the forward ODE, requiring no Markov chain Monte Carlo (MCMC) at training time. The base samples are generated offline and reused across training batches and runs, decoupling sample generation from parameter optimization and enabling embarrassingly parallel training across multiple GPUs. We introduce three novel permutation-equivariant vector field architectures: Pairwise Deep Sets (PDS), FermiNet Vector Fields (FVF), and Pairwise Deep Sets Gradient (PDSG), each offering a different balance of expressivity and computational cost. We further introduce an augmented dynamics formulation for kinetic energy computation that co-evolves the required derivative quantities as ODE state variables, eliminating differentiation through the ODE trajectory and yielding significant reductions in wall-clock time and memory. Training runs on systems of harmonically trapped spinless electrons demonstrate ground-state energies below CISD reference values. Scaling experiments demonstrate near-ideal strong scaling from 1 to 128 NVIDIA A100s using 32 GPU nodes of NERSC's Perlmutter supercomputer for systems of up to N = 48 particles in three dimensions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.18486) | 2026-07-22
