---
title: "Superlinear Quantum Query Lower Bounds for Subgraph Detection"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40263"
summary: "arXiv:2609.40263v1 Announce Type: new Abstract: Subgraph detection asks whether an n-vertex graph, accessed through queries to its adjacency matrix, contains a copy of a fixed graph H. We prove the fi"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40263v1 Announce Type: new Abstract: Subgraph detection asks whether an n-vertex graph, accessed through queries to its adjacency matrix, contains a copy of a fixed graph H. We prove the first unconditional superlinear lower bounds on the bounded-error quantum query complexity of this problem, answering a longstanding open question. A copy of H is a certificate of constant size, so the adversary method with nonnegative weights cannot prove superlinear lower bounds. For every fixed rge 4, detecting the clique K_r requires n^{lambda_r-o(1)} queries, where lambda_4=19/18, the exponents lambda_r increase strictly with r, and lambda_rge 2-4sqrt{2/r}+O(1/r). More generally, we prove superlinear lower bounds for detecting every fixed connected graph H with chromatic number cge 4. These bounds approach quadratic as c grows: for sufficiently large c, detection requires n^{2-O(sqrt{loglog c/c})-o(1)} queries. Chromatic number alone does not characterize the quantum query complexity of subgraph detection: we show that detecting the complete bipartite graph K_{r,r} requires n^{eta_r-o(1)} queries, where eta_{10}=181/180 and eta_rge 2-O(1/sqrt{r}). Our main technical result is a lower bound for finding an all-ones certificate from a known family when the input bits are sampled independently. Its proof combines Zhandry's compressed oracle (CRYPTO 2019) with conditioning on a randomly planted certificate, adapting an argument of Belovs (FOCS 2026). Our hard instances are built from graphs containing many copies of the desired subgraph with limited overlap. For cliques, we use a construction of Gowers and Janzer (CPC 2021); for complete bipartite graphs, we use a random construction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40263) | 2026-10-01
