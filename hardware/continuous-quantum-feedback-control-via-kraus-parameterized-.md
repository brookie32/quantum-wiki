---
title: "Continuous Quantum Feedback Control via Kraus-Parameterized Belief Reinforcement Learning"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.15715"
summary: "arXiv:2608.15715v1 Announce Type: new Abstract: Quantum feedback control requires acting on noisy continuous measurement records without direct access to the underlying quantum state. We propose Kraus"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.15715v1 Announce Type: new Abstract: Quantum feedback control requires acting on noisy continuous measurement records without direct access to the underlying quantum state. We propose Kraus-Parameterized Belief Reinforcement Learning, a pipeline in which a recurrent encoder, constrained to the Stiefel manifold, produces density-matrix estimates that are guaranteed positive-semidefinite and trace-normalized by construction, embedding quantum state geometry directly into the learning loop. A Proximal Policy Optimization (PPO) actor then maps these physically valid belief states to continuous control actions. On a simulated continuously monitored qubit, the resulting policy achieves stable feedback control, maintaining a measurement-conditioned belief fidelity of approximately 0.77-0.80 and exhibiting substantially lower return variance than a parameter-matched LSTM-history baseline across both nominal and out-of-distribution conditions. Although gains in raw target fidelity are modest, the geometric constraint guarantees a physically valid, interpretable belief representation and yields markedly more stable control under measurement inefficiency and abrupt dynamics switches. These results indicate that physics-informed neural memory is a practical inductive bias for reliable quantum feedback control.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.15715) | 2026-08-18
