---
title: "Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.20801"
summary: "arXiv:2605.20801v2 Announce Type: replace-cross Abstract: Adaptive robot navigation in dynamic environments requires policies that can reach the target reliably while producing efficient and stable tr"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2605.20801v2 Announce Type: replace-cross Abstract: Adaptive robot navigation in dynamic environments requires policies that can reach the target reliably while producing efficient and stable trajectories. This paper presents Q-SpiRL, a quantum spiking reinforcement learning framework for obstacle-aware robot navigation. The framework develops and evaluates five agent families: tabular Q-learning, classical MLP, classical SNN, quantum-enhanced MLP (QMLP), and quantum-enhanced spiking neural network (QSNN). While all models are implemented under a unified training and evaluation pipeline, the QSNN is the central architecture of interest, as it combines spike-based temporal processing with variational quantum feature transformation. Experiments are conducted across three grid-world environments of increasing size, namely 20x20, 30x30, and 40x40, with both static and dynamic obstacles. Performance is assessed using success rate, success-weighted path length, path length, and turn rate under deterministic inference. Results show that QSNN achieves the strongest overall trade-off between task completion, trajectory efficiency, and motion smoothness, reaching up to 99% success rate while maintaining high path efficiency in the most challenging setting. Execution on IBM quantum hardware further demonstrates the feasibility of deploying the proposed hybrid policy under real-device conditions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.20801) | 2026-07-24
