---
title: "CREST: A Hardware-Aware GNN-Based Framework for High-Fidelity and Robust Superconducting Quantum Compilation"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24886"
summary: "arXiv:2611.24886v1 Announce Type: new Abstract: Quantum compilation on superconducting processors requires selecting a connected execution region whose topology and calibrated properties suit the inpu"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24886v1 Announce Type: new Abstract: Quantum compilation on superconducting processors requires selecting a connected execution region whose topology and calibrated properties suit the input circuit. This choice constrains subsequent routing and influences the noise encountered during execution, yet aggregate hardware-quality metrics alone may not reliably predict the execution fidelity of a given circuit. Calibration updates can also change region suitability and trigger the rebuilding of calibration-dependent resource structures. We present CREST, a graph neural network (GNN)-based framework that evaluates circuit-region compatibility before routing. It encodes gate dependencies and logical-qubit interactions alongside each candidate region's connectivity and current calibration attributes; bidirectional cross-graph attention relates the two representations, while real-device execution outcomes supervise candidate ranking. The trained scorer is reused with updated calibration attributes. Evaluations on 324 circuits from seven datasets on TianYan-176 show that CREST improves mean measurement-distribution fidelity by 19.03% over the strongest baseline and achieves the highest mean fidelity on every dataset. Furthermore, using updated calibration attributes, the same trained model maintains the highest overall mean fidelity across six measurement dates without retraining. With a unified model of circuit-region compatibility, CREST improves execution fidelity across diverse workloads and sustains that advantage as hardware calibration changes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24886) | 2026-11-19
