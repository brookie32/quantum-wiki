---
title: "Degree-conditioned anneal offsets reshape certified-optimum sampling for minimum vertex cover"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03379"
summary: "arXiv:2610.03379v1 Announce Type: new Abstract: Quantum annealers can sample degenerate optima unevenly, so the composition of finite-read output matters when multiple solutions are sought. We investi"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03379v1 Announce Type: new Abstract: Quantum annealers can sample degenerate optima unevenly, so the composition of finite-read output matters when multiple solutions are sought. We investigate whether problem structure can steer this output through node-dependent anneal offsets for Minimum Vertex Cover (MVC). In MVC, vertex degree equals the number of incident edge-cover constraints and therefore measures local constraint participation. We use this relation to define degree-conditioned offset-scheduled quantum annealing (DC-OSQA), a static rule assigning more negative offsets to vertices with larger max-normalized degree. Experiments used a D-Wave Advantage2 system1 quantum processing unit (QPU). For each graph, DC-OSQA was compared with a zero-offset baseline using the same MVC encoding, fixed physical embedding, majority-vote chain decoding, and 1000-read budget. A sampled bitstring was counted as a certified candidate only if it represented a feasible vertex cover and its cardinality matched the minimum independently certified by integer linear programming. Across 120 paired comparisons on sparse Barabasi-Albert graphs with two attachments per added vertex and graph sizes N = 70-150, DC-OSQA increased the mean number of distinct certified candidates from 171.7 to 455.8 and the mean number of complete-linkage Hamming-distance families from 22.5 to 80.0; paired gains were positive at every tested size. These shifts, together with lower empirical concentration, indicate a change in the composition of the observed certified support. At N = 150, the degree-aligned assignment exceeded the within-instance mean over 20 random reassignments of the same offset values in 19 of 20 graphs for certified-support size and all 20 graphs for Hamming families. Within the tested ensemble, these results show that an MVC-specific degree rule changes the certified optima observed within a fixed QPU read budget.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03379) | 2026-10-05
