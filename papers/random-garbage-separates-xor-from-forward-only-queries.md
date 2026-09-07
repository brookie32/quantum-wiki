---
title: "Random Garbage Separates XOR from Forward-Only Queries"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.03628"
summary: "arXiv:2609.03628v1 Announce Type: cross Abstract: We give exponential quantum query separations between the standard XOR interface and two forward-only interfaces that supply neither an adjoint nor an"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.03628v1 Announce Type: cross Abstract: We give exponential quantum query separations between the standard XOR interface and two forward-only interfaces that supply neither an adjoint nor an inverse oracle. Let X=F_2^n, N=|X|, and f_{h,r}(x)=(h(x),x,r_x), where h:Xo X is promised to be either a permutation or a Simon two-to-one function, and r is a fixed table of n-bit tags, unrestricted by the promise and reused on every query. The resulting problem is solvable with at most n+2 standard XOR queries, but has forward-erasing query complexity Theta(sqrt N). This answers affirmatively open question 11 in [Scott Aaronson. Open problems related to quantum query complexity. ACM Transactions on Quantum Computing, 2(4):14:1-14:9, 2021] . We also embed these instances into permutations. The detailed construction retains the copy of x in each prescribed output, but for these promises that copy can be replaced by one bit that distinguishes the two inputs in every Simon pair. This gives a permutation domain of size L=4N^2 and a permutation problem with the same standard-query upper bound and forward-only in-place query complexity Theta(sqrt N)=Theta(L^{1/4}). Both lower bounds remain valid with a clean coherent bypass. The common lower bound uses an analysis-only recording replacement. In the replacement computation, tracing out the fixed random tag table after T calls gives a sum of positive-semidefinite operator contributions, each depending on h at no more than T addresses. On such a set, the restrictions induced by random permutations and random Simon functions differ only if the set contains a hidden Simon pair, an event of probability O(T^2/N).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.03628) | 2026-09-07
