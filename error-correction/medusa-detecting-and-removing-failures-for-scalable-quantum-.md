---
title: "Medusa: Detecting and Removing Failures for Scalable Quantum Computing"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.16289"
summary: "arXiv:2511.16289v2 Announce Type: replace Abstract: Quantum circuits will experience failures that lead to computational errors. We introduce Medusa, an automated compilation method for lowering a cir"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2511.16289v2 Announce Type: replace Abstract: Quantum circuits will experience failures that lead to computational errors. We introduce Medusa, an automated compilation method for lowering a circuit's failure rate. Medusa uses flags to predict the absence of high-weight errors. Our method can numerically upper bound the failure rate of a circuit in the presence of flags, and fine tune the fault-tolerance of the flags in order to reach this bound. We assume the flags can have an increased fault-tolerance as a result of applying surface QECs to the gates interacting with them. We use circuit level depolarizing noise to evaluate the effectiveness of these flags in revealing the absence of the high-weight stabilizers. Medusa reduces the cost of quantum-error-correction (QEC) because the underlying circuit has a lower failure rate. We benchmark our approach using structured quantum circuits representative of ripple-carry adders. In particular, our flag scheme demonstrates that for adder-like circuits, the failure rate of large-scale implementations can be lowered to fit the failure rates of smaller-scale circuits. We show numerically that a slight improvement in the local fault-tolerance of the flag-qubits can lead to a reduction in the overall failure rate of the entire quantum circuit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.16289) | 2026-07-24
