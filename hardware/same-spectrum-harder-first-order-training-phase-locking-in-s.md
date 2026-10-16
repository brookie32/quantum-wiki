---
title: "Same Spectrum, Harder First-Order Training: Phase-Locking in Single- versus Multi-Qubit Re-Uploading Circuits"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21778"
summary: "arXiv:2610.21778v1 Announce Type: new Abstract: Angle-encoded variational quantum circuits implement truncated Fourier series. For one-dimensional inputs, a single-qubit re-uploading (serial) circuit "
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21778v1 Announce Type: new Abstract: Angle-encoded variational quantum circuits implement truncated Fourier series. For one-dimensional inputs, a single-qubit re-uploading (serial) circuit represents every function that a multi-qubit circuit with the same encoding budget E can; we find that this exchange of width for depth is not free in first-order training. Because its state lives on the Bloch sphere, all parameters of the serial circuit move the state, at each input, along one complex direction, which we call phase-locking. We prove that this costs no Fourier direction but leaves no direction to spare: however many parameters it has, the serial circuit has at most 2E+2 tangent directions, one more than its 2E+1 Fourier coefficients need, while a two-qubit control with the same encoding budget and model class generically has at least 6E+6. The cost in training is measured against this control, as the number of runs out of 100 that reach the optimum within a fixed step budget. On an exact loss with flat-spectrum targets the gap grows with E; at E=32 the serial circuit converges in 3, 53 and 83 runs under gradient descent, Adam and Levenberg--Marquardt, the control in 99, 100 and 100. On three real-world series, at matched parameter counts, the serial circuit reaches the least-squares optimum in at most 9 runs under Adam and in 32 to 93 under Levenberg--Marquardt, the control in at least 98 and in all 100; its held-out error is up to about 1.5 times that of the control under Adam, but no larger in the typical run under Levenberg--Marquardt.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21778) | 2026-10-16
