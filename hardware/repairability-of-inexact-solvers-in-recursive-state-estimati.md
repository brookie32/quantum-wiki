---
title: "Repairability of Inexact Solvers in Recursive State Estimation with Machine Learning"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28425"
summary: "arXiv:2609.28425v1 Announce Type: new Abstract: Recursive state estimation often executes approximate numerical solutions inside a feedback loop, where highly accurate local steps do not guarantee bet"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28425v1 Announce Type: new Abstract: Recursive state estimation often executes approximate numerical solutions inside a feedback loop, where highly accurate local steps do not guarantee better overall results. For a fixed linear Kalman model, we characterize when a correction within a prescribed subspace and norm budget can meet a local admissibility tolerance, and how the defects actually executed affect the finite-horizon covariance response. Centering each defect on the exact gain for the implemented covariance separates current solve error from inherited gain drift. Expanding the exact residual-drift identity reveals opposing quartic contributions beyond the quadratic response: innovation-covariance inflation enters positively, while local-gain reoptimization enters subtractively. Under matched initialization, an absolute sixth-order remainder bound, uniform over bounded defect sequences at fixed horizon, gives sufficient conditions for quadratic under- or overprediction. Machine learning proposes bounded corrections, while a learner-independent residual certificate and verified fallback govern execution of classical and quantum candidates without changing the reference estimator. In a power-grid tolerance study, learned correction lowers the minimum conjugate-gradient iteration count for deployment without fallback relative to uncorrected solves under the same residual certificate. Gains reconstructed from a variational quantum linear solver and from an annealing-based binary encoding, with small-scale terminal measurements on superconducting hardware and sampling on a quantum annealer, are executed through the same interface. By linking local repairability to nonlinear error propagation, the framework evaluates approximate solvers and learned corrections through independent certification and finite-horizon response, providing a practical basis for studying hybrid quantum--classical computation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28425) | 2026-09-24
