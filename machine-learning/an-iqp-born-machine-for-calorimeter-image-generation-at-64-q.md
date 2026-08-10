---
title: "An IQP Born Machine for Calorimeter Image Generation at 64 Qubits with Compiled-IQP Deployment"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.27735"
summary: "arXiv:2605.27735v3 Announce Type: replace Abstract: The challenge to scaling quantum generative models on near-term hardware is training. Variational circuit Born machines require repeated quantum sam"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2605.27735v3 Announce Type: replace Abstract: The challenge to scaling quantum generative models on near-term hardware is training. Variational circuit Born machines require repeated quantum sampling and are prone to barren plateaus. Instantaneous Quantum Polynomial-time (IQP) Born machines sidestep both, since their loss is built from low-order Pauli-Z correlators that admit an unbiased classical estimator, while sampling from worst-case circuits in the class is conjectured to be classically hard. We take this train-on-classical, deploy-on-quantum workflow to a real high-energy-physics generative task, learning calorimeter shower profiles at 64 qubits and running the trained model on an IBM Heron r2 superconducting processor at 67 physical qubits. Three ingredients make it work. A uniform mixture of IQP circuits (MoIQP) widens the model class at single-circuit training cost. The Pearson-Stabilized Correlation Kernel (PSCK) biases descent toward the pairwise correlations that carry the shower-development physics, which the standard heat kernel systematically compresses. An exact deferred-measurement compilation collapses the mixture into a single IQP circuit, realized on hardware as a constant-depth dynamic circuit with zero SWAP insertions on the device's native heavy-hex graph. The trained model reconstructs the correlation structure to within 0.016 of the floor imposed by the encoding itself. Raw device samples reproduce the per-cell energy spectra and the full pairwise correlation structure at Pearson r = 0.989, up to a single global amplitude compression of depolarizing origin. A Gaussian copula fitted to the same training split matches the pairwise target more accurately than the quantum model at negligible cost. The contribution is therefore the classical trainability, exact compilation, and hardware deployability of a quantum generative model at this scale, not superiority over classical surrogates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.27735) | 2026-08-10
