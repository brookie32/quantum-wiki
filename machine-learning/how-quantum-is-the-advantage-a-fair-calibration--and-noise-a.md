---
title: "How Quantum Is the Advantage? A Fair, Calibration- and Noise-Aware Benchmark and Attribution Audit of Quantum Machine Learning for Network Intrusion Detection"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18155"
summary: "arXiv:2608.18155v1 Announce Type: new Abstract: Quantum machine learning (QML) for network intrusion detection (NIDS) is routinely reported to reach near-perfect accuracy, yet the most rigorous studie"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18155v1 Announce Type: new Abstract: Quantum machine learning (QML) for network intrusion detection (NIDS) is routinely reported to reach near-perfect accuracy, yet the most rigorous studies find that well-tuned classical models remain competitive, and that apparent quantum gains may be artefacts of classical dimensionality reduction and implicit regularisation rather than genuine quantum effects. We ask not whether a quantum model can post a high accuracy, but how quantum the advantage really is. We present a unified, reproducible QML-IDS benchmark evaluating hybrid variational quantum circuits and quantum-kernel SVMs against five honestly-tuned classical baselines across four standard NIDS datasets (NSL-KDD, UNSW-NB15, CICIDS2017, NF-ToN-IoT-v2) under one leakage-controlled protocol, with an equal-budget feature view, imbalance- and calibration-aware metrics with significance testing, and a simulated NISQ noise sweep. We introduce a quantum-attribution audit (parameter-matched classical controls, a random-feature kernel, and a regularisation sweep) that quantifies how much of any gain is genuinely attributable to the quantum component. Tuned classical models (Random Forest, XGBoost) match or exceed the quantum models on aggregate detection on every dataset, and the audit attributes this to classical preprocessing and regularisation rather than quantum effects. Two advantages survive false-discovery-rate correction: the quantum-kernel SVM out-ranks its direct classical surrogate (a random-feature kernel) on AUPRC and ROC-AUC, and a small four-qubit hybrid out-detects the best classical baseline at the 1% false-positive operating point on the distribution-shifted NSL-KDD task (p = 0.005, BH q = 0.030). Code, seeds, and splits are released; our contribution stands whether quantum wins, ties, or loses.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18155) | 2026-08-20
