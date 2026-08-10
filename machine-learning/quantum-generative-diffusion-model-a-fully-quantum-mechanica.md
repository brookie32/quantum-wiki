---
title: "Quantum Generative Diffusion Model: A Fully Quantum-Mechanical Model for Generating Quantum State Ensemble"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2401.07039"
summary: "arXiv:2401.07039v5 Announce Type: replace Abstract: Mixed quantum states are the native description of many physically important quantum systems, making their generation a fundamental task in quantum "
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2401.07039v5 Announce Type: replace Abstract: Mixed quantum states are the native description of many physically important quantum systems, making their generation a fundamental task in quantum information processing. However, constructing a diffusion process that generates density operators while keeping every reverse step physically valid remains nontrivial. This work introduces Quantum Generative Diffusion Model (QGDM), a fully quantum-mechanical model whose forward and backward processes are grounded in quantum channel theory. Through a non-unitary forward process, any target quantum state can be transformed into a completely mixed state. A trainable backward process recovers the former from the latter. We introduce partial trace to make the backward process non-unitary, and share parameters across timesteps by incorporating temporal information as an input. We present QGDM's resource-efficient version to reduce auxiliary qubits while preserving generative capabilities. We theoretically analyze the denoising design, showing it avoids a low-loss shortcut that traps training and cause generation failure. Simulations confirm that QGDM outperforms quantum generative adversarial networks on random pure- and mixed-state generation, with better noise robustness than other quantum generative models and a task-specialized approach for practical Gibbs state generation. Hence, QGDM provides a channel-based diffusion framework for learning fixed mixed-state targets, extending quantum generative modeling toward realistic quantum information settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2401.07039) | 2026-08-10
