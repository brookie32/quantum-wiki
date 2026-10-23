---
title: "ArcTN: Efficient Tensor-Network Contraction Planning for Quantum Circuit Simulation"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31554"
summary: "arXiv:2610.31554v1 Announce Type: new Abstract: Tensor-network simulation of quantum circuits depends on contraction orders with low computational cost and small intermediate tensors, found without ex"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.31554v1 Announce Type: new Abstract: Tensor-network simulation of quantum circuits depends on contraction orders with low computational cost and small intermediate tensors, found without excessive planning time. We present ArcTN, a contraction-order optimization framework with two search presets. Light keeps planning overhead low, and Heavy spends more effort on refinement. Both combine randomized-greedy construction, subtree reconfiguration, and parallel tempering with stage-specific stopping rules. ArcTN also provides Fixed and Dynamic slicing to meet tensor-size limits and executes the returned orders. On the 30 QC32 quantum-circuit networks completed by all eight compared configurations, Light reduces FLOPs by 61.32% and plans 1.62imes faster than Cotengra Auto/CMA-ES, and Heavy reduces FLOPs by 43.83% and plans 7.21imes faster than Cotengra AutoHQ/Optuna. Heavy also needs 11.85% fewer FLOPs than OMECO TreeSA-8 and plans 1.33imes faster. Dynamic slicing meets the size limits in all 90 runs on 18 scalar-output networks and reduces total sliced FLOPs by 31.99% relative to Fixed slicing, at the cost of longer planning. With a common NumPy executor, Heavy has the lowest combined planning and execution time among five configurations on the runs that all of them completed. On 672 networks built from 320 MQT Bench circuits, Heavy obtains the lowest geometric-mean FLOPs on the 142 large networks while planning 3.1imes and 31imes faster than Cotengra AutoHQ and Hyper128.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31554) | 2026-10-23
