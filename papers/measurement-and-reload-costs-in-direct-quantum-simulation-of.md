---
title: "Measurement and reload costs in direct quantum simulation of nonlinear waves"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.21647"
summary: "arXiv:2608.21647v1 Announce Type: new Abstract: Quantum processors encode an N-point field in log_2(N) qubits, which renders nonlinear wave equations an important application for quantum simulation. N"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.21647v1 Announce Type: new Abstract: Quantum processors encode an N-point field in log_2(N) qubits, which renders nonlinear wave equations an important application for quantum simulation. Nonlinear evolution, however, requires the field values themselves, and these are not directly accessible without quantum measurement. Existing algorithms circumvent this measurement through linear embeddings and state copies, thereby obscuring its cost within the truncation order, the auxiliary dimensions, and the state preparation. In order to expose this cost, a hybrid split-step solver is proposed in which the field is measured, updated classically, and reloaded at every step, with all shots and gates accounted for in a single cost-and-error model. Since the entire field is available at every step, a property unavailable to linear approximations in strongly nonlinear regimes, the design of the solver reduces to a budgeting problem over the timestep, the polynomial degree, and the shot count. The coherent kernels of the solver are validated on superconducting hardware. An identical structure and bottleneck govern the viscous Burgers' equation in one and two dimensions. Because every step reads the full field, the quantum cost per step, measured as circuit depth multiplied by measurement shots, exceeds the classical cost with increasing grid size. The framework consequently identifies a coherent, measurement-free nonlinear update as the quantitative target that any end-to-end advantage must meet.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.21647) | 2026-08-25
