---
title: "Predictive Maintenance at the Edge: An Embedded Anomaly Detection Pipeline Trained with Quantum Optimization"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.40848"
summary: "arXiv:2610.40848v1 Announce Type: new Abstract: This article presents a predictive-maintenance pipeline that detects anomalies in bearings from vibration signals, adapted for deployment at the edge on"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.40848v1 Announce Type: new Abstract: This article presents a predictive-maintenance pipeline that detects anomalies in bearings from vibration signals, adapted for deployment at the edge on low-cost microcontrollers, and that uses quantum optimization in two steps of its training. The pipeline consists of a step of vibration feature extraction and a step of classification with a one-class support vector machine (OCSVM). The features are selected by minimum redundancy and maximum relevance (mRMR) with the variational quantum eigensolver (VQE), under a limit on computing time. The OCSVM is adapted for inference at the edge without floating-point operations and is trained by a variational quantum algorithm with Pauli-correlation encoding (PCE). In small-scale tests on a simulator, with the Paderborn bearing dataset, the VQE found the optimal selection in 36% of the runs with Adam, and PCE chose better support vectors than chance, until a classical local search made the two equal. A classical baseline, the usual OCSVM trained by SMO with its weights rounded, matched them without any search.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.40848) | 2026-11-02
