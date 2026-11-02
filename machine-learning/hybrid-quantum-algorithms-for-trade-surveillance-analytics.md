---
title: "Hybrid Quantum Algorithms for Trade Surveillance Analytics"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41874"
summary: "arXiv:2610.41874v1 Announce Type: new Abstract: Anti-money laundering (AML) and trade surveillance remain largely manual: rule-based monitoring raises alerts of which, by estimate, over 95% are false "
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41874v1 Announce Type: new Abstract: Anti-money laundering (AML) and trade surveillance remain largely manual: rule-based monitoring raises alerts of which, by estimate, over 95% are false positives, each reviewed by a human analyst. We benchmark four quantum and hybrid classifiers against classical baselines on a synthetic pump-and-dump detection task: a fidelity-based quantum k-nearest-neighbours classifier (QKNN) with clustering-based routing; a quantum support vector machine (QSVM) on a one-body projected quantum kernel; a 20-qubit quantum neural network (QNN) with a Pauli-ZZ feature map and RealAmplitudes ansatz; and a hybrid quantum neural network (HQNN) in which a small classical network generates every rotation angle of a five-qubit circuit. Baselines are logistic regression, XGBoost, one- and three-hidden-layer neural networks, and classical k-nearest neighbours. All models share one stratified split of 1000 accounts (800 train, 200 test, 20% suspicious) and two 20-feature representations (ANOVA and PCA); QKNN and QSVM are also tested under simulated noise, and the HQNN is run on the ibm_fez processor. The best model is classical XGBoost on ANOVA features, at a suspicious-class F1 of 61.4%. The HQNN is the strongest quantum-hybrid model, at 54.5-57.9% F1 on an ideal simulator and 55.4-59.8% on ibm_fez, ahead of six of eight classical configurations; at a 15% false-positive rate, half its alerts are genuinely suspicious. Versus the QNN (42.0% F1), it raises under half the false alarms at similar recall with a quarter of the qubits. The QKNN reaches 43.5% F1 (44.4% under noise), above classical KNN (35.6%); the QSVM does not exceed 41%. We observe no quantum advantage, but a five-qubit hybrid on today's noisy hardware already matches well-tuned classical models, with room to grow via richer circuits and larger devices. We contribute a like-for-like comparison with classical models on shared data, splits and features.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41874) | 2026-11-02
