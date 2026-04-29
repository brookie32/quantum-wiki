---
title: "Use case study: benchmarking quantum breadth-first search for maximum flow problems"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "applications"
tags: [applications, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24962"
summary: "arXiv:2604.24962v1 Announce Type: new Abstract: The maximum flow problem asks to find the largest possible flow from a source to a sink in a capacitated network. It arises frequently in scheduling, pr"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.24962v1 Announce Type: new Abstract: The maximum flow problem asks to find the largest possible flow from a source to a sink in a capacitated network. It arises frequently in scheduling, project selection, and as a core subroutine in broader optimisation tasks. Classically, it can be efficiently solved using Dinic's algorithm, which repeatedly performs breadth-first search (BFS) and blocking flow computations on the graph. As a potential candidate for quantum speedups, these BFS subroutines can be naturally replaced with quantum BFS (qBFS), an instantiation of Grover's search algorithm. In this paper, we evaluate the expected performance of qBFS on standard classical datasets. These instances are too large to be solved directly on current quantum hardware, so we adopt a hybrid benchmarking approach: (i) we run a classical implementation of Dinic's algorithm and isolate the runtime of its BFS subroutines; (ii) we analytically estimate the minimum number of quantum cycles required to implement qBFS, where we use the classically logged data. Our results indicate that achieving a practical quantum advantage for realistic problem sizes would translate to quantum gate operation times surpassing physical limitations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24962) | 2026-04-29
