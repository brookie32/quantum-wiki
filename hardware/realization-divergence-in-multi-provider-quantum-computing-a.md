---
title: "Realization Divergence in Multi-Provider Quantum Computing: A Pre-Registered Study of What Survives Measurement"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.21714"
summary: "arXiv:2610.21714v1 Announce Type: cross Abstract: Quantum programs pass through compilers, transpilers and vendor services before execution. However, the distance between what was written and what run"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.21714v1 Announce Type: cross Abstract: Quantum programs pass through compilers, transpilers and vendor services before execution. However, the distance between what was written and what runs is rarely measured. We call this distance realization divergence: the observable difference in how an identical source circuit is realized and behaves across quantum software stacks. We report a hardware study across three vendors and four devices, combining pre-registered predictions with explicitly identified exploratory analyses and amendments. In a compilation experiment with assigned placement policies, embedding radius correlates with two-qubit overhead at Spearman 0.805, against 0.492 for circuit size. Under a fixed lowest-index policy, an eight-qubit Bernstein-Vazirani circuit exhibits greater execution divergence than a twelve-qubit circuit on IQM Emerald. The opposite ordering occurs on IQM Garnet. Both comparisons replicate across two repetitions with disjoint confidence intervals. These results support a placement-dependent explanation, without isolating individual hardware noise mechanisms. The same ordering inversion is absent on the all-to-all IonQ control. On Rigetti Cepheus, a follow-up using topology-aware native placement found no consistent advantage in correct-answer probability for either submission track, but did not establish equivalence between the tracks. Structural comparisons depend on metric weighting, placement and device generation. Provider interfaces also limit observability: Rigetti's supported-operation list remained unchanged across a device generation that replaced the native entangler. We classify silent interface failures in composed toolchains and identify checks at toolchain boundaries, connecting valid cross-provider comparisons with concrete software-quality practices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.21714) | 2026-10-16
