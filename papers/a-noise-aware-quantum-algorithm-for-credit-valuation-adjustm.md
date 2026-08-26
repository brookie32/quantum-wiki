---
title: "A Noise-Aware Quantum Algorithm for Credit Valuation Adjustments on Real Quantum Hardware"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.12990"
summary: "arXiv:2607.12990v2 Announce Type: replace Abstract: Credit Valuation Adjustment (CVA) requires repeated risk-neutral expectation estimation, making it a natural test bed for quantum amplitude estimati"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2607.12990v2 Announce Type: replace Abstract: Credit Valuation Adjustment (CVA) requires repeated risk-neutral expectation estimation, making it a natural test bed for quantum amplitude estimation, whose coherent amplification can in principle reduce Monte Carlo sampling cost. Whether this advantage survives realistic financial encoding and noisy hardware remains open. We develop an end-to-end, noise-aware quantum workflow for CVA, covering market calibration, discretisation, oracle construction, hardware execution and error-budget analysis. The model combines a correlated two-asset exposure with discount and default factors, encoded through a QCBM-based joint time-market distribution and controlled payoff rotations. We introduce contrast-aware Bayesian iterative quantum amplitude estimation (CABIQAE), which incorporates experimentally calibrated Grover-contrast loss into Bayesian inference and circuit-depth selection. Hardware-calibrated experiments show that CABIQAE exploits the limited amplification available on current devices more effectively than noise-agnostic alternatives and achieves a much lower classical post-processing runtime than the noise-aware BAE baseline. The analysis further decomposes the total CVA error into statistical, encoding, discretisation and hardware contributions. The full CVA oracle remains limited by circuit depth and discretisation resolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.12990) | 2026-08-26
