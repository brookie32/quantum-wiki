---
title: "Simulating two-Dimensional decaying vortex structure with the Carleman-Lattice-Boltzmann method"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41653"
summary: "arXiv:2610.41653v1 Announce Type: new Abstract: We perform a numerical study of the free decay of two-dimensional nonlinear vortex structures using the second-order-truncated Carleman-Lattice Boltzman"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41653v1 Announce Type: new Abstract: We perform a numerical study of the free decay of two-dimensional nonlinear vortex structures using the second-order-truncated Carleman-Lattice Boltzmann method (CLB2). To this purpose, we simulate the nonlinear vortex system on a 128imes128 grid at two initial Reynolds numbers, Reapprox15 and Reapprox46, by resorting to a highly-tuned multi-GPU implementation of the CLB2 code. At Re approx 15, CLB2 shows significant accuracy all along the decay process, up to six diffusive times (corresponding to 950 time steps), with structure-preserving errors below 10% in amplitude, where by structure-preserving we imply that such errors can be almost entirely reabsorbed by a global time-dependent rescaling factor. At Re approx 46, the evolution is carried out over 2850 time steps, also corresponding to six diffusive times. In this scenario, however, the errors grow in time well above 10% in amplitude with a still relatively modest but appreciable effect on the spatial structure of the flow. These results indicate that CLB2 is capable of preserving the nonlinear evolution of coherent structures over sufficiently long time spans to reach an effective zero steady-state. However CLB2 shows a constant sub-dissipative trend (more energy than the corresponding Lattice Boltzmann configurations) with a deteriorating accuracy at increasing time and Reynolds number. The present results shed hope that further developments, such as suitable closures instead of truncation and/or various forms of regularization, may lead to a significant improvement of the CLB2 accuracy, prior or even without escalating to expensive higher-order truncations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41653) | 2026-11-02
