---
title: "Towards Scaling Quantum Fine-Tuning of Foundational Time Series Models for Classification"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.05408"
summary: "arXiv:2609.05408v1 Announce Type: new Abstract: Time-series foundation models produce rich embeddings, but whether quantum models can exploit them, and how far hybrid classical-quantum architectures s"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.05408v1 Announce Type: new Abstract: Time-series foundation models produce rich embeddings, but whether quantum models can exploit them, and how far hybrid classical-quantum architectures scale, remains unclear. We address this by fine-tuning Chronos for power-grid event classification (PSML-5) with a quantum head on the model's embeddings. Grouping embeddings by physical sensor type before summarization already surpasses the best published baseline built for this benchmark, and with finer-grained features the quantum head outperforms a larger classical multilayer perceptron on identical inputs by 1.7-2.0 percentage points of balanced accuracy. Yet the gains saturate: past a point, feeding more information to the same fixed-width register yields no improvement. We show the bottleneck is neither the supply of information nor circuit expressiveness, but the bandwidth of the data intake. To overcome this limitation, we introduce the wing module, a self-contained few-qubit circuit that feeds additional information into the core circuit through a sparse, one-way coupling. Under a preregistered four-seed protocol, we attach wings to a fixed 12-qubit core with fixed features. Balanced accuracy increases with each added wing, from 83.6% with no wings (13 qubits, including a post-selection qubit) to 85.2% with two (19 qubits). Ablations establish that a circuit enlarged without new information gains nothing, while a wing fed information from the wrong sample harms accuracy. These results reframe scaling for quantum fine-tuning: added qubits help when they carry added inputs, not merely more parameters. Wings offer a modular and stable route to widening that bandwidth.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.05408) | 2026-09-07
