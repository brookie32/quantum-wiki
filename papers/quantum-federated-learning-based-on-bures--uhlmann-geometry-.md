---
title: "Quantum Federated Learning Based on Bures--Uhlmann Geometry for Heterogeneous Noisy Clients"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.28379"
summary: "arXiv:2608.28379v1 Announce Type: new Abstract: Quantum federated learning enables collaborative model training across quantum devices without sharing raw data, and it faces the data and hardware hete"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.28379v1 Announce Type: new Abstract: Quantum federated learning enables collaborative model training across quantum devices without sharing raw data, and it faces the data and hardware heterogeneity inherent to noisy quantum devices. Utilizing the quantum geometric tensor is a natural remedy, yet pure-state approaches and diagonal approximations discard the correlations that encode parameter incompatibility. To address this, we extend the parameter-space geometry to the mixed states that noisy clients actually prepare. The real part of the resulting mixed-state geometric tensor is the Bures metric, which measures how fast the physical state changes under parameter variation, and the imaginary part is the mean Uhlmann curvature, which quantifies the incompatibility of estimating multiple parameters simultaneously. Accordingly, we employ the Bures metric as a local preconditioner and use the mean Uhlmann curvature to develop an achievable-precision aggregation rule that dynamically down-weights unreliable clients. Furthermore, we establish theoretical guarantees by proving a convergence theorem and a variance-dominance proposition. Empirical evaluations on a trapped-ion quantum emulator demonstrate that the proposed method maintains high accuracy across diverse device-heterogeneity conditions and outperforms standard federated averaging, whose accuracy degrades under strong noise.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.28379) | 2026-08-31
