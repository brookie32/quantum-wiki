---
title: "Hybrid Quantum Error Correction and Mitigation by Purification"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.11568"
summary: "arXiv:2603.11568v2 Announce Type: replace Abstract: Quantum error correction physically removes errors from a quantum state, while quantum error mitigation improves observable estimates by processing "
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2603.11568v2 Announce Type: replace Abstract: Quantum error correction physically removes errors from a quantum state, while quantum error mitigation improves observable estimates by processing noisy measurement data. We introduce purification quantum error suppression (PQES), a hybrid approach that uses multiple noisy copies of an unknown state to combine these two ideas. The protocol uses SWAP tests to physically reduce errors by purification, while the full outcome record is used to combine all branches without postselection. In this way, PQES avoids the fixed-success-outcome requirement of standard SWAP-test purification while still accessing the power-purified state rho^N. The SWAP identities allow purification steps to be interleaved with unitary circuit blocks, so errors can be suppressed during a computation rather than only at the final measurement. We provide both a parallel binary-tree implementation and a more compact register-recycled implementation using O(Mell) coherent data qubits for an M-qubit register and N=2^ell input copies. We analyze the resulting error thresholds under representative noise models. For local depolarizing noise on the product-state family studied here, the threshold is p_{th}=3/4 for any register size, while local dephasing of |+rangle^{otimes M} has a threshold of p_{th}=1/2. Local Clifford twirling can be used to convert dephasing into a depolarization channel and restore the higher threshold.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.11568) | 2026-07-31
