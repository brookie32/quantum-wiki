---
title: "QPAT: A Universal Quantum Machine Learning Framework for Quantum-Assisted Training and Classical Inference"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33806"
summary: "arXiv:2611.33806v1 Announce Type: new Abstract: Deep learning models often struggle with sharp local optima and overfitting in limited-data regimes, and exhibit limited capacity for capturing high-ord"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33806v1 Announce Type: new Abstract: Deep learning models often struggle with sharp local optima and overfitting in limited-data regimes, and exhibit limited capacity for capturing high-order, complex probability distributions. Quantum Machine Learning (QML) models, by operating in exponentially large Hilbert spaces, can efficiently represent such distributions and provide favorable inductive biases for learning, offering a promising pathway to overcome these limitations. However, their practical deployment in the Noisy Intermediate-Scale Quantum (NISQ) era is severely hindered by gradient coupling, barren plateaus, data-loading bottlenecks, and high inference latency. To bridge classical AI and QML, we propose QPAT (QCBM-Prior-Assisted Training), a universal framework that employs a Quantum Circuit Born Machine (QCBM) as a learnable generative prior to provide a task-aligned structured inductive bias during classical model training. The framework can be seamlessly integrated into any classical backbone, including LSTMs, CNNs, and Transformers. We introduce a decoupled fitness-based scoring mechanism and a stochastic "Drop-Prior" mechanism to implicitly distill quantum structural knowledge into the classical weights during training. Evaluated extensively on six benchmarks spanning time-series forecasting, computer vision, and natural language processing, our framework consistently outperforms purely classical backbones in both predictive performance and stability across random seeds; ablation studies further show that these gains are not reproduced by unstructured random priors or a classically learned generative prior. Remarkably, our approach enables completely classical inference, bypassing quantum latency while preserving quantum-enhanced accuracy, paving a highly practical path for QML deployment.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33806) | 2026-11-26
