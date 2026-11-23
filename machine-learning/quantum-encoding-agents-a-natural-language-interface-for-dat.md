---
title: "Quantum Encoding Agents: A Natural Language Interface for Data Embedding Strategy Selection in Quantum Machine Learning"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.31902"
summary: "arXiv:2609.31902v2 Announce Type: replace Abstract: Selecting a data encoding is a central and poorly tooled decision in quantum machine learning. The feature map fixes the geometry of the Hilbert spa"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2609.31902v2 Announce Type: replace Abstract: Selecting a data encoding is a central and poorly tooled decision in quantum machine learning. The feature map fixes the geometry of the Hilbert space, the expressibility of quantum kernels, and whether the circuit can run on near-term hardware. This paper presents Quantum Encoding Agents, an open-source system that turns encoding selection into a natural-language interaction. Given a dataset and an optional task description, it profiles the data, applies a hardware-aware policy using the gate-error threshold p* approximately 10^{-3}, returns a copyable Qiskit circuit with a justification in Portuguese or English, and scores the quantum kernel by Kernel-Target Alignment (KTA). When a numerical matrix is available, it estimates the correlation fractal dimension D_2 and selects original columns with FD-ASE, using q* = max(2, ceil(D_2)) as a qubit budget so that angle and IQP maps are not proposed at a width where the fidelity kernel has collapsed. The service implements seven encoding families: amplitude, angle, dense angle, IQP, basis, data re-uploading, and custom feature map. On benchmark datasets, KTA separates these encodings under realistic NISQ constraints.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.31902) | 2026-11-23
