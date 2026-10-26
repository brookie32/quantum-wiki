---
title: "HQTN-SER: Speech Emotion Recognition with Hybrid Quantum Tensor Networks"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.14523"
summary: "arXiv:2605.14523v2 Announce Type: replace Abstract: Speech emotion recognition (SER) remains fragile in real-world conditions because emotional cues are subtle, speaker-dependent, and easily confounde"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2605.14523v2 Announce Type: replace Abstract: Speech emotion recognition (SER) remains fragile in real-world conditions because emotional cues are subtle, speaker-dependent, and easily confounded by recording variability, while high-performing deep models typically rely on large and carefully curated training sets. Quantum machine learning offers an alternative way to introduce nonlinear correlation modeling with compact modules, yet existing quantum SER studies remain limited, and the impact of circuit structure is not well understood. This paper presents HQTN-SER, a hybrid quantum-classical framework that investigates how quantum tensor network connectivity can support SER under small-qubit settings. HQTN-SER introduces (i) an MPS-inspired quantum tensor network module that enforces structured interactions to model correlations in speech representations with a small number of trainable parameters, and (ii) a fusion strategy that combines quantum measurement features with a learned classical latent embedding for end-to-end emotion classification. We evaluate HQTN-SER on three public benchmarks (RAVDESS, SAVEE, and MDER) under a unified preprocessing and training protocol. The proposed model achieves test accuracies of 80.09% on RAVDESS, 78.12% on SAVEE, and 73.51% on MDER, with corresponding macro-F1 scores of 0.8012, 0.7826, and 0.7351, respectively. The model also exhibits stable convergence while using only three or four qubits, suggesting that MPS-inspired circuit structure can be an effective and hardware-aware design choice for quantum-assisted SER. These results provide a compact experimental baseline for studying structured quantum modules in affective computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.14523) | 2026-10-26
