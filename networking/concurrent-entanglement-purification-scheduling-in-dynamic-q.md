---
title: "Concurrent Entanglement Purification Scheduling in Dynamic Quantum Networks"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.26900"
summary: "arXiv:2610.26900v1 Announce Type: new Abstract: Quantum networks must deliver end-to-end entanglement whose fidelity meets application requirements, which typically requires entanglement purification "
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.26900v1 Announce Type: new Abstract: Quantum networks must deliver end-to-end entanglement whose fidelity meets application requirements, which typically requires entanglement purification along multi-hop paths. Existing scheduling approaches either purify at the link level or optimize end-to-end fidelity for a static set of requests, and do not capture concurrent requests competing for network resources over time. This paper studies concurrent entanglement purification scheduling in a time-slotted quantum network with heterogeneous links, in which requests compete for link capacity and quantum memories, and each request may be served by multiple parallel paths for increased reliability. We formulate a mixed-integer linear programming (MILP) scheduler that maximizes the number of scheduled requests, with max-min path allocation as a fairness criterion, and develop reinforcement learning (RL) schedulers based on DQN, PPO, and SAC, whose rewards balance request success against Bell-pair consumption. Simulations under varying network load, topologies and target fidelity thresholds show that the RL schedulers achieve the highest success rates, improving on MILP by up to 6% and on Progressive Filling and Greedy heuristics by 16.5% and 19.5% respectively, at the cost of higher Bell pair consumption and the deferral of a small fraction of requests. MILP, in contrast, achieves the highest fairness and the lowest Bell pair consumption in most scenarios.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.26900) | 2026-10-21
