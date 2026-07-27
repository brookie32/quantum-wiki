---
title: "Absent, Not Faint: Fisher-Information Limits and a Logarithmic Measurement-Design Cure for Passive Characterization of Coherent Qubit Noise"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.21663"
summary: "arXiv:2607.21663v1 Announce Type: new Abstract: Calibrating a quantum processor means estimating error parameters, and estimation theory usually assumes a parameter hard to estimate is faint: its sign"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.21663v1 Announce Type: new Abstract: Calibrating a quantum processor means estimating error parameters, and estimation theory usually assumes a parameter hard to estimate is faint: its signal is weak but present, so more repetitions or a richer model will recover it. This assumption fails for a leading hardware fault. A coherent over-rotation is a small systematic gate miscalibration. Measured through the cheapest data a device returns--one fixed-basis histogram--it is not faint but absent: to first order it leaves the distribution unchanged, indistinguishable from a compensating stochastic error, exactly as two numbers cannot be separated from their sum. For commuting single- and two-qubit transverse over-rotations, with known support on the canonical input, the histogram's Fisher information is singular along the fault's direction at zero angle, its Cramer-Rao bound is infinite, and no finite-variance, locally unbiased estimator recovers it. At a generic nonzero angle the degeneracy partly lifts; beyond four qubits it clears entirely, leaving conditioning, not absence, as the obstruction. The cure is a richer measurement, not a richer model: a fixed, logarithmically small set of extra settings makes every such fault visible. Visibility alone is not enough. The sampling cost is set by conditioning, not coverage, through a floor whose complete-family closed form is exponentially small in the qubit count. We prove the impossibility and cure, confirm both in exact simulation, show conditioning predicts recovery error across hundreds of designs, and observe a 3-5x bias gap on IBM Heron hardware as a consistency check. Non-commuting faults and unknown support remain open.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.21663) | 2026-07-27
