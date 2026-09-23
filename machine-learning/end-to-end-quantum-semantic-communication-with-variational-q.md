---
title: "End-to-End Quantum Semantic Communication with Variational Quantum Neural Networks"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25044"
summary: "arXiv:2609.25044v1 Announce Type: new Abstract: This paper presents a quantum semantic communication (QSemCom) framework combining quantum machine learning (QML) and semantic communication (SemCom). C"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25044v1 Announce Type: new Abstract: This paper presents a quantum semantic communication (QSemCom) framework combining quantum machine learning (QML) and semantic communication (SemCom). Classical data are compressed into low-dimensional semantic representations, encoded and processed by a variational quantum transmitter, transmitted through a quantum channel, and processed by a trainable quantum receiver for classification. The framework considers a distributed quantum communication scenario in which quantum processing units (QPUs) exchange task-relevant semantic information through quantum links. While the general setting may involve multiple quantum nodes, this work focuses on the fundamental two-node case, with transmitter and receiver QPUs connected through a noisy quantum channel. Using MNIST, the framework is evaluated under ideal, bit-flip, depolarizing, and amplitude-damping channels. A baseline model is first trained over a perfect channel and evaluated under increasing noise without retraining. Receiver-side end-to-end training is then performed at fixed depolarizing-noise levels. The perfect-channel model achieves an accuracy of 0.9556 and an F1-score of 0.9551. Results show channel-dependent performance degradation, while receiver training substantially restores task performance under moderate and high depolarizing noise. Moreover, task recovery does not require reconstruction of the transmitted density matrix, highlighting a distinction between physical-state recovery and semantic-feature recovery. These results demonstrate that a trainable quantum receiver can recover task-relevant semantic information from noise-distorted quantum states and maintain high classification performance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25044) | 2026-09-23
