---
title: "Effective Noise Thresholds for Reliable Quantum Approximation Optimisation Algorithm under Noisy Environment"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.36597"
summary: "arXiv:2610.36597v1 Announce Type: new Abstract: Variational quantum algorithms are leading candidates for practical utilisation on noisy intermediate-scale quantum (NISQ) processors, but accumulating "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36597v1 Announce Type: new Abstract: Variational quantum algorithms are leading candidates for practical utilisation on noisy intermediate-scale quantum (NISQ) processors, but accumulating noise bounds the usefulness of circuit depths. For the quantum approximate optimisation algorithm (QAOA), this trade-off has mostly been addressed by searching for the best depth for a given device. In this work, we consider the inverse question: how much noise each depth can tolerate. Using GPU-accelerated noisy QAOA simulations for MaxCut on three graph families with 6 to 18 vertices, depths up to 10 and three noise channels, we fit the approximation ratios with a generalised logistic surface. We propose the effective noise threshold as the inflection boundary of the logistic surfaces, a noise boundary separating reliable and unreliable QAOA approximation regimes. In general, the threshold decreases as depth rises, indicating that deeper circuits demand for stricter noise requirement for reliable approximation. Its best and worst values over depth divide the noise axis into three regions: every depth remains effective, depth must be chosen with care, or no depth induces effective optimisation. Assessing on the ibm_marrakesh processor, although modelled gate errors understate factual noise, the threshold modeling remains beneficial in informing qualitative depth-dependence structure and identifying dominating noise channel in noisy QAOA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.36597) | 2026-10-28
