---
title: "Quantum Circuit Pruning: From NISQ Architectures to Fault-Tolerant Operations"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00669"
summary: "arXiv:2610.00669v1 Announce Type: new Abstract: We present a routing-aware pruning strategy for quantum circuits that selectively removes parametric two-qubit gates whose computational contribution is"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00669v1 Announce Type: new Abstract: We present a routing-aware pruning strategy for quantum circuits that selectively removes parametric two-qubit gates whose computational contribution is outweighed by the fidelity cost of their execution, and assess it across both Noisy Intermediate-Scale Quantum (NISQ) and fault-tolerant quantum computing (FTQC) architectures. Each two-qubit gate of a circuit is evaluated by comparing an architecture-independent lower bound on the fidelity cost of omitting the gate against a hardware-specific model for the routing execution cost in each setting. We additionally provide an analytical characterization of the pruning boundary as a function of rotation angle, qubit distance, and hardware noise. Simulations on benchmark circuits demonstrate gate count reductions of up to 48.6% and fidelity improvements of up to 47.7% in the NISQ regime, while a feasibility analysis on FT hardware indicates that pruning is expected to remain relevant across a range of code distances and physical error rates. These results establish routing-aware pruning as a practical and unified compilation strategy across the quantum computing stack.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00669) | 2026-10-02
