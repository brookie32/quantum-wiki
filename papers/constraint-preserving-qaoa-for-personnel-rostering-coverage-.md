---
title: "Constraint-Preserving QAOA for Personnel Rostering: Coverage-Preserving and Guarded-XY Mixer Constructions"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09145"
summary: "arXiv:2607.09145v2 Announce Type: replace Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a promising framework for combinatorial optimization, but constrained problems are commonly"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2607.09145v2 Announce Type: replace Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a promising framework for combinatorial optimization, but constrained problems are commonly handled using energetic penalty terms that require calibration and allow infeasible configurations to remain dynamically accessible. We develop a constraint-preserving QAOA framework for personnel rostering in which hard scheduling constraints are embedded directly into the mixer Hamiltonian. Using a binary rostering model with daily coverage and no-consecutive-duty constraints, we formulate the dynamics from a transition-graph perspective and introduce a guarded-XY mixer that confines the evolution to the fully feasible scheduling manifold. We further distinguish feasibility preservation from feasible-transition design and propose a tight-pattern extension that introduces collective feasible exchanges in saturated workload segments where local guarded exchanges alone are insufficient. Exact statevector simulations demonstrate that, compared with Penalty-X and Coverage-XY formulations under both expectation-value and Conditional Value-at-Risk optimization, the proposed approach eliminates hard-constraint penalty calibration, guarantees feasible evolution by construction, and consistently yields higher-quality output distributions with stronger concentration on optimal feasible schedules. To the best of our knowledge, this is the first constraint-preserving QAOA formulation for personnel rostering, and the transition-graph framework is readily applicable to a broad class of constrained quantum optimization problems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09145) | 2026-08-04
