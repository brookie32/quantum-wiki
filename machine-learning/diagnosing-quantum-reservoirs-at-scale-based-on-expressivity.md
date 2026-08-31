---
title: "Diagnosing quantum reservoirs at scale based on expressivity and coverage"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09445"
summary: "arXiv:2607.09445v2 Announce Type: replace Abstract: Quantum reservoirs offer a hardware-friendly route to quantum machine learning, replacing trainable circuits with fixed random dynamics and a classi"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2607.09445v2 Announce Type: replace Abstract: Quantum reservoirs offer a hardware-friendly route to quantum machine learning, replacing trainable circuits with fixed random dynamics and a classical readout. Because the reservoir is not optimized, performance depends entirely on the choice of reservoir family, yet existing diagnostics demand resources that grow exponentially with system size. We introduce a scalable, hardware-agnostic framework built on two complementary quantities. The first is a task-independent order-statistics (ORS) expressivity score, which compares only the largest output probabilities of a reservoir ensemble against an analytical Haar baseline. It never reconstructs the full output distribution, is cost-independent of Hilbert-space dimension, and admits a closed-form depolarizing noise correction, making it directly usable on hardware. The second is the task-dependent effective rank R_{eff} of the feature matrix, which measures how much input-dependent information reaches the readout. We validate the ORS score against established complexity diagnostics and confirm it remains informative under simulated noise and on IBM quantum hardware. Across synthetic and real quantum extreme learning machine and quantum reservoir computing benchmarks, ORS captures the intrinsic expressivity hierarchy of reservoir families while R_{eff} determines when that expressivity becomes usable predictive information.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09445) | 2026-08-31
