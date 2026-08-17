---
title: "Efficient Multiparty Entanglement Distribution in Dynamic Quantum Networks"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2408.07118"
summary: "arXiv:2408.07118v3 Announce Type: replace Abstract: Distributing multipartite entanglement over a quantum network means routing it through a shared resource state. Existing measurement-based schemes s"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2408.07118v3 Announce Type: replace Abstract: Distributing multipartite entanglement over a quantum network means routing it through a shared resource state. Existing measurement-based schemes search for a fresh path and re-verify the topology before every request, placing a network-wide classical exchange on the critical path of each one. We introduce DODAG-X, which removes it. A single destination-oriented directed acyclic graph spanning tree is computed once and reused across all requests, so each party's route is recovered by following parent pointers instead of by a new search. The per-request routing cost drops from O(N) to O(sqrt{N}) on symmetric grids and to O(log N) on small-world networks for N nodes, and only the N-1 tree links need be maintained under link loss. Routing on the sparse tree also shrinks the neighborhoods cleared to isolate the parties, lowering measurements per request by roughly 19% on small-world graphs and up to 34% on moderately dense, strongly rewired ones; on a fixed tree the two protocols use identical counts. We prove correctness for up to three parties with no restriction on topology, and prove a sufficient condition under which one application yields an n-party GHZ state for any n. We then delimit it, exhibiting requests outside the hypothesis whose output is multipartite entangled yet in a different local-Clifford class. Under a discrete-time Markov failure model the classical repair layer matches the reachability of full-graph re-search up to a failed-edge fraction of one half, and a coherence criterion relating tree depth to memory lifetime identifies the viable hardware platforms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2408.07118) | 2026-08-17
