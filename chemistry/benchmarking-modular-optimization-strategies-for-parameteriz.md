---
title: "Benchmarking Modular Optimization Strategies for Parameterized Quantum Circuits"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10254"
summary: "arXiv:2610.10254v1 Announce Type: new Abstract: Training parameterized quantum circuits requires balancing optimization progress with limited evaluation budgets and the statistical uncertainty of near"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10254v1 Announce Type: new Abstract: Training parameterized quantum circuits requires balancing optimization progress with limited evaluation budgets and the statistical uncertainty of near-term quantum hardware. We present a modular benchmarking framework that separates quantum search-direction estimation from classical parameter-update rules, allowing their interactions and sensitivities to be examined independently. We evaluate a suite of gradient-based, stochastic, and derivative-free optimizers across combinatorial optimization using the Quantum Approximate Optimization Algorithm (QAOA), supervised quantum machine learning using Iris classification and a quantum convolutional neural network (QCNN) for binary MNIST classification, and quantum chemistry using the variational quantum eigensolver (VQE) for molecular hydrogen. By separating objective evaluations from sample-circuit costs under finite-shot simulation and physical execution on a 156-qubit processor, we compare optimizer behavior across workloads with different parameter counts and measurement requirements. Four selected simulator and hardware case studies report terminal and best observed objectives separately, alongside post-training classifier accuracies. The comparisons include selected MaxCut and hydrogen trajectories and illustrate workload-dependent objective changes and evaluation costs, while the simulator benchmark compares both peak and mean performance across three seeds. The hardware runs do not establish an optimizer ranking or isolate a causal effect of device noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10254) | 2026-10-08
