---
title: "Quantum Convolutional Autoencoders for Reconstruction-Based Anomaly Detection"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.02135"
summary: "arXiv:2607.02135v2 Announce Type: replace Abstract: Quantum convolutional neural networks (QCNNs) are increasingly used in quantum machine learning (QML) due to their efficient parameterization and hi"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2607.02135v2 Announce Type: replace Abstract: Quantum convolutional neural networks (QCNNs) are increasingly used in quantum machine learning (QML) due to their efficient parameterization and hierarchical representation of quantum information. Anomaly detection has important applications across many domains, including scientific data analysis. In this work, we adapt a QCNN architecture into a quantum autoencoder (QAE) framework for semi-supervised, reconstruction-based anomaly detection. The models are trained on normal samples to reconstruct feature-extracted and dimensionally reduced time-series data, with reconstruction error used as an anomaly score. We investigate two quantum convolutional autoencoder architectures that differ in their treatment of latent information: a hierarchical architecture in which information remains distributed across the circuit and a bottleneck-based architecture in which information is explicitly compressed and reconstructed using additional decoder qubits. The latent-space size is varied to study its influence on reconstruction and anomaly-detection performance. The approaches are benchmarked against a variational quantum circuit and classical baselines using the Kepler exoplanet dataset and pulsar candidates from the High Time Resolution Universe Survey (HTRU-2). The models are evaluated over ten deterministic optimization seeds at matched four- and eight-component input dimensions and matched latent-space sizes where feasible. Across all available compressed matched configurations, the bottleneck QAE achieves higher ROC AUC than the hierarchical QAE, with all differences remaining significant after Holm correction. The preferred compressed latent-space size depends on the dataset and architecture. The strongest classical autoencoder performs better than both quantum autoencoder families on HTRU-2, while the supervised neural network achieves the strongest overall discrimination on both datasets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.02135) | 2026-11-23
