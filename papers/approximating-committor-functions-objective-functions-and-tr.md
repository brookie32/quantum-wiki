---
title: "Approximating committor functions: Objective functions and training data sampling"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2607.21425"
summary: "arXiv:2607.21425v1 Announce Type: new Abstract: Many molecular dynamics simulations aim at studying transitions between two states (from reactants to products). In this context, the committor function"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.21425v1 Announce Type: new Abstract: Many molecular dynamics simulations aim at studying transitions between two states (from reactants to products). In this context, the committor function (which gives for a given molecular configuration the probability to reach the product state before the reactant state) is a pivotal quantity, in particular because it is the optimal importance function for rare event simulation methods such as importance sampling or splitting techniques. These methods are used to sample the reactive path ensemble, and estimate for example the transition rate. However, learning such a function is generally a challenging task due to the high dimensionality of the configuration space. In this work, after reviewing the existing methodologies to construct approximate committor functions, a new loss function based on the application of Ito's formula is proposed to learn the committor function with a minimization procedure on the parameters of a neural network. After comparing this novel approach to existing procedures on the Muller--Brown potential, we introduce a coupling strategy with the Adaptive Multilevel Splitting method to better approximate the committor function using a better sampling of the reactive trajectories. This methodology in which the committor function is iteratively learned only requires initially the knowledge of the reactant and product states.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2607.21425) | 2026-07-24
