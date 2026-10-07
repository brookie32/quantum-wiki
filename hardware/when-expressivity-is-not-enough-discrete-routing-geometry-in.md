---
title: "When Expressivity Is Not Enough: Discrete Routing Geometry in Variational Quantum Circuits"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.07697"
summary: "arXiv:2610.07697v1 Announce Type: new Abstract: Finding useful variational quantum circuits requires more than representational capacity: training must also have access to directions that improve the "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.07697v1 Announce Type: new Abstract: Finding useful variational quantum circuits requires more than representational capacity: training must also have access to directions that improve the objective. We study how discrete CNOT routing shapes both capacity and local accessibility. For circuits built from CNOT and arbitrary one-qubit gates, we separate binary routing matrices from continuous rotations to relate global capacity to local tangent accessibility. An exact finite-field formula for the operator Schmidt rank of a CNOT block and cumulative multiblock bounds yield capacity constraints and a Bell-pair fidelity obstruction. Locally, routing propagates generators into a routing-dependent tangent space, so all parameter gradients can vanish even when the ambient objective gradient is nonzero; frame bounds distinguish loss of gradient coverage from poor conditioning. A routing-conditioned identity insertion preserves the current unitary, state, loss, and existing gradients while adding new tangent directions. Candidate-only and incremental projection scores provide local criteria for ranking insertions. Exact-statevector tests show strong short-horizon score-descent correlations on controlled Bell tasks and effective equal-cost selection on connected Heisenberg chains up to twelve qubits, with complementary TFIM selector controls. A broader TFIM routing ensemble exhibits routing-dependent near-stagnation. Together, these results connect representational capacity, local accessibility, and same-point repair through a common discrete routing description. An architecture need not remain fixed during training: task-dependent geometric information can guide the opening of new descent directions while preserving the learned circuit at insertion. This provides a concrete local approach to a broader problem: how useful quantum circuits can be discovered from the information a task supplies.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.07697) | 2026-10-07
