---
title: "Certification cost of quantum models: measurement correlation, not parameter count"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14424"
summary: "arXiv:2609.14424v1 Announce Type: new Abstract: Reporting the Fisher geometry of a trained variational quantum model is routine; quoting the shot budget that would establish it is not. Certifying an e"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14424v1 Announce Type: new Abstract: Reporting the Fisher geometry of a trained variational quantum model is routine; quoting the shot budget that would establish it is not. Certifying an empirical Fisher matrix to relative Frobenius error arepsilon under coordinate-wise parameter shift costs Theta(B p^{2} V/(arepsilon^{2} G)) circuit executions, where V is the measured readout variance and G the measured squared gradient norm, with uniform allocation optimal in that class. One constant reproduces the cost of two circuit families whose exponents differ by a full power of p. The exponent is an identity in how nV and nG scale with the register, holding family by family to 0.001 across 624 matrix-product-state cells once the finite-p prefactor is removed. The cubic cost is therefore a finite-size window, set by whether the readout light cone grows with the register. A product family to 256 qubits gives 1.966 (95% CI 1.934--1.997); a brickwork entangler falls from 2.853 below ten qubits to 1.715 beyond sixty-four; a blocked entangler gives 1.984 at a fixed cone width against 3.034 at a proportional one. Fixed device connectivity fixes the cone, so a cubic budget from a small simulation overestimates a large machine, on top of hardware multipliers 2.07imes (1.41--3.02), 2.38imes and 1.91imes on ibm_marrakesh, ibm_fez and ibm_kingston. Cost-optimal readout weights cut the measured shot budget by 2.67imes (1.33--4.00) on hardware, flat from four to twelve qubits. A discrepancy model fitted on cheap circuits transfers its mean inside the calibration grid and, at six larger sizes named before the data, does not: nominal 90% intervals cover 36%, and split conformal is the only rung that stays near nominal.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14424) | 2026-09-15
