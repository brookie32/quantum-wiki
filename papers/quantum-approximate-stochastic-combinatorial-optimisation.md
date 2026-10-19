---
title: "Quantum approximate stochastic combinatorial optimisation"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.22876"
summary: "arXiv:2610.22876v1 Announce Type: new Abstract: Two-stage stochastic combinatorial optimisation concerns discrete decisions made before all relevant information is known. An initial decision is made; "
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.22876v1 Announce Type: new Abstract: Two-stage stochastic combinatorial optimisation concerns discrete decisions made before all relevant information is known. An initial decision is made; once uncertainty is resolved, it can be adapted to the realised scenario, at a cost. The aim is to find the initial decision that minimises the upfront cost plus the expected cost of optimal adaptation. The first-stage decision problem is often NP-hard, and computing the expected minimum recourse cost can be #P-hard for a single first-stage candidate. We introduce Quantum Approximate Stochastic Combinatorial Optimisation (QASCO), a variational quantum-walk ansatz that coherently incorporates scenario-dependent recourse into its dynamics to search over first-stage decisions without explicitly evaluating expected minimum recourse costs. We demonstrate QASCO for MaxCut with stochastic edge weights, obtain a circuit with polynomial per-layer gate complexity, and study the ansatz via exact state-vector simulation. Across the instances considered, QASCO concentrates amplitude more effectively on stochastic-optimal first-stage decisions than a previously proposed two-stage QAOA construction. We further show that the ansatz can be calibrated using a depth-independent number of parameters and applied to unseen instances without further circuit-parameter optimisation, including joint decision--scenario--recourse spaces spanning more than 2^{32} configurations. Under a query-cost model, comparison with the tested classical heuristics using sample-average approximations of the expected minimum recourse cost shows that QASCO more reliably reaches globally optimal first-stage solutions while requiring fewer cut evaluations. These results show how to incorporate scenario-dependent recourse into the ansatz dynamics, providing a general framework for variational quantum walks in two-stage stochastic combinatorial optimisation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.22876) | 2026-10-19
