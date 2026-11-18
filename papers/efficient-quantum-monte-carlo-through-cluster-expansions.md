---
title: "Efficient Quantum Monte Carlo through Cluster Expansions"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03893"
summary: "arXiv:2610.03893v2 Announce Type: replace Abstract: The sign problem remains a major obstacle to extending the success of Monte Carlo methods to generic quantum many-body systems. A powerful alternati"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2610.03893v2 Announce Type: replace Abstract: The sign problem remains a major obstacle to extending the success of Monte Carlo methods to generic quantum many-body systems. A powerful alternative relies on cluster expansions, which provide convergent representations of free energies and related quantities, with applications ranging from tensor network contractions to quantum dynamics and circuits. Within their convergence regime, these expansions often yield deterministic polynomial-time algorithms. However, such methods require exhaustive enumeration of connected clusters, leading to a computational overhead of (Narepsilon^{-1})^{O(logDelta)}, where N is the system size, arepsilon the desired precision, and Delta the interaction-graph degree. This becomes particularly severe in long-range systems, where Deltaequiv N, resulting in quasi-polynomial runtimes. Here, we introduce a Markov chain algorithm that samples cluster expansions directly in the space of connected clusters, replacing deterministic enumeration by Monte Carlo sampling. Because sampling occurs in an abstract cluster space rather than a physical configuration space, the conventional exponential sign problem is absent within the convergence regime. For general polymer models, we establish an FPRAS with runtime ilde{O}(N^4arepsilon^{-3}). For quantum partition functions at temperatures etaleqeta_{sampling}equivO(1), this improves to ilde{O}(N^{3+1/D}arepsilon^{-3}), where D is the lattice dimension. The framework applies to long-range quantum systems with interactions propto1/r^alpha, including 2-local models with alpha>2D.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03893) | 2026-11-18
