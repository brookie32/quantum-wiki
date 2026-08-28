---
title: "Quantum Rare-Event Estimation for Ising Graphical Models with Belief-Propagation State Preparation"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.26840"
summary: "arXiv:2608.26840v1 Announce Type: new Abstract: Quantum amplitude estimation can reduce the sampling cost of rare-event probability estimation, but applying it to correlated Ising graphical models is "
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.26840v1 Announce Type: new Abstract: Quantum amplitude estimation can reduce the sampling cost of rare-event probability estimation, but applying it to correlated Ising graphical models is limited by the difficulty of preparing the target distribution and building a practical event oracle. This work explores two approximate strategies for mitigating these challenges. We introduce a sample-free state-preparation method combining loopy belief propagation with the Chow--Liu algorithm. The resulting tree approximation is compiled into a quantum circuit with linear gate count and depth, and its accuracy is evaluated across graph families spanning different topologies, coupling strengths, and coupling signs. We also construct a structural oracle that evaluates threshold rules with reversible Boolean gates. Using a twenty-node supply-chain disruption model as a case study, we compare maximum likelihood amplitude estimation against four classical Monte Carlo baselines. Under the fixed-depth schedule used throughout this work, the quantum estimator has the same asymptotic error scaling as the classical methods but achieves lower estimation error by a constant factor. This reduction narrows when amplitude-encoding queries replace raw shots as the resource metric. We separate statistical error from the deterministic errors caused by approximate state preparation and oracle construction, and identify the requirements for achieving an improvement beyond a constant factor.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.26840) | 2026-08-28
