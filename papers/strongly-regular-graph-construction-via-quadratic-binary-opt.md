---
title: "Strongly Regular Graph Construction via Quadratic Binary Optimization"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.30142"
summary: "arXiv:2610.30142v1 Announce Type: cross Abstract: Strongly regular graphs, hereafter SRGs, are highly structured combinatorial objects of central interest in algebraic graph theory and quantum informa"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30142v1 Announce Type: cross Abstract: Strongly regular graphs, hereafter SRGs, are highly structured combinatorial objects of central interest in algebraic graph theory and quantum information, whose explicit construction becomes rapidly intractable as the number of vertices grows; Conway's still unresolved 99-graph problem is an emblematic example. The matrix equation defining SRGs is quadratic in the binary edge variables, so the natural penalty enforcing it, a sum of squared residuals, is quartic and lies outside quadratic unconstrained binary optimization, known as QUBO. We prove a considerably stronger obstruction, namely that no quadratic function of the edge variables has the labeled SRGs as its exact set of global minimizers, except for three degenerate families given by the perfect matchings, the cocktail-party graphs and the pentagon. In particular, we formally establish that the 99-vertex graph of Conway's problem cannot be obtained from any QUBO over the edge variables without auxiliary variables. Guided by this theorem we develop two complementary algorithms. The first operates within pure QUBO, solves the degenerate families exactly, and beyond them works as a generate--prune--verify pipeline whose output is a reduced set of candidates certified by a polynomial-time classical test. The second solves the full problem by quadratizing this quartic penalty through Rosenberg auxiliary variables, whose number grows as Theta(N^3) with the number of vertices N. We test the pure-QUBO route under simulated annealing on all feasible families with at most 18 vertices and the auxiliary-variable route on representative targets up to 16 vertices, and tabulate the algebraically feasible parameter sets for graphs with at most 49 vertices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.30142) | 2026-10-23
