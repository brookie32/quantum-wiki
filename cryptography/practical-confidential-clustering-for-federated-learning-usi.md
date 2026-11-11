---
title: "Practical Confidential Clustering for Federated Learning using Efficient Secret-Sharing"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2839"
summary: "Federated Learning (FL) often suffers from statistical heterogeneity, where diverging data distributions prevent a single global model from achieving high utility for all participants. Clustered Feder"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Federated Learning (FL) often suffers from statistical heterogeneity, where diverging data distributions prevent a single global model from achieving high utility for all participants. Clustered Federated Learning (CFL) addresses this problem by grouping similar clients to train personalized sub-models, yet performing such clustering while ensuring strict confidentially with minimal communication overhead remains a significant challenge. This paper introduces CCFL, a framework for Confidential Clustering that executes clustering logic, including distance computations and centroid updates, entirely within the encrypted domain using Replicated Secret Sharing (RSS). CCFL orchestrates a unified pipeline that integrates client-side feature extraction, an anonymization server for oblivious shuffling, and Multi-Party Computation (MPC)-based clustering to ensure both input privacy and participant unlinkability. By employing a ring-based Euclidean distance optimization, CCFL significantly reduces interactive rounds, achieving up to 46.7imes computational speedup under realistic LAN and WAN constraints. Our one-shot clustering approach decouples heavy cryptographic computation from the training loop, allowing the system to scale seamlessly to thousands of clients with negligible edge overhead. Finally, downstream evaluations confirm that CCFL achieves a superior privacy-utility trade-off, matching or outperforming state-of-the-art personalized FL paradigms without exposing sensitive feature geometries.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2839) | 2026-11-09
