---
title: "QTUNER: A Feature-Guided Adaptive Framework for Quantum-Compiler Optimization Pass Tuning"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.04586"
summary: "arXiv:2607.04586v2 Announce Type: replace Abstract: Quantum compiler optimization is important for improving the execution fidelity of quantum circuits. In practice, this optimization is often formula"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2607.04586v2 Announce Type: replace Abstract: Quantum compiler optimization is important for improving the execution fidelity of quantum circuits. In practice, this optimization is often formulated as reducing circuit-level metrics. In classical compilers, pass tuning has been well-established through various methods. However, these methods cannot be directly applied to quantum compilers, because quantum programs exhibit quantum-specific features. Existing quantum compiler tuning studies have attempted to incorporate quantum circuit features with compiler tuning techniques, but they still suffer from two key limitations. First, they tune only a limited subset of optimization passes, leaving the global effectiveness of the full optimization pass space underexplored. Second, the quantum features they use are mainly static features, such as structure and DAG features, which are not directly tied to the optimization characteristics of quantum circuits. In this paper, we propose QTuner, a feature-guided framework for quantum compiler pass tuning. We first construct an optimization dataset by performing Bayesian Optimization and recording their optimized pass sequences. Based on this dataset, QTuner represents each circuit with two types of features: static circuit features and optimization-aware pass embeddings. Finally, QTuner trains two models offline, which are used to efficiently retrieve and rank promising pass sequences for a new circuit. We evaluate QTuner on two benchmarks across Qiskit and PyTKET compilers. On Qiskit, QTuner achieves up to a 10.6-percentage-point improvement in 2Q gate reduction over the strongest baseline while reducing tuning time by 73.59%. On PyTKET, QTuner achieves up to a 9.4-percentage-point improvement in 2Q gate reduction and reduces tuning time by 64.49%. These results demonstrate that QTuner enables efficient pass tuning across quantum compilers.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.04586) | 2026-10-28
