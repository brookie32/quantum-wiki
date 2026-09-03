---
title: "qSHIFT: An Adaptive Sampling Protocol for Higher-Order Quantum Simulation"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.26263"
summary: "arXiv:2604.26263v3 Announce Type: replace Abstract: Early fault-tolerant quantum computers are expected to support reliable but depth-limited quantum circuits, while classical computational resources "
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2604.26263v3 Announce Type: replace Abstract: Early fault-tolerant quantum computers are expected to support reliable but depth-limited quantum circuits, while classical computational resources remain available. These conditions have motivated hybrid coherent algorithms which use quantum simulation as a central algorithmic primitive. This trend calls for quantum-simulation methods that operate with shallow circuits and admit systematic improvements in gate-complexity scaling. Here, we introduce qSHIFT, an adaptive sampling protocol for simulating a Hamiltonian H=sum_{i=1}^{L}h_iH_i. qSHIFT achieves gate complexity O_rleft((lambda t)^{1+1/r}/arepsilon^{1/r}right), where r is an algorithmic parameter, lambda=sum_i |h_i| and arepsilon denotes the target precision. Relative to qDRIFT, increasing r systematically improves the gate complexity for a given target precision without incurring extra quantum cost. Unlike Trotterization, the number of sampled gates is nominally independent of L. qSHIFT retains the elementary gate set of qDRIFT and, unlike qSWIFT, requires neither ancillary qubits nor controlled operations. The improved gate complexity scaling is obtained at the cost of a classical calculation involving L^r coefficients at each adaptive sampling round.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.26263) | 2026-09-03
