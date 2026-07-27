---
title: "Automated Flag-based Fault-Tolerant State Preparation using Integer Linear Programming"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.22498"
summary: "arXiv:2607.22498v1 Announce Type: new Abstract: Post-selected stabilizer state preparation is a necessary subroutine in fault-tolerant quantum computation, both for initialization of logical qubits, a"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.22498v1 Announce Type: new Abstract: Post-selected stabilizer state preparation is a necessary subroutine in fault-tolerant quantum computation, both for initialization of logical qubits, and for logical-ancilla-based error correction gadgets (e.g. Steane and Knill). Therefore, reducing the number of gates needed to prepare a stabilizer state fault-tolerantly can simultaneously reduce time-to-solution and increase reliability. For small, low-distance codes such as the [[7, 1, 3]] Steane code, circuits with low gate counts can be found by inspection. This becomes impractical for larger codes, necessitating automation. There are two state-of-the-art methods for automated fault-tolerant state preparation, SAT-based stabilizer measurement and flag-at-origin. In this work, we optimize state preparation circuits using the circuit gauge operator formalism to express the construction of flag circuits as an integer linear program. This allows the construction of circuits with equal or lower gate count than the state of the art, while detecting up to three errors. We use this technique to derive a Steane error correction gadget for the [[24, 10, 4]] two-block group algebra code, and test it on Quantinuum's System Model H2 quantum computer with 10,000 shots, resulting in a logical block error rate ~0.00014 (~0.000014 per logical qubit), with ~1.6% of the shots post-selected due to weight-two errors.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.22498) | 2026-07-27
