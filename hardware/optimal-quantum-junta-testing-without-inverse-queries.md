---
title: "Optimal Quantum Junta Testing without Inverse Queries"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37926"
summary: "arXiv:2609.37926v1 Announce Type: new Abstract: We study the query complexity of testing quantum juntas. Given an unknown n-qubit unitary or quantum channel, the goal is to decide whether it acts nont"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37926v1 Announce Type: new Abstract: We study the query complexity of testing quantum juntas. Given an unknown n-qubit unitary or quantum channel, the goal is to decide whether it acts nontrivially on at most k qubits or is arepsilon-far from every such operation. For unitaries, we consider the forward-only model, where the tester has access to U, but not to U^agger or controlled-U. We give tight bounds for both unitary and channel junta testing. For sufficiently large k, n ge 2k, and a broad range of arepsilon, both problems have query complexity Thetaleft(k/(arepsilon^2log k)right). Our upper bounds are achieved by simple nonadaptive testers using product inputs and single-qubit measurements. For junta channels, this closes the gap by Bao and Yao (COLT 23, TPAMI 2025) between an widetilde{O}(k) upper bound and a widetilde{Omega}(sqrt{k}) lower bound at constant arepsilon, establishing the optimal Theta(k/log k) query complexity. At the heart of both bounds is a strong connection between quantum junta testing and classical support-size testing. For the upper bounds, we reduce quantum junta testing to a generalized support-size problem for distributions over random subsets, and develop a new tester with improved sample complexity. For the lower bounds, we proceed in the reverse direction, reducing classical support-size testing to quantum junta testing through a phase-masked hard ensemble and showing that forward quantum queries can be exactly classicalized on average. Together, these reductions identify support-size testing as the classical core of quantum junta testing and yield matching lower bounds. At constant arepsilon, they also give a separation between Theta(k/log k) forward queries and widetilde{O}(sqrt{k}) queries with inverse access.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37926) | 2026-09-30
