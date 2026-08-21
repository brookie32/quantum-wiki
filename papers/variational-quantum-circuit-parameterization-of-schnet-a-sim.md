---
title: "Variational Quantum Circuit Parameterization of SchNet: A Simulator-Based Feasibility Study for Conservative Molecular Force Fields"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19532"
summary: "arXiv:2608.19532v1 Announce Type: new Abstract: Machine-learning force fields provide a promising route for accelerating molecular simulation by replacing expensive quantum-chemical calculations with "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19532v1 Announce Type: new Abstract: Machine-learning force fields provide a promising route for accelerating molecular simulation by replacing expensive quantum-chemical calculations with differentiable models of molecular energies and atomic forces. However, learning accurate and energy-conserving forces remains challenging, especially when the model must capture both global energy trends and local potential-energy gradients from limited data. In this work, we propose a Hybrid Quantum SchNet architecture that integrates variational quantum circuit modules into the continuous-filter SchNet framework. Quantum modules are inserted into the filter generator, atom-wise update, and readout transformations, allowing quantum-enhanced feature mappings to contribute to distance-dependent interactions and atomic energy prediction while preserving the energy-gradient formulation of forces. The model is evaluated on eight MD17 molecular systems using 1000 training configurations per molecule. Compared with energy-only training, joint energy--force supervision substantially improves both energy and force prediction accuracy. Compared with energy-only training, joint energy--force supervision substantially improves both energy and force prediction accuracy. Averaged over the benchmark, the energy MAE decreases from 2.567 to 0.593 kcal mol^{-1}, while the force MAE decreases from 16.340 to 1.540 kcal mol^{-1} AA^{-1}. Ablation experiments on ethanol further show that the performance of the hybrid model depends on the balance between quantum circuit width, circuit depth, and optimization stability. These results demonstrate that variational quantum circuits can be incorporated into neural force-field architectures and trained end-to-end to improve molecular energy and force prediction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19532) | 2026-08-21
