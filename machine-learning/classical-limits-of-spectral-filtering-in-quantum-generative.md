---
title: "Classical Limits of Spectral Filtering in Quantum Generative Models"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14169"
summary: "arXiv:2608.14169v1 Announce Type: new Abstract: Spectral filtering has been proposed as a route to regularization in quantum generative models: the quantum Fourier transform exposes the amplitude spec"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2608.14169v1 Announce Type: new Abstract: Spectral filtering has been proposed as a route to regularization in quantum generative models: the quantum Fourier transform exposes the amplitude spectrum of a quantum circuit Born machine, and a diagonal filter suppresses the high frequencies associated with finite-sample noise, an operation whose classical counterpart seemingly requires manipulating an exponentially long amplitude vector. We examine whether this coherent operation produces anything that classical post-processing of samples from the unfiltered model cannot match. Measuring the filter against convolution with a symmetric probability kernel at matched sampling cost, which accounts for the post-selection overhead of attenuation, we derive necessary and sufficient conditions for the gap between the two to vanish. Magnitude (attenuating) filters obey a dichotomy: at a fixed affordability threshold, the filtered output is either a constant-size Fourier object with an efficient classical sampler, or the passband must widen until no fixed frequency is attenuated and the filter no longer smooths. In neither case does the filter create a quantum-classical separation. Whatever separation survives is inherited from the spectral phase of the input state. Numerical experiments on trained circuit Born machines confirm the classification and show that the deciding phases are invisible to the Born-rule training loss and set by the initialization. Within the diagonal family, pure phase filters remain the only spectral operations exempt from these constraints.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14169) | 2026-08-17
