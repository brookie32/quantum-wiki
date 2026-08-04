---
title: "Cooperative Platoon Routing and Dispatching via Edge-Assisted Hybrid Quantum Optimization"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00524"
summary: "arXiv:2608.00524v1 Announce Type: new Abstract: Cooperative platooning can reduce the energy use of Connected and Autonomous Vehicle (CAV) fleets, but the routing problem becomes difficult when vehicl"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00524v1 Announce Type: new Abstract: Cooperative platooning can reduce the energy use of Connected and Autonomous Vehicle (CAV) fleets, but the routing problem becomes difficult when vehicles must meet on the same road segments at compatible times while moving through unstable urban traffic. This paper develops an edge-assisted, closed-loop evaluation pipeline for platooning-aware vehicle routing. Roadside Units estimate local traffic kinematics from video, classify segment-level flow stability, and activate platooning rewards only on road segments where close-gap coordination is physically appropriate. The resulting multi-vehicle routing problem is written directly as a Quadratic Unconstrained Binary Optimization (QUBO) model, so pairwise platooning interactions are represented as native quadratic Ising terms instead of requiring auxiliary MILP linearization variables. We evaluate the framework using a 24-hour microscopic SUMO simulation of Troy, NY, together with localized IBM Quantum hardware benchmarks. The SUMO study shows an 18.5% reduction in fleet tractive-energy demand relative to a non-cooperative baseline. On 25-active-qubit benchmark instances executed on exttt{ibm_boston}, Linear-Chain QAOA reduces two-qubit CNOT depth by 66.7% compared with dense QAOA and samples the exact classical ground state with P_{ext{feas}} = 38.6% and P_{ext{opt}} = 14.2% at p=2. These results suggest that edge perception and shallow quantum optimization can work together as a useful component of closed-loop CAV platoon dispatching.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00524) | 2026-08-04
