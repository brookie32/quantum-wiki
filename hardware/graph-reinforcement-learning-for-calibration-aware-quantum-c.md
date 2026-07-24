---
title: "Graph Reinforcement Learning for Calibration-Aware Quantum Circuit Routing"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.12816"
summary: "arXiv:2606.12816v4 Announce Type: replace Abstract: Quantum circuit routing is a key step in compiling programs for noisy intermediate-scale quantum processors, particularly superconducting devices wh"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2606.12816v4 Announce Type: replace Abstract: Quantum circuit routing is a key step in compiling programs for noisy intermediate-scale quantum processors, particularly superconducting devices whose sparse fixed coupling makes routing a central compilation cost. Routes that appear efficient by standard overhead metrics such as SWAP count, routed two-qubit count, and depth can still lose fidelity when they pass through poorly calibrated couplers. We study a calibration-aware graph reinforcement-learning router that uses same-day calibration data from superconducting IBM Heron r2 processors to choose hardware-edge SWAPs. We train the policy with proximal policy optimization and evaluate it with exact simulated fidelity across nine Munich Quantum Toolkit (MQT) Bench circuits and three calibration snapshots. Across these evaluations, pooled mean exact fidelity is 0.727, compared with 0.440 for SWAP-based bidirectional heuristic search (SABRE)-best20 and 0.481 for target-aware SABRE. We observe that fidelity gains come with higher routed two-qubit counts and are concentrated in 5 qubit and 8 qubit circuit families; under the fixed tree action graph, all 10 qubit families favor SABRE-best20. Overall, our results show that calibration-aware learned routing can improve fidelity beyond gate-count-driven compilation, by roughly 0.25 to 0.29 in absolute mean fidelity over the SABRE-family baselines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.12816) | 2026-07-24
