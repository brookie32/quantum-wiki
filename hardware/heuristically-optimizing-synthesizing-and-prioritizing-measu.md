---
title: "Heuristically optimizing, synthesizing, and prioritizing measurement settings for quantum state tomography"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02633"
summary: "arXiv:2609.02633v1 Announce Type: new Abstract: A key task in many quantum-computing applications, e.g., quantum simulation and quantum state tomography (QST), is to partition an arbitrary set of oper"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02633v1 Announce Type: new Abstract: A key task in many quantum-computing applications, e.g., quantum simulation and quantum state tomography (QST), is to partition an arbitrary set of operators into mutually commuting subsets for efficient measurements. However, brute-force approaches to this task quickly become intractable as the number and dimensionality of operators grow. Here, we reformulate operator partitioning as a graph-coloring (GC) problem and develop an efficient computational framework to solve it, balancing accuracy and efficiency. Our framework enables leveraging a range of GC algorithms, which we benchmark for operator partitioning. Then, we demonstrate their utility in optimizing QST experiments, where determining non-overlapping data acquisition settings for QST is a major challenge, and prioritizing among these settings, i.e., selecting the experiments that provide the most information. We further show how to perform these experiments by synthesizing Clifford circuits for joint measurement of commuting Pauli operators in multi-qubit systems. We validate our framework across multi-qubit (up to five qubits), multi-qutrit (up to three qutrits), and hybrid qubit-qutrit systems. Our results show that heuristic GC methods substantially reduce the number of required measurement settings for QST and enable priority-based scheduling that maximizes the information gain per experiment. The optimization converges within minutes on a student-grade laptop, providing speedups of several orders of magnitude over brute-force methods already for these relatively small quantum systems. This demonstrates the potential of GC heuristics as a scalable and practical tool for characterization of noisy intermediate-scale quantum devices. We have made the Python implementation of our GC framework to optimize and schedule QST experiments publicly available at https://github.com/ssm8015/QST_GT.git.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02633) | 2026-09-03
