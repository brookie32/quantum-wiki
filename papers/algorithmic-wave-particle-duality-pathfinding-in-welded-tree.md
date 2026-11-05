---
title: "Algorithmic Wave-Particle Duality: Pathfinding in Welded Trees is Hard"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05912"
summary: "arXiv:2611.05912v1 Announce Type: new Abstract: In the welded trees problem, an algorithm navigates a randomly labeled graph formed from two binary trees joined at their leaves through a 'weld' of con"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05912v1 Announce Type: new Abstract: In the welded trees problem, an algorithm navigates a randomly labeled graph formed from two binary trees joined at their leaves through a "weld" of connecting edges. A quantum walk can navigate from root to root exponentially faster than any classical algorithm. However, recording its path destroys the constructive interference responsible for the speedup, leaving open whether some quantum algorithm can efficiently find a path between the roots. We prove that, for trees of height n, the quantum query complexity of finding a path between the roots with constant probability is ilde{Theta}(2^{n/3}). This establishes an algorithmic wave-particle duality, adapting the double-slit experiment to the high-complexity regime: interference between many paths lets a quantum algorithm reach the exit efficiently, but finding a single path (the algorithmic analog of the route of a particle) requires exponentially many queries. Furthermore, the bound is tight, matching the cost of a quantum algorithm that finds collisions between paths from each root to the weld. Our proof uses the compressed permutation oracle to track the information about the graph that an algorithm retains and forgets. We show that the compressed database remains close to a space of states that do not record a path between the roots by bounding the error introduced by each compressed oracle query.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05912) | 2026-11-05
