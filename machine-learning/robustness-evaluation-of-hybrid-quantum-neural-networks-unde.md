---
title: "Robustness Evaluation of Hybrid Quantum Neural Networks under Noise Models via System-Level Error Mitigation"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.17515"
summary: "arXiv:2604.17515v2 Announce Type: replace Abstract: Quantum Neural Networks (QNNs) represent a promising direction within Quantum Machine Learning (QML), yet their realization on noisy intermediate-sc"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2604.17515v2 Announce Type: replace Abstract: Quantum Neural Networks (QNNs) represent a promising direction within Quantum Machine Learning (QML), yet their realization on noisy intermediate-scale quantum (NISQ) devices remains constrained by decoherence, gate imperfections, crosstalk, and readout errors. This study provides a systematic evaluation of noise effects and mitigation strategies in hybrid quantum neural networks (HQNNs). Zero-Noise Extrapolation (ZNE), Digital Dynamical Decoupling (DDD), and Layerwise Richardson Extrapolation (LRE) are integrated into end-to-end QNN training pipelines developed with PennyLane, simulated under Qiskit Aer noise models, and integrated with the Mitiq framework, while Probabilistic Error Cancellation (PEC) is evaluated separately under depolarizing noise due to its computational cost. Experiments conducted on the Iris dataset with five representative noise channels show that the impact of noise and the effect of mitigation are strongly dependent on the noise model and its strength. The model maintains comparatively strong performance under phase-flip and phase-damping noise, while substantial degradation is observed under high depolarizing and amplitude-damping noise. Across the evaluated mitigation methods, the observed benefits remain limited and noise-dependent: ZNE, DDD, and LRE generally follow the same degradation trends as the unmitigated baseline, while PEC shows limited gains only in the low-noise depolarizing regime. These findings highlight the need for context-specific mitigation strategies to improve the robustness of QNNs in practical NISQ settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.17515) | 2026-07-27
