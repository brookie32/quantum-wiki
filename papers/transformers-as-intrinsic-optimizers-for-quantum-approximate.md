---
title: "Transformers as Intrinsic Optimizers for Quantum Approximate Optimization Algorithm"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.19392"
summary: "arXiv:2609.19392v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a leading variational framework for combinatorial optimization on noisy intermediate-scale quan"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19392v1 Announce Type: new Abstract: The Quantum Approximate Optimization Algorithm (QAOA) is a leading variational framework for combinatorial optimization on noisy intermediate-scale quantum hardware, but its practical performance depends strongly on the classical optimizer used to train its variational parameters. This outer-loop optimization is often nonconvex, initialization-sensitive, and costly when repeated across large families of related problem instances. In this work, we propose a Transformer-based intrinsic optimization framework for QAOA, in which the optimizer itself is learned and embedded directly into the hybrid quantum-classical loop. The proposed graph-conditioned Transformer processes problem structure, current QAOA parameters, measurement feedback, and recent optimization history to predict the next variational-parameter update, thereby reformulating instance-wise classical optimization as an amortized learned policy. We develop a mathematical formulation of this intrinsic-optimization perspective and evaluate the method on QAOA-based MaxCut benchmarks across multiple problem settings, with comparisons against representative classical and learned optimization baselines. The results demonstrate that Transformer-based intrinsic optimization can provide a structured and transferable mechanism for improving the classical component of hybrid quantum optimization algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.19392) | 2026-09-18
