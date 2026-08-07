---
title: "QSCI-CMP: Quantum-Selected Configuration Interaction with Chemically Motivated Preselection"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05766"
summary: "arXiv:2608.05766v1 Announce Type: new Abstract: We present QSCI-CMP, a quantum-classical hybrid algorithm for molecular ground-state calculations that reduces both the query count and the gate count o"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05766v1 Announce Type: new Abstract: We present QSCI-CMP, a quantum-classical hybrid algorithm for molecular ground-state calculations that reduces both the query count and the gate count of sample-based quantum diagonalization with amplitude amplification (SQD-AA). SQD-AA mitigates the measurement bottleneck of quantum-selected configuration interaction (QSCI) by amplifying the basis states that have not yet been measured. Its oracle, however, specifies the measured states by listing them one by one, so its gate count grows with the number of collected states. Moreover, the quantum resources are spent even on states whose importance is evident from chemical knowledge, such as low-order excitations from the Hartree-Fock reference, which could be collected classically at the outset. We therefore propose to fix such chemically trivial states in advance, include them in the diagonalization subspace from the start, and exclude them from the amplification target, using a low-cost oracle that recognizes them through the excitation level and the seniority number of each basis state. We numerically demonstrate that QSCI-CMP reduces the query count and the gate count required to reach chemical accuracy by up to approximately 68% and 72% relative to SQD-AA for 24-qubit systems. The chemically trivial subspace is freely tunable within the classical computational budget. A larger subspace shifts more work onto the classical solver and increases the reduction in quantum cost, and when it captures the ground state sufficiently well, no quantum sampling is needed at all. We also point out that a query-optimal iteration count known from the analysis of quantum search further reduces the query count of both methods by approximately 12%.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05766) | 2026-08-07
