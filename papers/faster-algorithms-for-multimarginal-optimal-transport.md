---
title: "Faster Algorithms for Multimarginal Optimal Transport"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09513"
summary: "arXiv:2608.09513v1 Announce Type: new Abstract: We study algorithms for approximating the multimarginal optimal transport (MOT) distance, a generalization of the classic optimal transport distance, be"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09513v1 Announce Type: new Abstract: We study algorithms for approximating the multimarginal optimal transport (MOT) distance, a generalization of the classic optimal transport distance, between m discrete probability distributions each supported on at most n points. We give a classical algorithm that computes a coupling between these marginals whose expected transportation cost is within an additive arepsilon > 0 of the MOT distance in time O(m^2 n^m arepsilon^{-1}polylog(m,n,arepsilon^{-1})). This is, to our knowledge, the first bound for general MOT problems with simultaneous linear dependence on the dimension n^m and on the accuracy parameter arepsilon^{-1}, improving the prior state of the art. On the quantum side, we give two algorithms that achieve speedups in dimension, though with worse accuracy dependence than classical approaches. First, we construct a quantum projected subgradient method for estimating the MOT distance within an additive arepsilon >0 with runtime O( m^3 n^{frac{m}{2}+1} arepsilon^{-2} polylog(m,n,arepsilon^{-1})). This algorithm works with the linear programming dual of the MOT problem, and does not return a coupling. We also give a quantum multimarginal Sinkhorn algorithm for entropy-regularized MOT. This algorithm returns an implicit description of an approximately optimal coupling with runtime O(m^8n^{frac{m+1}{2}} arepsilon^{-5} polylog(m,n,arepsilon^{-1}))) after the usual reduction from entropic MOT to unregularized MOT. We also record query lower bounds: for any precision arepsilon<1/2, randomized classical algorithms require Omega(n^m/(1+arepsilon n)) queries and quantum algorithms require Omega(sqrt{n^m/(1+arepsilon n)}) queries.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09513) | 2026-08-11
