---
title: "Circuit Hypernetworks for Quantum-Augmented Diffusion Language Models"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.24657"
summary: "arXiv:2609.24657v1 Announce Type: new Abstract: Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.24657v1 Announce Type: new Abstract: Language models can be adapted by changing the computations applied to individual tokens. Quantum circuits offer one such approach, but evaluating wider circuits inside a large model can be computationally demanding. Here we introduce HyperQ, which adds token-conditioned quantum residual branches to a frozen masked-diffusion language model. A quantum residual branch is a module in each transformer block that reads a token's hidden state, emits the coordinates of that token's circuit, executes it, and adds the measured values back through a residual connection. The backbone remains frozen, and only the added branches are trained. Within each branch, a lightweight circuit hypernetwork emits token-specific rotation angles, coupling strengths, and measurement axes in a shared sparse circuit structure. The required expectation values have an exact classical expression whose evaluation cost grows linearly with the qubit count, enabling circuits from 16 to 64 qubits to be trained within a 1.1-billion-parameter backbone. Across downstream benchmarks, increasing circuit width raises the average score from 47.65 to 54.30. At 64 qubits, HyperQ exceeds the backbone and its low-rank-adapted counterpart by 4.71 and 3.67 points, respectively. HyperQ is fine-tuned on 20,000 prompt-response pairs, compared with 200,000 for the classical baselines. These findings support token-conditioned circuit emission as a tractable architectural approach to quantum-augmented language modelling.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.24657) | 2026-09-22
