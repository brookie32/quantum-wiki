---
title: "Digital Annealer-Assisted CNOT Oriented Quantum Circuit Transpilation with Integrated QUBO Mapping and Routing"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.11500"
summary: "arXiv:2605.11500v2 Announce Type: replace Abstract: Limited qubit counts and two-qubit gate errors motivate reducing CNOT overhead in noisy intermediate-scale quantum (NISQ) transpilation. In circuit-"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2605.11500v2 Announce Type: replace Abstract: Limited qubit counts and two-qubit gate errors motivate reducing CNOT overhead in noisy intermediate-scale quantum (NISQ) transpilation. In circuit-partitioning workflows, repeated hardware sampling can motivate additional classical search, although this study does not evaluate end-to-end runtime or hardware fidelity. We evaluate two Digital Annealer (DA) strategies on seven fixed standalone benchmark instances and a 64-node 8 x 8 square-grid. Hybrid combines DA-based global initial mapping with Qiskit routing, whereas Full DA applies DA to both initial mapping and iterative routing. Hybrid achieved lower mean equivalent CNOT counts than both configured baselines on four benchmarks and identical means on the remaining three. The unweighted macro-average reductions were 6.14% relative to Qiskit and 17.9% relative to t|ketrangle. Among the six benchmarks with feasible Full DA outputs, Full DA achieved lower means than ISAAQ on five, with a success-conditioned macro-average reduction of 48.9%; however, it produced no feasible BV output and did not outperform Hybrid on any benchmark. These results identify DA-generated global placement followed by heuristic routing as the primary positive result and characterize the limitations of the evaluated short-horizon DA routing workflow. Equivalent CNOT count is a structural proxy and does not directly measure execution fidelity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.11500) | 2026-09-01
