---
title: "Photonic Quantum Computing vs. Classical Solvers in Constrained Factor Portfolio Optimization"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14134"
summary: "arXiv:2608.14134v1 Announce Type: new Abstract: The authors present a rigorous empirical evaluation of three distinct optimization paradigms for institutional factor portfolio construction: an entropy"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14134v1 Announce Type: new Abstract: The authors present a rigorous empirical evaluation of three distinct optimization paradigms for institutional factor portfolio construction: an entropy-based photonic quantum annealer (Dirac-3, Quantum Computing Inc.), a commercial mixed-integer programming solver (Gurobi), and a model-free deep reinforcement learning agent (SAC). Evaluating these pipelines on the Jensen-Kelly-Pedersen 13-factor equity library across 164 months test window, we implement a full factorial penalty sweep comprising 48 hyperparameter configurations that govern return, volatility, and skewness trade-offs. Our findings demonstrate that while photonic hardware can locate superior risk-return topologies within a narrow operating range, classical mixed-integer programming remains superior for risk-constrained mandates requiring tight tail-risk control and cross-seed stability. Furthermore, we document structural failure modes in reinforcement learning factor allocators under unanchored higher-moment shaping. We translate these empirical results into actionable, mandate-specific guidelines for quantitative portfolio managers deploying advanced optimization engines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14134) | 2026-08-17
