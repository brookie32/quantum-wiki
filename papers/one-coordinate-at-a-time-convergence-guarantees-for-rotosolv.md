---
title: "One Coordinate at a Time: Convergence Guarantees for Rotosolve in Variational Quantum Algorithms"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25613"
summary: "arXiv:2604.25613v1 Announce Type: new Abstract: In this paper, we resolve an open question in the field of optimization algorithms for training parametrized quantum circuits: Does the popular Rotosolv"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25613v1 Announce Type: new Abstract: In this paper, we resolve an open question in the field of optimization algorithms for training parametrized quantum circuits: Does the popular Rotosolve algorithm converge? Until now, interpolation-based coordinate descent methods such as Rotosolve have mostly been treated as heuristics, lacking any formal convergence guarantees. We rigorously analyze Rotosolve, and show that it converges to arepsilon-stationary points if the optimization landscape is non-convex and smooth; and to arepsilon-suboptimal points if the objective function additionally obeys the Polyak-Lojasiewicz (PL) condition. Further, we derive explicit worst-case rates of convergence in the finite quantum measurement regime. These rates are contrasted against those from a similar coordinate-based method: Randomized Coordinate Descent (RCD). Although in the worst case their rates are, prima facie, equivalent, we present arguments for a more nuanced comparison between the two. We highlight that Rotosolve is hyperparameter-free, and implicitly uses first and second derivatives in its updates. Finally, we supplement our theoretical findings with numerical experiments from Quantum Machine Learning; and compare the performance of Rotosolve against RCD, Stochastic Gradient Descent, Simultaneous Perturbation Stochastic Approximation, and Randomized Stochastic Gradient Free methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25613) | 2026-04-29
