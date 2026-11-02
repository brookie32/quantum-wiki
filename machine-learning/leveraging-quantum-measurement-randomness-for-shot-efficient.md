---
title: "Leveraging Quantum Measurement Randomness for Shot-Efficient Diffusion Models"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41721"
summary: "arXiv:2610.41721v1 Announce Type: new Abstract: In quantum computing, the readout always carries finite-shot sampling noise. Suppressing this noise through repeated measurements raises the cost of a q"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41721v1 Announce Type: new Abstract: In quantum computing, the readout always carries finite-shot sampling noise. Suppressing this noise through repeated measurements raises the cost of a quantum neural network (QNN). Meanwhile, a stochastic diffusion sampler deliberately adds randomness at each reverse (generation) step. This paper turns the measurement noise from a liability into a resource. Specifically, we use the noise quantum measurement produces anyway to replace part of the noise the sampler would otherwise inject. We characterize the measurement error as multinomial sampling noise propagated through a trainable linear readout. To connect the circuit's Born probabilities to the denoising task, we further formulate the diffusion process on a bounded zero-sum hyperplane mapped to the probability simplex. Therefore, we can employ a compensation noise to match the mean and covariance of the shot-noise-free linear update under some minimum shot conditions. Solving this condition for the shot count gives a state-dependent adaptive budget. For the denoising diffusion implicit model (DDIM), this budget increases as the sampler becomes more deterministic. On an eight-dimensional Gaussian mixture, the schedule achieves comparable generation quality with 303 shots per sample against a high-shot reference of 1.6imes10^{6}, about 5300imes fewer. Latent diffusion experiments on MNIST further validate the proposed mechanism for generation in a learned latent space.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41721) | 2026-11-02
