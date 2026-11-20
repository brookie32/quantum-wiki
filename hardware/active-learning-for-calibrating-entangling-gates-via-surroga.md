---
title: "Active Learning for Calibrating Entangling Gates via Surrogate-Based Optimization"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.00284"
summary: "arXiv:2607.00284v2 Announce Type: replace Abstract: High-fidelity quantum gates require precise tuning of many classical control parameters, and drift in these parameters necessitates periodic recalib"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2607.00284v2 Announce Type: replace Abstract: High-fidelity quantum gates require precise tuning of many classical control parameters, and drift in these parameters necessitates periodic recalibration that takes time and qubit resources. Physics-based calibration can be efficient, but it requires a validated and high-fidelity model of the quantum gate under the given classical control and environment. A high-fidelity model is expensive to build, especially as systems scale, and will have to be periodically re-validated as system parameters drift. Here, we present a physics-agnostic active-learning framework that identifies optimal control parameters from noisy measurement outcomes. A generic Gaussian process with a heteroskedastic noise model set by quantum projection noise is used to model the score landscape of the calibration sequence. Bayesian optimization simultaneously learns the calibration landscape and locates its optimum. We validate the technique by calibrating a two-qubit trapped-ion entangling gate. In simulation, where the ground-truth landscape is known, we find that the surrogate accurately models the three-parameter landscape and the calibrated infidelity saturates at a level set by the number of shots per evaluation. Validation on the Sandia Quantum User Testbed shows that the physics-agnostic protocol works on an experimental system with four calibrated parameters, needing an average of 44pm 11 evaluation points at 100 shots per point to model the calibration landscape and find the optimal parameter set. These results show that active learning with physics-agnostic surrogate models can calibrate quantum gates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.00284) | 2026-11-20
