---
title: "ConQUESTA: Topology-Aware Post-Training Structural Pruning of Quantum Neural Networks"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23415"
summary: "arXiv:2610.23415v1 Announce Type: new Abstract: Deploying quantum neural networks (QNNs) on sparse hardware requires preserving task accuracy while reducing compiler-induced two-qubit gates, SWAPs, an"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23415v1 Announce Type: new Abstract: Deploying quantum neural networks (QNNs) on sparse hardware requires preserving task accuracy while reducing compiler-induced two-qubit gates, SWAPs, and depth. We present ConQUESTA (nderline{C}onstrained nderline{Qu}antum nderline{E}ntangler nderline{S}election with nderline{T}opology nderline{A}wareness), a post training pruning framework that combines task saliency with compiler cost, screens candidate entanglers, and searches complete pruning masks under an explicit accuracy constraint. Unlike one-shot ranking, each mask is transpiled as a whole across multiple coupling topologies. Across 4-, 6-, and 8-qubit QNNs and eight model seeds at 55% pruning, ConQUESTA achieves mean resource reductions of 61.6% on Breast Cancer, 72.0% on Digits01, and 82.2% on Iris, exceeding the strongest matched simple baseline by 3.5, 1.7, and 8.9 percentage points, respectively. Fixed-mask recovery raises feasibility from 16/24 to 22/24 runs. In a fixed-k=4 scaling study on a scaling probe of 4 to 12-qubits, the raw mask space grew from 495 to 12.1M while the evaluated masks increase only from 189 to 305. Resource-weight changes alter depth/routing priorities with at most a 0.44-point mean validation shift.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23415) | 2026-10-19
