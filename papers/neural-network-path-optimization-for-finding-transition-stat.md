---
title: "Neural Network Path Optimization for Finding Transition States on a Machine Learned Potential"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.22272"
summary: "arXiv:2611.22272v1 Announce Type: new Abstract: Transition states govern chemical reaction rates and outcomes, yet locating them remains a central challenge in computational chemistry. Double-ended se"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22272v1 Announce Type: new Abstract: Transition states govern chemical reaction rates and outcomes, yet locating them remains a central challenge in computational chemistry. Double-ended search methods find transition states given reactant and product structures, but generally rely on discretized path representations developed for density functional theory, where potential energy surface evaluations are expensive. Machine learned interatomic potentials (MLIPs) dramatically reduce this cost and leverage automatic differentiation to access higher-order derivatives efficiently. We introduce Popcornn, a framework to find transition states by optimizing continuous neural network paths atop an MLIP with a parallelized adaptive numerical integrator. This combination eliminates path discretization artifacts, reduces hyperparameter sensitivity, and enables non-local optimization to overcome local features using second-order potential-energy-surface information. Popcornn consistently recovers more correct transition states than standard methods such as nudged elastic band and growing string, across MLIPs on thousands of organic reactions, establishing it as a robust, automation-ready method for high-throughput transition state search. Popcornn's infrastructure is flexible in path objective, integration strategy, and optimization algorithm, making it a practical tool and platform for investigating open questions in MLIP-based path optimization.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.22272) | 2026-11-18
