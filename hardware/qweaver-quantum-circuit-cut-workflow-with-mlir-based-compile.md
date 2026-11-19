---
title: "QWeaver: Quantum Circuit Cut Workflow with MLIR-based Compiler, Runtime, and Weaver Hybrid Tasks"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23786"
summary: "arXiv:2611.23786v1 Announce Type: new Abstract: Quantum computers available today are constrained by limited qubit counts and high noise levels, making the direct execution of large quantum circuits i"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23786v1 Announce Type: new Abstract: Quantum computers available today are constrained by limited qubit counts and high noise levels, making the direct execution of large quantum circuits infeasible on a single device, and while quantum circuit cutting addresses this by partitioning a large circuit into smaller subcircuits for independent execution, orchestrating the full end-to-end workflow remains a significant programming challenge. In this paper, we present QWeaver, a task-graph-based programming and orchestration workflow framework for quantum circuit cutting that accepts OpenQASM quantum circuits as input and constructs a directed acyclic task graph. In this graph, the Multi-Level Intermediate Representation (MLIR)-based circuit cut is the first task, responsible for analyzing and partitioning the input circuit into executable fragment representations; the generated fragments are then handed to a set of quantum circuit execution tasks that depend on the cut task and can be dispatched concurrently across available quantum backends via the Quantum Intelligent Runtime System (Q-IRIS). Finally, a weaving task, dependent on all execution tasks, performs classical post-processing that applies quasi-probability reconstruction techniques to combine the sampled measurement outcomes of all fragments and recover an accurate approximation of the original circuit's output distribution. We describe the architecture of QWeaver, its integration with Q-IRIS and the execution engine for the Quantum Intermediate Representation (QIR-EE), validate end-to-end reconstruction on GHZ and Harris-Ross instances, and evaluate systems and width trade-offs on structured GHZ simulator workloads.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23786) | 2026-11-19
