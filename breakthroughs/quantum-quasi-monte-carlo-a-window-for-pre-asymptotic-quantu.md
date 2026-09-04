---
title: "Quantum Quasi-Monte Carlo: a window for pre-asymptotic quantum advantage"
date: "2026-09-04"
updated: "2026-09-04"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03625"
summary: "arXiv:2609.03625v1 Announce Type: new Abstract: Numerical integration with Monte Carlo methods is a central computational task in many scientific and industrial applications, including financial deriv"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

arXiv:2609.03625v1 Announce Type: new Abstract: Numerical integration with Monte Carlo methods is a central computational task in many scientific and industrial applications, including financial derivative pricing and risk management. Classical Monte Carlo algorithms are computationally demanding: achieving an accuracy epsilon typically requires a number of function evaluations scaling as O(1/epsilon^2). Quantum-accelerated Monte Carlo methods based on quantum amplitude estimation can in principle quadratically improve this dependence. However, extit{quasi}-Monte Carlo methods have not been explored in the quantum context. In this work, we introduce a quantum quasi-Monte Carlo algorithm that combines low-discrepancy nets with quantum amplitude estimation. The proposed method prepares the quasi-random point set coherently in superposition. The method does not yield an asymptotic improvement over classical quasi-Monte Carlo, since the total error separates into a discretization error, determined by the finite net, and a quantum estimation error. Instead, we explore a pre-asymptotic advantage window: for a target accuracy that would classically require 2^q low discrepancy points, one can prepare a higher-resolution net of size 2^Q, with Q>q, in superposition and reach the same accuracy using significantly fewer function queries. This window can be controlled by tuning the circuit resolution and amplitude-estimation parameters, making the approach relevant for practical regimes where the number of queries is finite rather than asymptotically large.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03625) | 2026-09-04
