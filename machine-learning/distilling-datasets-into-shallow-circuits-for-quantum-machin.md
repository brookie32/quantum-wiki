---
title: "Distilling Datasets into Shallow Circuits for Quantum Machine Learning"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28229"
summary: "arXiv:2609.28229v1 Announce Type: new Abstract: In quantum machine learning, training a quantum model requires each sample to be prepared as a quantum state by a loading circuit that must be re-execut"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28229v1 Announce Type: new Abstract: In quantum machine learning, training a quantum model requires each sample to be prepared as a quantum state by a loading circuit that must be re-executed for every shot at every training step. The total burden therefore scales with both the number of samples and the cost of preparation. Existing approaches reduce the loading cost of individual inputs or distill data and compress their representations before applying a separate quantum encoding. This separation can leave resulting samples costly to prepare or cause additional loss of the information during subsequent compilation into shallow circuits. We propose quantum dataset distillation (QDD), which distills the full dataset directly into a small set of shallow circuits. Each synthetic sample is parameterized as a staircase circuit corresponding to a low-rank tensor network, making the sample and its loading circuit the same object. The circuit parameters are optimized classically with exact gradients using distribution matching under an explicit loading budget, without post-hoc state-preparation synthesis. On MNIST and Fashion-MNIST, only 10 circuits per class (0.0017imes the full dataset size) achieve accuracy comparable to full-data training and outperform selection baselines under matched sample and loading budgets. In finite-shot training, QDD reaches 95% of the full-data accuracy with more than 100imes fewer cumulative shots. Additionally, we validate QDD on real quantum hardware, demonstrating its practical deployment potential.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28229) | 2026-09-24
