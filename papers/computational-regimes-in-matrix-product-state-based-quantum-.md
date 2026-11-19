---
title: "Computational regimes in matrix-product-state-based quantum trajectory simulations"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.13779"
summary: "arXiv:2606.13779v2 Announce Type: replace Abstract: Efficient simulation of open quantum systems is central to modeling noisy quantum hardware and many-body dynamics. In trajectory-based tensor networ"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2606.13779v2 Announce Type: replace Abstract: Efficient simulation of open quantum systems is central to modeling noisy quantum hardware and many-body dynamics. In trajectory-based tensor network methods, cost is often associated with trajectory-level quantities such as entanglement growth or bond dimension. However, the total cost of a fixed-accuracy simulation also depends on statistical sampling and on how many trajectories can run in parallel. Here we characterize computational regimes in matrix product state (MPS)-based quantum trajectory simulations by separating memory per trajectory, runtime per trajectory, and sampling effort. Two dimensionless ratios compare the bond dimensions and trajectory counts required by physically equivalent unravelings to reach the same target accuracy. When memory limits parallel execution, a smaller trajectory representation reduces the work per sample and allows more samples to run concurrently. Our scaling model predicts when this additional benefit reverses the preferred unraveling between execution limited by workers and execution limited by memory. Benchmarks across several noise channels illustrate how physical and numerical parameters change the bond dimension and sampling requirements. As an application, a pilot protocol estimates the inputs to this regime classification for a specified problem. These results show how the computational cost of an unraveling depends jointly on trajectory complexity, statistical convergence, and available hardware resources.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.13779) | 2026-11-19
