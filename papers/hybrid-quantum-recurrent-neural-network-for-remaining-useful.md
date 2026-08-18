---
title: "Hybrid quantum recurrent neural network for remaining useful life prediction of turbofan engines"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2504.20823"
summary: "arXiv:2504.20823v3 Announce Type: replace-cross Abstract: Accurate remaining useful life (RUL) estimation underpins safe operation and cost-effective maintenance of aerospace propulsion systems. We pr"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2504.20823v3 Announce Type: replace-cross Abstract: Accurate remaining useful life (RUL) estimation underpins safe operation and cost-effective maintenance of aerospace propulsion systems. We propose a Hybrid Quantum Recurrent Neural Network (HQRNN) for jet-engine RUL forecasting on the NASA C-MAPSS FD001 benchmark. The HQRNN stacks Quantum Long Short-Term Memory (QLSTM) layers, replacing each LSTM gate's linear transformation with a Quantum Depth-Infused (QDI) circuit; this is followed by classical dense layers. Quantum and hybrid quantum-classical methods for turbofan RUL prediction are still at an early stage. Our study is therefore among the first to evaluate a gate-based QLSTM hybrid at matched parameter counts, comparing it against classical and joint state-of-the-art models on this benchmark and complementing that comparison with a circuit-level analysis of the quantum layer. Encoding the gate signals in a quantum feature space is intended to help the network represent high-frequency degradation patterns with fewer trainable parameters than a matched classical counterpart. The HQRNN improves mean RMSE and mean MAE by about 5% over matched-parameter stacked-LSTM RNNs across 10 random seeds, and attains a test RMSE of 15.46, outperforming Random Forest, CNN, and MLP baselines. ZX calculus, Fisher information, and Fourier analyses indicate that the QDI circuit is compact, trainable, and expressive. Advanced joint deep-learning models still outperform the stand-alone HQRNN, indicating that quantum-enhanced recurrent modules are best deployed as components within composite prognostics pipelines rather than stand-alone predictors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2504.20823) | 2026-08-18
