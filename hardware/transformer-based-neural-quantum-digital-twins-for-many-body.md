---
title: "Transformer-Based Neural Quantum Digital Twins for Many-Body Spectral Reconstruction and Adaptive Quantum-Annealing Schedule Design"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2505.15662"
summary: "arXiv:2505.15662v3 Announce Type: replace Abstract: We introduce Transformer-based Neural Quantum Digital Twins (Tx-NQDTs) to reconstruct the low-energy spectral evolution of many-body quantum systems"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2505.15662v3 Announce Type: replace Abstract: We introduce Transformer-based Neural Quantum Digital Twins (Tx-NQDTs) to reconstruct the low-energy spectral evolution of many-body quantum systems along quantum-annealing paths, including ground- and first-excited-state energies, spectral gaps, and transition matrix elements, at efficient computational cost. Tx-NQDTs employ a graph-informed Transformer neural network trained to estimate the spectral information needed for annealing-schedule design. We integrate these estimates with an adaptive schedule-construction procedure guided by first-order adiabatic perturbation theory (FOAPT), which is used as a closed-system spectral diagnostic to allocate annealing time near predicted spectral bottlenecks. Experiments on a D-Wave quantum annealer (N=10,15,20 logical variables, with schedules represented by up to 12 control points) show that Tx-NQDT-informed schedules can improve empirical ground-state success probabilities relative to the default 20,mus linear schedule under the tested hardware conditions. The proposed schedules achieve success probabilities 2.2--11.7 percentage points higher across the reported easy and hard subsets and outperform the default baseline in 44 of 60 cases. The results demonstrate the feasibility of using learned logical spectral information to automatically generate adaptive quantum-annealing schedules for practical hardware experiments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2505.15662) | 2026-08-11
