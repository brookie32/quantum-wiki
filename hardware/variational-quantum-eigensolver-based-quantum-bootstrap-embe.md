---
title: "Variational Quantum Eigensolver-Based Quantum Bootstrap Embedding for Molecules"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.17095"
summary: "arXiv:2606.17095v2 Announce Type: replace-cross Abstract: Simulating strongly correlated molecular systems on near-term quantum hardware remains challenging because current hardware offers limited qua"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2606.17095v2 Announce Type: replace-cross Abstract: Simulating strongly correlated molecular systems on near-term quantum hardware remains challenging because current hardware offers limited quantum volume and moderate-fidelity qubits. One way to address this challenge is through bootstrap embedding (BE). Bootstrap embedding partitions molecules into smaller fragments that are then embedded in the ``bath'' of other fragments iteratively. Bootstrap embedding is appealing for quantum simulation because fragmentation reduces the qubit requirements of each fragment problem. In this work, we develop a quantum bootstrap embedding (QBE) workflow that uses variational quantum eigensolver (VQE) fragment solvers and examines the algorithmic choices that determine the success of the overall VQE-QBE procedure. To improve efficiency, we introduce FastAdaptVQE, a sparse-matrix-accelerated form of the adaptive variational quantum eigensolver (ADAPT-VQE) that replaces symbolic commutator evaluation with direct statevector calculations, and MatrixFreeAdaptVQE, a matrix-free extension that removes the sparse-matrix memory bottleneck that arises for larger fragments. We also explore modifying the ADAPT-VQE operator-selection step by replacing the purely greedy choice with a lookahead strategy. Benchmarks on H_4, F_2, and selected geometries of H_6 reach chemical accuracy, within 1 kcal/mol of BE results obtained with a full configuration interaction (FCI) solver. For n-butane, density-matching residuals converged, but energy errors remained outside chemical accuracy. These results show that combining QBE with VQE can accurately compute molecular energies, while density convergence alone does not ensure energy accuracy. This work lays the foundation for extending these energy calculations to larger molecular systems and quantum materials on near-term quantum hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.17095) | 2026-08-18
