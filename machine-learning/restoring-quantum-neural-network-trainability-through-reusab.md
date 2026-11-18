---
title: "Restoring quantum neural network trainability through reusable calibration"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.21748"
summary: "arXiv:2611.21748v1 Announce Type: new Abstract: Quantum neural networks (QNNs) rely on measured quantum observables to guide optimization, but hardware noise can suppress the parameter-dependent signa"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.21748v1 Announce Type: new Abstract: Quantum neural networks (QNNs) rely on measured quantum observables to guide optimization, but hardware noise can suppress the parameter-dependent signals essential for learning. Here, we develop a structure-preserving error-mitigation framework that improves QNN trainability through reusable calibration of the quantum circuit's effective noise response. By calibrating a reference circuit with the same gate architecture as the trainable circuit, we construct regularized estimators of local quantum features that remain fixed throughout training. We quantify how calibration errors and response mismatches affect the recovery of both observables and their derivatives. Numerical simulations demonstrate enhanced loss-landscape contrast, faster convergence, and improved classification performance, and an IBM Quantum experiment confirms improved closed-loop variational optimization under hardware noise. We further demonstrate calibration reuse in a modular QNN comprising 25 independent four-qubit channels, corresponding to 100 qubits in aggregate. Our results establish reusable feature calibration as a practical approach to improving noise-limited quantum machine learning without repeated calibration at every training step.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.21748) | 2026-11-18
