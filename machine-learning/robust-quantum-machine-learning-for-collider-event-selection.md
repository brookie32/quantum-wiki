---
title: "Robust Quantum Machine Learning for Collider Event Selection under Detector Variability"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11330"
summary: "arXiv:2608.11330v1 Announce Type: new Abstract: Robust machine-learning methods are becoming increasingly important for high-energy physics data analysis as experiments enter the era of higher luminos"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11330v1 Announce Type: new Abstract: Robust machine-learning methods are becoming increasingly important for high-energy physics data analysis as experiments enter the era of higher luminosity and future higher-energy colliders. Detector degradation, changing running conditions and calibration drift can shift data distributions, causing models trained on clean reference samples to degrade after deployment. We investigate whether parameterised quantum models provide a useful inductive bias for robust collider-event selection in two complementary settings. In the unsupervised study, quantum autoencoders trained on background events are compared with classical and variational autoencoders for anomaly detection. In the supervised study, quantum classifiers with data reuploading are trained to distinguish a supersymmetric signal from background and are compared with linear and multilayer-perceptron classifiers. All models are trained under reference conditions and subsequently evaluated under controlled feature-level smearing while their parameters and preprocessing transformations are held fixed. On clean inputs, the quantum autoencoders achieve competitive anomaly-detection performance, including in the low-false-positive-rate regime relevant for triggering, while the deeper data-reuploading classifier attains discrimination comparable to the non-linear classical baseline. Under smearing, the quantum models generally exhibit smaller shifts in their output scores and retain their discrimination more effectively than the expressive classical baselines. These results suggest that parameterised quantum models can provide a useful robustness inductive bias for collider-event selection and motivate further studies with realistic detector systematics, finite-shot statistics and quantum-device noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11330) | 2026-08-13
