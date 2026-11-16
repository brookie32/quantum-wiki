---
title: "Max-Cut QAOA on Non-Hardware-Native Graphs via MinLA Surrogates and Configuration Recovery"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18002"
summary: "arXiv:2611.18002v1 Announce Type: new Abstract: For non-hardware-native extsc{MAX-CUT} instances, the Quantum Approximate Optimization Algorithm (QAOA) can incur additional two-qubit depth overhead du"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18002v1 Announce Type: new Abstract: For non-hardware-native extsc{MAX-CUT} instances, the Quantum Approximate Optimization Algorithm (QAOA) can incur additional two-qubit depth overhead due to SWAP-based routing of interactions between non-adjacent qubits. We propose a hybrid quantum--classical workflow that reduces this depth by selectively removing interactions and subsequently recovers solution quality through classical optimization of the original extsc{MAX-CUT} objective. We employ a Minimum Linear Arrangement (MinLA)-based vertex ordering to preferentially retain short-range interactions, thereby constructing a two-qubit depth-reduced surrogate QAOA ansatz. To compensate for the information lost through interaction removal, we develop classical extit{recovery} strategies that refine QPU-sampled bitstrings directly on the original extsc{MAX-CUT} objective. We develop two recovery strategies: signed-residue-based local search and bipartite-block optimization, where each conditional block problem is solved exactly using an s--t minimum cut. Recovery is performed independently on each sampled configuration, ensuring monotonic improvement in cut value without additional QPU executions. We evaluate the workflow on exttt{ibm_kingston} for 120 distinct non-hardware-native instances comprising 6-regular and Erdos--Renyi graphs with 40, 60 and 100 vertices. We verify that the surrogates substantially reduce transpiled two-qubit depth while staying within the prescribed two-qubit depth, and with recovery yield extit{near-optimal} cuts on the original graphs. These results demonstrate the potential of hardware-aware interaction selection and classical recovery to extend QAOA to graph instances whose full cost Hamiltonians exceed practical circuit-depth budgets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18002) | 2026-11-16
