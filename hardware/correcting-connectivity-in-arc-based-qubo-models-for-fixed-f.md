---
title: "Correcting Connectivity in Arc-Based QUBO Models for Fixed-Fleet Vehicle Routing"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.26894"
summary: "arXiv:2608.26894v1 Announce Type: new Abstract: We revisit a degree-only arc Hamiltonian for fixed-fleet, homogeneous, uncapacitated vehicle routing. Because its local penalties define only a cycle co"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.26894v1 Announce Type: new Abstract: We revisit a degree-only arc Hamiltonian for fixed-fleet, homogeneous, uncapacitated vehicle routing. Because its local penalties define only a cycle cover, ground states may contain customer cycles disconnected from the depot. We construct a polynomial-size quadratic unconstrained binary optimization (QUBO) repair using capped single-commodity flow and prove that every ground-state routing is connected and cost-optimal under explicit penalty assumptions. For N-1 customers and K nonempty routes, the unreduced encoding uses exactly |E|(1+lceillog_2(N-K+1)rceil) logical problem qubits. A reversible compute--phase--uncompute realization evaluates the flow penalties in O(N^2log N+Nlog^2N) logical gates on a complete graph with O(log N) reusable workspace and no product register. On complete loopless graphs, a depot-delimited single-sequence position encoding uses fewer problem qubits and fewer written terms when the flow-word length grows. Conversely, the flow model achieves a smaller structured logical-gate upper bound under a common reversible accounting model. Exact audits of the Hamiltonian and circuit implementation, combined with a 1{,}200-matrix classical benchmark, verify the formulation and quantify the connectivity gap. Finally, a 32,000-shot Amazon Braket task on IQM Emerald characterizes depth-one termwise Ising circuits on a diagnostic N = 4,, K = 1 counterexample instance. In the degree-only circuit, 78.05% of selected p=1 shots realize the invalid disconnected ground state; the reduced 14-qubit flow-augmented circuit yields no fully feasible sample. These device results characterize mapped Hamiltonians and compilation rather than an asymptotic routing solution advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.26894) | 2026-08-28
