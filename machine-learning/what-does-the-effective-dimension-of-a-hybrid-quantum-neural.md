---
title: "What Does the Effective Dimension of a Hybrid Quantum Neural Network Actually Measure?"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.14070"
summary: "arXiv:2610.14070v2 Announce Type: replace Abstract: Hybrid quantum neural networks (QNNs) pass features from a classical backbone into a variational quantum circuit, and many studies log a scalar call"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2610.14070v2 Announce Type: replace Abstract: Hybrid quantum neural networks (QNNs) pass features from a classical backbone into a variational quantum circuit, and many studies log a scalar called the effective dimension as a sign of capacity or model quality. The effective dimension is usually defined as the participation ratio (PR) of the quantum Fisher information matrix (QFIM), but studies in practice log a PR of cheap parameter sensitivities instead, and the meaning of that scalar is rarely tested. We show that the logged scalar equals the PR of Pauli-Z output sensitivities, that each sensitivity is at most n times its QFIM diagonal entry on n qubits, and that a PR of the QFIM diagonal overstates the full-matrix PR by an exact factor set by the off-diagonal mass. We then test the scalar on CIFAR-10 and EuroSAT with four frozen backbones, one of them a random projection, over 4 to 16 qubits, 1 to 4 layers, three entangling patterns, and three seeds. At a fixed circuit, CIFAR-10 accuracy spans 23.14% to 86.44% while the scalar stays between 6.63 and 9.13, and its correlation with accuracy changes sign across seeds in 7 of the 14 configurations. Depth raises the share of active parameters from 0.39 to 0.91, near a ceiling we derive, and initial gradient variance falls by a factor of 34.5 from 4 to 16 qubits. Removing entanglement raises accuracy by 5.3 to 8.2 points at the same parameter count. The effective dimension therefore describes circuit geometry rather than model quality, so capacity, trainability, and accuracy each need their own diagnostic.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.14070) | 2026-11-06
