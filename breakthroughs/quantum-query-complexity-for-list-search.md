---
title: "Quantum Query Complexity for List Search"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38736"
summary: "arXiv:2609.38736v1 Announce Type: new Abstract: Searching in a linked list is one of the most basic problems in classical algorithms. Although the nodes of the list come with memory addresses, classic"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38736v1 Announce Type: new Abstract: Searching in a linked list is one of the most basic problems in classical algorithms. Although the nodes of the list come with memory addresses, classically those addresses play no role in the cost of search: one simply starts at the head and follows successor pointers to search for an element. In this paper, we show that the quantum setting is different. Here, the ambient address space from which the list vertices are drawn can itself affect the query complexity. We study the following problem analogous to search in a linked list in the query complexity model: the input consists of an address universe [N], a public start symbol s, a successor oracle f whose non-perp values trace a hidden simple path s o a_1 o a_2 o dots o a_ell o perp, and a marking oracle g that marks at most one list vertex. The task is to decide whether the list contains a marked vertex. We prove that both the decision and search versions of this problem for all N ge ell ge 1 have quantum query complexity Theta!igl(min{ell,(Nell)^{1/4}}igr). Thus, quite surprisingly, when N < ell^3 the optimal quantum complexity is (Nell)^{1/4}, which is strictly smaller than the Theta(ell) cost of ordinary linked-list traversal. This gives a precise characterization of when the ambient address space yields a genuine quantum advantage for linked-list search. We extend our results and give the same tight asymptotic bounds for the natural double linked-list version as well.



## Related
- [[deterministic-quantum-search-for-arbitrary-initial-success-p|Deterministic Quantum Search for Arbitrary Initial Success Probabilities]]
- [[parallel-quantum-advantage-with-limited-adaptivity-requires-|Parallel Quantum Advantage with Limited Adaptivity Requires Structure]]
- [[harnessing-problem-structure-for-end-to-end-quantum-speed-up|Harnessing problem structure for end-to-end quantum speed-ups]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38736) | 2026-10-01
