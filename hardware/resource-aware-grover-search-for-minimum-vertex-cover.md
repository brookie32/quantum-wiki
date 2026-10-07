---
title: "Resource-Aware Grover Search for Minimum Vertex Cover"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.07252"
summary: "arXiv:2610.07252v1 Announce Type: new Abstract: The Minimum Vertex Cover (MVC) problem is a fundamental NP-hard combinatorial optimization problem with applications in network analysis and resource al"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07252v1 Announce Type: new Abstract: The Minimum Vertex Cover (MVC) problem is a fundamental NP-hard combinatorial optimization problem with applications in network analysis and resource allocation. Grover's algorithm provides a quadratic reduction in query complexity for unstructured search, but existing Grover-based MVC formulations can incur substantial quantum resource overhead due to costly vertex-counting circuits and complex oracle constructions. We develop and evaluate several encoding and oracle-design strategies for reducing the qubit count, circuit depth, and gate complexity of Grover-based MVC search. First, we construct a Dicke-Parallel formulation that restricts the search to fixed-cardinality subsets, eliminating explicit vertex counting, together with a parallel edge-verification oracle that reduces feasibility-checking overhead. We then develop an Edge-Counting formulation that replaces per-edge auxiliary storage with a logarithmic-size counting register, substantially reducing ancillary-qubit requirements. Finally, we propose an Edge-Centric encoding that represents endpoint selections directly and derives vertex-selection states through incident-edge Boolean operations, enabling more depth-efficient oracle construction. Our resource analysis reveals complementary trade-offs among qubit width, circuit depth, gate count, and Grover iteration count. Edge-Counting is particularly attractive under tight qubit constraints, while Edge-Centric can reduce both circuit depth and Grover iteration count when the graph has a moderate edge count and sufficient representation multiplicity. Dicke-Parallel provides a more robust choice when such multiplicity is limited or graph density makes the edge-based search space large. These results provide practical guidance for selecting Grover-based MVC formulations according to hardware constraints and graph structure.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.07252) | 2026-10-07
