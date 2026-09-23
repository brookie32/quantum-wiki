---
title: "Lattice Lindbladian simulation by patching and merging"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26372"
summary: "arXiv:2609.26372v1 Announce Type: new Abstract: Simulating the dynamics of dissipative quantum many-body systems governed by local Lindbladians is a fundamental task in quantum computation. While the "
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.26372v1 Announce Type: new Abstract: Simulating the dynamics of dissipative quantum many-body systems governed by local Lindbladians is a fundamental task in quantum computation. While the near-optimal gate count has been achieved for Hamiltonian simulation, comparable results for Lindbladian simulation remain elusive. In this work, we develop quantum algorithms for lattice Lindbladians by exploiting their locality. First, we consider sparsely dissipative systems, in which the dissipation is sparsely located, including boundary-driven systems. We establish a near-optimal quantum algorithm for their dynamics with gate count O(Nt , polylog(Nt/arepsilon)), where N is the system size, t is the evolution time, and arepsilon is the allowable error. We then consider generic lattice Lindbladians with finite-range interactions and dissipation, and develop an algorithm for simulating time-evolved observables with gate count O((Nt)^{4/3} , polylog(Nt/arepsilon)) per sample with the sampling complexity Theta(arepsilon^{-2}). The gate count has the smallest known dependence on the system size among algorithms retaining polylogarithmic dependence on 1/arepsilon. Our algorithms are based on two techniques that exploit locality: patching and merging. Patching decomposes dissipative dynamics into dynamics on subsystems with exponentially small error, generalizing a key idea underlying the Haah-Hastings-Kothari-Low algorithm for near-optimal Hamiltonian simulation. Merging absorbs reversed dissipative dynamics into other parts of the evolution, substantially reducing the overhead associated with quasi-probabilistic sampling. These results demonstrate that locality can be fully exploited to achieve fast quantum simulation of dissipative many-body dynamics, opening the way to applications such as predicting nonequilibrium phenomena and preparing desirable quantum states.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26372) | 2026-09-23
