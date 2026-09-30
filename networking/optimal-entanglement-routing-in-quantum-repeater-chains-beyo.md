---
title: "Optimal Entanglement Routing in Quantum Repeater Chains: Beyond Fixed Operation Order and Purification Schedule"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37206"
summary: "arXiv:2609.37206v1 Announce Type: new Abstract: Entanglement routing establishes entangled pairs between distant nodes of a quantum network by purifying and swapping pairs generated on elementary link"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37206v1 Announce Type: new Abstract: Entanglement routing establishes entangled pairs between distant nodes of a quantum network by purifying and swapping pairs generated on elementary links. Existing methods typically restrict the decision space along two axes: the operation order, often fixed to purify-then-swap (PtS), and the purification schedule of each link, often restricted to pumping. Focusing on linear repeater chains with finite link capacities, we relax both restrictions and study the maximization of the expected end-to-end throughput subject to a fidelity threshold under two quantum-noise models. We develop a unified capacity-aware optimization framework comprising an exact mixed-integer linear program (MILP) under PtS, instantiated with either pumping or general tree purification schedules, and an exact dynamic program (DP) over arbitrary operation orders. Under symmetric Pauli noise, we prove that pumping converges to a fidelity strictly below unity, imposing a capacity-independent feasibility bound and a maximum chain length on every pumping-based PtS method, whereas general tree schedules yield a capacity-dependent bound. We further prove that post-swap purification never increases the throughput, so a free operation order can only increase feasibility. Numerical evaluations confirm the bounds: tree schedules serve over 90% of the requests that pumping cannot at moderate fidelity thresholds; within the pumping class, a free operation order recovers much of this advantage; but once links use tree schedules, the tree-based MILP and the order-exact DP serve identical request sets throughout. Operation order and purification schedule are thus substitutes, with the purification schedule the dominant factor governing feasibility under symmetric Pauli noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37206) | 2026-09-30
