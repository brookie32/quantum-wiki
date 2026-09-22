---
title: "From IceCube to IT-Sphere: A Hybrid Quantum-Classical GNN for Banking IT Root Cause Analysis"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.22822"
summary: "arXiv:2609.22822v1 Announce Type: new Abstract: We present Hybrid Quantum Root Cause Analysis (HQ-RCA), an industrially grounded workflow for root cause analysis in banking IT operations, built on a h"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2609.22822v1 Announce Type: new Abstract: We present Hybrid Quantum Root Cause Analysis (HQ-RCA), an industrially grounded workflow for root cause analysis in banking IT operations, built on a hybrid Quantum Graph Neural Network (QGNN): the classical backbone of DynEdge (the IceCube neutrino-reconstruction GNN, which we call standalone DynEdge), with its classification head replaced by a Variational Quantum Circuit (VQC). On 13 months of anonymised IT data (13k alarm clusters) from a major European bank, the hybrid QGNN matches standalone DynEdge -- the strongest classical baseline -- on F_1, while standalone DynEdge leads the ranking metrics. A readout-sensitivity and layout-robustness study, analysed via Dimensional Expressivity Analysis (DEA), shows that the effective parameter dimensionality (rank) of the quantum observable has no measurable correlation with F_1; we therefore keep the simplest readout langle Z_0rangle (the Pauli-Z expectation on the first qubit), which in the deployed layout is rank-1, collapsing optimisation to a 1-D problem solvable by a gradient-free grid scan. Execution on IBM Heron r2 (no error mitigation) shows this gradient-free readout is executable on NISQ hardware after threshold recalibration.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.22822) | 2026-09-22
