---
title: "Fractal dimension predicts quantum kernel collapse in angle-encoded data"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.00475"
summary: "arXiv:2609.00475v2 Announce Type: replace Abstract: Angle-encoded quantum kernels on tabular data collapse when the feature map is wider than the intrinsic dimension of the data. We propose the correl"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2609.00475v2 Announce Type: replace Abstract: Angle-encoded quantum kernels on tabular data collapse when the feature map is wider than the intrinsic dimension of the data. We propose the correlation fractal dimension D2 as an a priori qubit budget: encode D2 coordinates chosen by FD-ASE instead of the PCA-95% width or all E attributes. On nine data sets and a statevector simulator (n= 32), a one-layer ZZ fidelity kernel at q=D2 stays geometrically alive while the same kernel at the PCA-95% width has already collapsed. The budget is map-dependent: product-state and IQP maps overshoot it; a second ZZ layer undershoots it. Packed dense-angle and re-uploading encodings still live at the fractal q, but not when PCA-95% features are stacked onto those qubits. Shrinking the angle bandwidth moves the ZZ knee later; stretching it kills the kernel earlier. On IBM Quantum (ibm_fez, 256 shots, n=8) the one-layer ZZ kernel at the fractal width matches the exact kernel (MAE 0.021); past that width both hardware and simulator have collapsed. The ceiling is a property of the map-data pair at a stated bandwidth, not of the classical table alone.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.00475) | 2026-10-05
