---
title: "Semi-Analytical Geometric Synthesis of Robust Quantum Controls"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08107"
summary: "arXiv:2611.08107v1 Announce Type: new Abstract: High-fidelity quantum gates are a central requirement for fault-tolerant quantum computation, yet their implementation is limited by the sensitivity of "
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.08107v1 Announce Type: new Abstract: High-fidelity quantum gates are a central requirement for fault-tolerant quantum computation, yet their implementation is limited by the sensitivity of qubits to environmental noise and by control non-idealities. To mitigate these effects, quantum gates can be designed as dynamically corrected gates (DCGs), where control sequences are engineered to suppress the impact of errors on the resulting operation. Many methods in the literature are able to synthesize DCGs, but they typically rely on numerical optimization, with synthesis times on the order of minutes per gate. Here, we propose an automated semi-analytical method that reduces this cost by orders of magnitude, synthesizing smooth, robust control pulses in tens of milliseconds rather than minutes, with comparable fidelity and robustness. Our approach is based on the Space Curve Quantum Control (SCQC) formalism, where quantum evolution is mapped onto a geometric space curve whose geometric properties determine the target gate and its robustness. We parameterize the curve in the Frenet-Serret frame and employ the Pontryagin Maximum Principle (PMP) to design controls that are robust against both amplitude and dephasing errors. The PMP is formulated as a boundary-value problem and solved using a shooting method. The Frenet-Serret frame is integrated using Rodrigues' formula. Starting from a reference solution, we gradually vary the target rotation angle to construct a library of solutions, whose interpolation provides initial guesses for the shooting parameters of new target gates. We evaluated the method on 2,000 single-qubit rotations, obtaining a mean local optimization time of 39.945 ms per gate after preparation of the interpolation base. Quantum propagation yielded nominal gate infidelities below 10^-9 after virtual phase correction, with verified robustness against quasistatic amplitude and dephasing errors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08107) | 2026-11-06
