---
title: "Low Latency GNN Accelerator for Quantum Error Correction"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.22149"
summary: "arXiv:2603.22149v2 Announce Type: replace Abstract: Quantum computers have the potential to solve certain complex problems in a much more efficient way than classical computers. Nevertheless, current "
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2603.22149v2 Announce Type: replace Abstract: Quantum computers have the potential to solve certain complex problems in a much more efficient way than classical computers. Nevertheless, current quantum computer implementations are limited by high physical error rates. This issue is addressed by Quantum Error Correction (QEC) codes, which use multiple physical qubits to form a logical qubit to achieve a lower logical error rate, with the surface code being one of the most commonly used. The most time-critical step in this process is interpreting the measurements of the physical qubits to determine which errors have most likely occurred - a task called decoding. Consequently, the main challenge for QEC is to achieve error correction with high accuracy within the tight 1mu s decoding time budget imposed by superconducting qubits. State-of-the-art QEC approaches trade accuracy for latency. In this work, we propose an FPGA accelerator for a Neural Network based decoder as a way to achieve a lower logical error rate than current methods within the tight time constraint, for code distance up to d=7. We achieved this goal by applying different hardware-aware optimizations to a high-accuracy GNN-based decoder. In addition, we propose several accelerator optimizations leading to the FPGA-based decoder achieving a latency smaller than 1mu s, with a lower error rate compared to the state-of-the-art.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.22149) | 2026-04-29
