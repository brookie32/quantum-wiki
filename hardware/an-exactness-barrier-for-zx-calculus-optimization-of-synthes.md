---
title: "An Exactness Barrier for ZX-Calculus Optimization of Synthesized Clifford+T Circuits"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.22801"
summary: "arXiv:2608.22801v1 Announce Type: new Abstract: Gate synthesis and circuit optimization are usually studied separately, and evidence on their interaction is contradictory: ZX-calculus rewriting remove"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.22801v1 Announce Type: new Abstract: Gate synthesis and circuit optimization are usually studied separately, and evidence on their interaction is contradictory: ZX-calculus rewriting removes a stable fraction of Solovay-Kitaev circuits, yet almost nothing from number-theoretically synthesized circuits. We show both behaviours follow from a single bound. For any optimizer that preserves the implemented element exactly--including all sound ZX rewriting with extraction--the achievable T-count is bounded below by the denominator exponent of the synthesized ring element. This exactness barrier is computable per instance and separates exact post-processing from approximation-aware resynthesis by a certified factor reaching 101x at recursion depth five. The two behaviours are then the barrier operating at different distances from the floor. For Solovay-Kitaev circuits we prove that the local ZX simplification layer (spider fusion and identity removal) computes exactly the free-product normal form of Z_2 * Z_8, giving exact per-instance compression and, under a calibrated ergodicity hypothesis, a depth-independent limit law confirmed on two independently constructed nets. For number-theoretically synthesized circuits the floor is already saturated: on single-qubit words automated ZX simplification attains it exactly, via a closed-form formula for minimal T-count in terms of phase linkage through the Z-axis normalizer. At two qubits and beyond the same valuation yields unconditional rigidity certificates, which on the quantum-Shannon-decomposition plus gridsynth pipeline certify 99.4-99.9% of the synthesized T-count as incompressible, with rigidity strengthening as accuracy tightens. This explains, and predicts the size of, the near-null optimization recently reported for that pipeline.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.22801) | 2026-08-25
