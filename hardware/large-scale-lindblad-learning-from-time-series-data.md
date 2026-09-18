---
title: "Large-scale Lindblad learning from time-series data"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.08165"
summary: "arXiv:2512.08165v2 Announce Type: replace Abstract: Learned open-quantum-system models have broad applications in device characterization, device calibration, realistic noise model construction, and b"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2512.08165v2 Announce Type: replace Abstract: Learned open-quantum-system models have broad applications in device characterization, device calibration, realistic noise model construction, and bounding observable estimates in quantum simulation. To this end, we develop a highly scalable Lindblad learning protocol assuming an effective time-independent Lindblad generator with local interactions. For a given operation that can be applied repeatedly on a quantum computer, the protocol learns the Lindbladian by forming a linear system of equations for the model parameters in terms of a set of observable values and their gradients. The required gradient information is obtained by fitting time-series data with sums of exponentially damped sinusoids and differentiating those curves. We develop a robust curve-fitting procedure that finds a parsimonious representation of the data up to shot noise. We demonstrate the approach by learning the Lindbladian for a full layer of gates on a 156-qubit superconducting quantum processor, providing the first learning experiment of this kind. We study the effects of state-preparation and measurement errors and limitations on the operations that can be learned. For improved performance under readout errors, we propose an optional fine-tuning strategy that improves the fit between the time-evolved model and the measured data.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.08165) | 2026-09-18
