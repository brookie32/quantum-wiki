---
title: "QSVM-RQNN: Low-Qubit Recurrent Quantum Similarity Learning for Condition Monitoring and Fault Classification"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09652"
summary: "arXiv:2608.09652v1 Announce Type: new Abstract: In the Noisy Intermediate-Scale Quantum (NISQ) era, limited qubit availability and hardware noise constrain the practical deployment of quantum machine "
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09652v1 Announce Type: new Abstract: In the Noisy Intermediate-Scale Quantum (NISQ) era, limited qubit availability and hardware noise constrain the practical deployment of quantum machine learning (QML). Existing quantum neural network (QNN) and quantum convolutional neural network (QCNN) architectures often require increasing quantum resources as the input dimension grows, limiting scalability on near-term devices. We propose QSVM-RQNN, a low-qubit framework integrating centroid-based Quantum Support Vector Machine (QSVM) similarity learning with Recurrent Quantum Neural Networks (RQNNs) for fault classification. The framework reduces the feature space using principal component analysis (PCA), partitions the reduced representation into sequential timesteps, and processes them using a compact three-qubit recurrent quantum architecture with shared parameters. Two complementary variants are developed: QSVM-RQNN-V1 performs class-conditioned joint quantum encoding of input and centroid segments, whereas QSVM-RQNN-V2 performs recurrent learning over timestep-wise quantum similarity representations. Experimental evaluation on multiple fault diagnosis datasets shows competitive and, in several cases, state-of-the-art performance compared with QSVM, QNN, QCNN, QSVM-QNN, QSVM-QCNN, and RQNN models. The proposed architectures provide favorable performance-efficiency trade-offs, improved recall, and enhanced fault detection on highly imbalanced datasets. These results demonstrate that integrating centroid-based quantum similarity learning with low-qubit recurrent representation learning provides an effective and scalable approach to condition monitoring and fault classification on resource-constrained NISQ devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09652) | 2026-08-11
