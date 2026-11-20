---
title: "Projected evolution of quantum gates for circuit simulation with matrix product states"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2508.10096"
summary: "arXiv:2508.10096v2 Announce Type: replace Abstract: Tensor networks and specifically matrix product states (MPS) enable feasible classical quantum circuit simulation when entanglement remains compress"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2508.10096v2 Announce Type: replace Abstract: Tensor networks and specifically matrix product states (MPS) enable feasible classical quantum circuit simulation when entanglement remains compressible, but for this, gate updates must balance accuracy, representation size, and runtime. Conventional methods incorporate a complete gate into the MPS before compressing enlarged bonds. Here, we instead use lessons from the time-dependent variational principle (TDVP) to analyze the projected action of each gate on the MPS by reducing it to a continuous generator path. We establish the spatial and state-space structure of this projected evolution and show that both the fixed-rank and two-site actions are confined to a contiguous window spanned by the gate while retaining boundary information from the surrounding MPS. Within this window characterization, we delineate when the instantaneous two-site action is exact and when variational directions can block it completely. Using standard nearest-point-projection geometry, we also show that fixed-rank TDVP and the local nearest fixed-rank projection of the exact gate endpoint agree to first order. We implement the gate-window restriction with rank-adaptive two-site TDVP and test both the projected update and a hybrid method that reserves it for long-range gates. Across the circuit benchmarks, these implementations incur runtime overhead and show no consistent accuracy--cost advantage over the tested baseline methods. The resulting framework provides a gate-specific structural analysis and a tested implementation together with explicit limits on its practical performance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2508.10096) | 2026-11-20
