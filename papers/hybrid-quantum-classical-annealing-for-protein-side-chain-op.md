---
title: "Hybrid Quantum-Classical Annealing for Protein Side-Chain Optimization: A Feasibility Study"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08696"
summary: "arXiv:2611.08696v1 Announce Type: cross Abstract: Hybrid quantum-classical annealing solvers are moving from research laboratories toward industrial use, but their advantage over classical optimizatio"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2611.08696v1 Announce Type: cross Abstract: Hybrid quantum-classical annealing solvers are moving from research laboratories toward industrial use, but their advantage over classical optimization appears to be confined to a narrow class of problems. A recent systematic benchmark of the D-Wave hybrid solver against industry-leading classical solvers, across several classes of optimization problems, found it to be most competitive on binary quadratic programs, while noting that few industrial problems take this form. Therefore, identifying real-world industrial problems that can be modeled with this structure is a key challenge. We propose protein side-chain optimization, a core step of computational protein design, as one of these problems: it is natively a binary quadratic program, and its application context requires pools of low-energy solutions, which annealers naturally return. In this feasibility study, we test whether the competitiveness of the hybrid solver against industry-leading classical solvers extends to this problem. On 40 instances derived from 20 experimentally determined protein structures with up to about 200 amino acids and 2000 binary variables, we compare the results achieved with a hybrid solver, run for 5 seconds, against those of the commercial solver Gurobi, run for 10 seconds, 1000 seconds, and 4 hours. The hybrid solver reaches the certified optimum whenever one is available, matches Gurobi's performance on smaller instances, and outperforms it on larger instances, finding lower-energy solutions. These results show that the competitiveness of the hybrid solver on binary quadratic programs, so far observed only on a synthetic benchmark, extends to a real-world problem. This motivates comparisons with classical heuristics specific to protein side-chain optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08696) | 2026-11-09
