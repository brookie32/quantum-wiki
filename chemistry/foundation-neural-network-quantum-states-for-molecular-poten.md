---
title: "Foundation Neural-Network Quantum States for Molecular Potential Energy Surfaces in Second Quantization"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37733"
summary: "arXiv:2609.37733v1 Announce Type: cross Abstract: Second-quantized neural-network quantum states have achieved accurate molecular energies, but extending them across molecular geometries requires a sh"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37733v1 Announce Type: cross Abstract: Second-quantized neural-network quantum states have achieved accurate molecular energies, but extending them across molecular geometries requires a shared representation of the geometry-dependent wavefunction coefficients. We introduce geometry-conditioned foundation neural-network quantum states for molecular electronic structure in second quantization. A single autoregressive model learns a family of ground states from sparse anchor geometries and provides wavefunctions at untrained geometries without further optimization. Orbital alignment matches orbital identities and transports their phases, establishing an aligned orbital basis across geometries. Frozen energies reach chemical accuracy at every untrained query geometry for N_2, CO, and H_4. On additional molecular paths, the energy-trained wavefunctions yield dipoles, quadrupoles, and natural occupations without property labels. Across three paired N_2 training seeds, orbital alignment lowers the mean absolute energy error over all untrained query geometries from 34-37 mHa to 0.049-0.085 mHa. At approximately 1 mHa mean absolute error, frozen evaluation reduces the per-geometry cost by 986imes relative to independent optimization, yielding an estimated 25.8imes end-to-end GPU-cost reduction on a 161-point N_2 grid.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37733) | 2026-09-30
