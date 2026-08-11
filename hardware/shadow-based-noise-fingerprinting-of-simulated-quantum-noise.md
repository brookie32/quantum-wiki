---
title: "Shadow-Based Noise Fingerprinting of Simulated Quantum Noise Models"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.08998"
summary: "arXiv:2607.08998v3 Announce Type: replace-cross Abstract: Accurate noise classification is essential for operating near-term quantum processors, yet existing approaches, such as quantum process tomogr"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2607.08998v3 Announce Type: replace-cross Abstract: Accurate noise classification is essential for operating near-term quantum processors, yet existing approaches, such as quantum process tomography, scale exponentially with system size, limiting their practicality for routine calibration. We propose a measurement-efficient noise fingerprinting pipeline that combines structured classical shadow tomography with physics-informed feature engineering to identify noise channels from a fixed set of 3-qubit probe circuits. Each sample is represented by a feature vector constructed from randomized Pauli measurements and derived observables designed to resolve physically similar noise channels that produce overlapping signatures under generic measurement sets. We evaluate random forest, extra trees, and a multilayer perceptron on 10,000 labeled samples spanning ten noise models. The three classifiers achieve comparable performance. In the reported runs, random forest and extra trees perform similarly, achieving approximately 0.736 test accuracy and 0.729-0.730 macro F1, compared with 0.715 accuracy and 0.699 macro F1 for the multilayer perceptron. We further analyze the effect of the noise-strength sampling range and conduct a limited sensitivity check using analogous 2- and 4-qubit probes. Confusion analysis shows that readout error, phase flip, thermal relaxation, and bit flip are classified with high reliability, while most remaining errors occur among channels with similar physical effects.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.08998) | 2026-08-11
