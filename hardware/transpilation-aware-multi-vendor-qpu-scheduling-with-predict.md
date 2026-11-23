---
title: "Transpilation-Aware Multi-Vendor QPU Scheduling with Predicted Post-Transpilation Fidelity"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27927"
summary: "arXiv:2611.27927v1 Announce Type: new Abstract: Cluster schedulers already choose nodes, GPUs and accelerators for submitted workloads, enforce quotas and spread load. QPUs from several vendors are no"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27927v1 Announce Type: new Abstract: Cluster schedulers already choose nodes, GPUs and accelerators for submitted workloads, enforce quotas and spread load. QPUs from several vendors are now schedulable resources in the same clusters, yet the user still names the device, usually the one with the best average fidelity. For a given circuit that choice is often wrong: compiling onto each device's qubit connectivity adds gates, so a job can meet its required success probability on one device and miss it on another with similar error rates, and checking this exactly by compiling for every candidate is too slow for a scheduling decision. We let the scheduler choose the QPU in two stages. A training-free estimate predicts, in milliseconds and without compiling, the success probability on every candidate and filters out those that would miss the requirement; only the chosen device then compiles the circuit, re-checks it, and binds the job or rolls back. The estimate matches compiling every candidate at about 25x lower latency in simulation, ranks measured success on IBM hardware as well as the post-compilation estimate (Spearman rho = 0.95), reduces requirement violations from tens of jobs to a few, and avoids them under contention without piling jobs onto one device. Across vendors it works when error rates are comparable (IBM and IQM) and fails when published figures overstate a device.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27927) | 2026-11-23
