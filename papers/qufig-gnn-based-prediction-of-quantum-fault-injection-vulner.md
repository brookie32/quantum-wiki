---
title: "QUFIG: GNN-Based Prediction of Quantum Fault Injection Vulnerabilities with Gate-Level Precision"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01777"
summary: "arXiv:2610.01777v1 Announce Type: new Abstract: The growing scale and accessibility of quantum hardware exposed new reliability and security challenges in the quantum computing workflow, such as the r"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01777v1 Announce Type: new Abstract: The growing scale and accessibility of quantum hardware exposed new reliability and security challenges in the quantum computing workflow, such as the run-time fault injection attacks in cloud-based quantum computing platforms. However, existing works fail to identify vulnerabilities with gate-level precision or adapt to run-time environments. In this work, we formulate gate-level fault analysis as a learning-guided prioritization problem under restricted fidelity budgets. The framework uses a circuit-DAG-based GNN backbone to predict the vulnerability score of each gate to each type of injected fault, defined as the impact of the gate-fault pair on circuit fidelity. The gate-fault pairs are then ranked by their vulnerability score. Experiments on QASMbench and HamLib MaxCut show that QUFIG recovers high-impact vulnerable gate-fault pairs with fewer inspections than random and depth-based heuristics. Our results show that QUFIG can reduce the number of gates requiring inspection by 2.9--19.8% while maintaining effective fault identification, allowing quantum circuit designers to identify vulnerabilities and apply targeted defenses more efficiently.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01777) | 2026-10-02
