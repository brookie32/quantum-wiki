---
title: "Quantum Causal Discovery via Amplitude Estimation of Kullback-Leibler Divergence"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23451"
summary: "arXiv:2604.23451v1 Announce Type: new Abstract: Causal discovery from observational data underpins applications in finance, climate modeling, and machine learning. Constraint-based causal discovery re"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23451v1 Announce Type: new Abstract: Causal discovery from observational data underpins applications in finance, climate modeling, and machine learning. Constraint-based causal discovery reduces structure learning to a sequence of conditional independence (CI) tests, where each test decides independence by estimating conditional mutual information I(X;Y mid Z) to additive precision au and thresholding against it. Classically this requires Theta(1/au^{2}) samples per test, a cost that dominates in the high-precision regime typical of weak dependencies. We present QKLA (Quantum Kullback--Leibler Amplitude estimation), a quantum algorithm that encodes a clipped log-density ratio as a bounded amplitude and applies amplitude estimation to recover the KL divergence. Given coherent oracle access to the joint distribution, QKLA achieves a quadratic precision improvement, needing only O((L/au)log(1/elta)) queries, where L is the log-ratio clip bound. Embedded in the PC algorithm, this compounds to an widetilde{Omega}(1/(Lau)) reduction in total queries for the full causal discovery procedure. We validate the theory in three experiments. A gate-level state-vector simulation of the full QKLA circuit confirms the predicted O(1/M) error decay. Across K=20 random binary distributions, classical and quantum error scalings match theory to slope accuracy pm 0.005. On two benchmark networks (extsc{Asia}, 8 nodes; extsc{Synthetic-12}, 12 nodes), quantum PC matches classical skeleton-recovery F1 while using 2.5--3.0imes fewer oracle queries at au = 5dot 10^{-3} bits and up to 12imes fewer at au = 10^{-3} bits.



## Related
- [[from-independent-to-joint-enhancing-quantum-phase-and-correl|From Independent to Joint: Enhancing Quantum Phase and Correlation Factor Estimation by Squeezed Reservoir Engineering]]
- [[autoqresearch-llm-guided-closed-loop-policy-search-for-adapt|AutoQResearch: LLM-Guided Closed-Loop Policy Search for Adaptive Variational Quantum Optimization]]
- [[calibrating-the-role-of-entanglement-in-variational-quantum-|Calibrating the Role of Entanglement in Variational Quantum Algorithms from a Geometric Perspective]]
- [[a-novel-hierarchy-of-quantum-kernel-networks-on-smoothed-par|A Novel Hierarchy of Quantum Kernel Networks on Smoothed Particle Hydrodynamics]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23451) | 2026-04-28
