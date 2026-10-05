---
title: "Compiling Together: High-Throughput Distributed Quantum Computing via Multi-Compilation"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03260"
summary: "arXiv:2610.03260v1 Announce Type: new Abstract: Quantum computing is a promising paradigm for problems that are challenging for classical machines, but realizing that promise requires far more qubits "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03260v1 Announce Type: new Abstract: Quantum computing is a promising paradigm for problems that are challenging for classical machines, but realizing that promise requires far more qubits than a single processor can offer. Distributed quantum computing (DQC) scales out by connecting multiple quantum processing units (QPUs), at the cost of making entanglement the scarce resource: every remote gate consumes a Bell pair, and inter-QPU links generate Bell pairs at finite rates orders of magnitude slower than local gates. Since quantum programs are executed repeatedly, this rate bounds how fast shots complete and thus how fast results are obtained. Existing DQC compilers emit a single implementation per circuit, so throughput is capped by its busiest link while other links stay idle. We observe that alternative compilations of the same circuit are logically equivalent yet stress different links; executing them concurrently and pooling their samples converts idle Bell pairs into additional shots. We formulate the joint selection of compilations and allocation of shots under per-link Bell-pair capacities as Candidate-Constrained Max-Shot Allocation (CMA), prove it NP-hard, and solve it with a dynamic program and its approximate variant AppDP, a compact MILP, and a greedy heuristic Effi. In simulation on six-QPU networks, multi-compilation raises throughput by 2-4.5* over the single compilation and correspondingly improves output fidelity under equal Bell-pair budgets. On hardware, it increases measured fidelity by up to 93% and reaches the single-compilation fidelity in up to 10* less time. Scaling to 36 QPUs and 144-qubit circuits, MILP improves throughput over the single compilation by 76.8% on average across 48 configurations while Effi allocates in milliseconds.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03260) | 2026-10-05
