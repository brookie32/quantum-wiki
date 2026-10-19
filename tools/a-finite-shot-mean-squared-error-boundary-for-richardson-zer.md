---
title: "A finite-shot mean-squared-error boundary for Richardson zero-noise extrapolation"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.08251"
summary: "arXiv:2605.08251v2 Announce Type: replace Abstract: Zero-noise extrapolation (ZNE) reduces the bias of noisy quantum-circuit measurements, but Richardson coefficients and shot splitting increase their"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2605.08251v2 Announce Type: replace Abstract: Zero-noise extrapolation (ZNE) reduces the bias of noisy quantum-circuit measurements, but Richardson coefficients and shot splitting increase their statistical error. This paper determines the noise strength at which Richardson ZNE starts to lower the mean-squared error relative to the unmitigated estimator at a fixed shot budget B. The boundary is set by the balance between the leading squared-bias improvement and the leading excess-variance penalty: depending on the variance exponent of the measurement, it shrinks with B, becomes a budget threshold, or disappears. For fixed Richardson extrapolation with linear leading bias, the Richardson order and the shot allocation change only constants; the boundary exponent is set by the measured observable and protocol. Deterministic stabilizer measurements and nonzero-variance Hamiltonian or variational-energy measurements have boundaries that shrink as B^{-1} and B^{-1/2}, and for finite-outcome shot measurements these two classes are the only ones. Qiskit Aer simulations of Greenberger-Horne-Zeilinger (GHZ) and quantum approximate optimization algorithm (QAOA) circuits reproduce this separation, and on IBM Quantum hardware ZNE lowers the mean-squared error at equal budget in 75 of 101 instances.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.08251) | 2026-10-19
