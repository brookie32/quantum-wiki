---
title: "Constant-Per-Layer-Depth MPS-Pretrained Ansatz for Noisy Distributed Quantum Processors"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01099"
summary: "arXiv:2610.01099v1 Announce Type: new Abstract: Distributed quantum processors could scale variational algorithms beyond single devices, but circuit depth, communication overhead, and noise limit thei"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01099v1 Announce Type: new Abstract: Distributed quantum processors could scale variational algorithms beyond single devices, but circuit depth, communication overhead, and noise limit their performance. We compare ladder, mixed-canonical, and brick-wall realizations of matrix-product-state (MPS) pretraining with matched per-layer two-qubit-block resources. Despite comparable ideal variational quantum eigensolver performance and gradient scales, the shallower brick-wall architecture reduces circuit duration, idle-time decoherence, and zero-noise-extrapolation (ZNE) overhead, yielding superior noisy and ZNE-assisted performance. We then extend MPS-pretrained circuits to modular processors with one communication qubit per quantum processing unit (QPU); a nearest-neighbor QPU-path schedule keeps the per-layer depth constant as QPUs are added. Distributed circuits whose inter-QPU links realize long-range interactions of the target Hamiltonian match or outperform the single-processor brick-wall under noise when communication idle time is short compared with the coherence time. These results establish hardware-aware co-design of tensor-network pretraining, circuit scheduling, and communication topology as a principle for variational quantum computation on noisy modular hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01099) | 2026-10-02
