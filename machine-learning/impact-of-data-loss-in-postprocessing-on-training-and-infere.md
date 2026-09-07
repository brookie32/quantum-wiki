---
title: "Impact of Data Loss in Postprocessing on Training and Inference of Quantum Neural Networks"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05060"
summary: "arXiv:2609.05060v1 Announce Type: new Abstract: As quantum hardware scales to larger devices, the classical software layers that interface with it must evolve in step. Postprocessing routines develope"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.05060v1 Announce Type: new Abstract: As quantum hardware scales to larger devices, the classical software layers that interface with it must evolve in step. Postprocessing routines developed and tested primarily in simulator settings can encode assumptions that no longer hold on utility-scale devices, leading to data loss that can be difficult to detect from high-level model outputs alone. We present a case study of exttt{SamplerQNN}, the sampling-based quantum neural network class in the Qiskit Machine Learning library. Here, the postprocessing method applies a filter that assumes measurement bit-strings are in virtual qubit space. On our quantum hardware runs, where bit-strings span over 100 physical qubits, this filter led to the loss of 85 to 99.6% of valid measurement shots, depending on the transpiler's qubit placement. The resulting probability vector is unnormalised, allowing distorted prediction and loss values to propagate through the model without an API-level warning. We demonstrate the impact across five experiments on two IBM backends: for inference, accuracy drops from 0.94 to 0.39 on the same raw measurements; for training, the loss signal is compressed by 22 to 27imes, substantially reducing the sensitivity of the optimiser to the objective landscape. The behaviour arises in all released versions of the library (0.8.4 to 0.9.0). We implemented a layout-based marginalisation fix, merged into the GitHub codebase as Pull Request #1041, that makes exttt{SamplerQNN} postprocessing forward-compatible with current and upcoming hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05060) | 2026-09-07
