---
title: "The Expressive Power of Constrained QAOA: What You Might Have MISsed"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.18209"
summary: "arXiv:2609.18209v1 Announce Type: new Abstract: Feasibility-preserving mixer Hamiltonians offer an attractive alternative to penalty encodings for constrained quantum optimization, yet how enforcing c"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18209v1 Announce Type: new Abstract: Feasibility-preserving mixer Hamiltonians offer an attractive alternative to penalty encodings for constrained quantum optimization, yet how enforcing constraints alters the state space reachable by the Quantum Approximate Optimization Algorithm (QAOA) remains largely unexplored. We address this question within the context of the Maximum Independent Set (MIS) problem. Alongside the standard controlled bit-flip mixer, we analyze the alternative mathit{Flipext{-}orext{-}Stay} mixer, whose restriction to the feasible subspace W_{F} corresponds precisely to the shifted negative Laplacian of the independent-set reconfiguration graph. Although both mixers induce identical transitions between independent sets, the diagonal modification changes the spectral structure and can substantially enlarge the set of reachable quantum states. For every connected input graph with at least two vertices, we prove that independently parameterized local controls associated with either mixer generate the full unitary Lie algebra on the feasible subspace. Standard QAOA exhibits a more nuanced algebraic structure. We prove that the dynamical Lie algebra associated with MIS-QAOA employing the conventional mixer embeds into its Flip-or-Stay counterpart. Furthermore, we construct an infinite family of graphs for which the corresponding vacuum-state dynamical group orbits exhibit strictly distinct dimensions, establishing a qualitative expressivity separation between the two architectures. For either mixer, we show that standard QAOA initialized in the empty set can prepare a state supported entirely on maximum independent sets at finite depth. For the free architectures, we also derive an exact loss-variance formula in the unitary-design limit, expressed through the number of feasible independent sets and the variance of their cardinalities.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.18209) | 2026-09-17
