---
title: "MoMPy: automated construction of moment matrices for semidefinite programming relaxations"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16512"
summary: "arXiv:2608.16512v1 Announce Type: new Abstract: We present MoMPy, an open-source Python package that provides a unified, declarative construction of moment matrices for semidefinite programming (SDP) "
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16512v1 Announce Type: new Abstract: We present MoMPy, an open-source Python package that provides a unified, declarative construction of moment matrices for semidefinite programming (SDP) hierarchies. The user declares operator labels together with a small set of structural relations, and MoMPy returns a matrix of SDP variable indices in which every implied identification has already been made, ready for CVXPY or any other modelling layer. Internally, the identification problem is recast as a word-rewriting problem on tuples of integers and solved with a memoised breadth-first closure coupled to a disjoint-set forest, so that each distinct monomial is processed exactly once per build, however many matrix entries it eventually labels. The central abstraction is independent of the physical scenario: the same construction handles tracial, state (NPA), and block-valued moments, with no notion of parties, settings or preparations. We demonstrate this generality on a tripartite Mermin inequality, the bipartite CHSH inequality, measurement compatibility in a steering scenario, state discrimination and dimension witnessing in prepare-and-measure scenarios, device-independent randomness certification, and certification of deterministic correlations from known ensembles. The construction is validated against an independent brute-force implementation and benchmarked across eight structurally distinct scenarios, spanning bipartite and tripartite Bell tests, heterogeneous-outcome, steering-type, jointly-measurable and network configurations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16512) | 2026-08-18
