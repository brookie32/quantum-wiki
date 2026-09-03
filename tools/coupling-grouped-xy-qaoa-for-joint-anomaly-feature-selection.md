---
title: "Coupling-Grouped XY-QAOA for Joint Anomaly-Feature Selection"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.13244"
summary: "arXiv:2606.13244v2 Announce Type: replace Abstract: Selecting anomalous samples and explanatory features under fixed cardinalities defines a coupled optimization problem: feature-first selection can o"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2606.13244v2 Announce Type: replace Abstract: Selecting anomalous samples and explanatory features under fixed cardinalities defines a coupled optimization problem: feature-first selection can overlook features whose usefulness depends on the selected samples. In the analyzed model, joint calibration-error sensitivity is sample-count independent, while the sum-column feature-first rule's sensitivity grows linearly. To optimize this formulation, we introduce Coupling-Grouped XY Quantum Approximate Optimization Algorithm (CG-XY-QAOA), with constraint-preserving mixers and block-structured phase angles. On matched sparse IBM Heron R3 circuits, our implementation reduces circuit depth by 35.1%-54.8% against Qiskit's optimization-level 3 preset pass manager on the CZ-basis target and enables runs at 64 decision qubits (p=2) and 36 (p=3). At 20 decision qubits (p=5), fully grouped angles raise the fixed low-energy hit probability 25-fold to 3.7%, with 64.7% of measured samples satisfying both constraints. Benchmarks favor joint selection when feature usefulness varies across anomalies. Noiseless simulations show problem-structured grouping improves over same-depth XY-QAOA and parameter-matched type-preserving randomizations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.13244) | 2026-09-03
