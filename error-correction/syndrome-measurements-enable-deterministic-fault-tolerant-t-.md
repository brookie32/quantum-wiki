---
title: "Syndrome measurements enable deterministic fault-tolerant T gates"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29890"
summary: "arXiv:2609.29890v1 Announce Type: new Abstract: Non-Clifford gates are essential for universal quantum computation, yet implementing them fault-tolerantly remains a central challenge for stabilizer co"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29890v1 Announce Type: new Abstract: Non-Clifford gates are essential for universal quantum computation, yet implementing them fault-tolerantly remains a central challenge for stabilizer codes. Here, we show how a syndrome degree of freedom can mediate a logical non-Clifford gate. Releasing one stabilizer check makes an additional logical qubit available within the encoded data block. Two Pauli rotations, followed by syndrome measurement and Clifford feed-forward, then implement a deterministic logical T gate on every stabilizer code of distance at least two, in a suitable logical basis. During the ideal rotations, the state remains in an intermediate stabilizer code whose distance we determine exactly. For pure codes with a balanced factorization, this distance grows with the original code distance, whereas the maximum weight of the stabilizer generators bounds the intermediate distance from above. We realize the mechanism in two circuits that tolerate a single fault under local stochastic circuit noise: a fixed 22-qubit construction admitting recursive error suppression and a direct Golay-code gate protected by measuring a stabilizer check transported through the non-Clifford rotation, which can recover the unknown encoded state even after rejection. Serial implementations with ancilla reuse, reset, and flexible two-qubit connectivity require at most 33 and 32 physical qubits, respectively. These results establish a general mechanism for logical non-Clifford gates and demonstrate how syndrome measurements and recovery can protect the intermediate evolution of encoded information.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29890) | 2026-09-25
