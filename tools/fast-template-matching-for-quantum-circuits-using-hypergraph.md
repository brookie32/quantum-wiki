---
title: "Fast Template Matching for Quantum Circuits Using Hypergraph"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29095"
summary: "arXiv:2610.29095v1 Announce Type: new Abstract: Quantum circuit optimization is a key step toward the efficient execution of quantum algorithms. Template matching has emerged as one of the dominant ap"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29095v1 Announce Type: new Abstract: Quantum circuit optimization is a key step toward the efficient execution of quantum algorithms. Template matching has emerged as one of the dominant approaches for simplifying quantum circuits, yet it confronts the intrinsic challenge of accommodating gate commutativity. The state-of-the-art template-matching algorithm relies on a directed acyclic graph (DAG) representation. While this DAG-based technique handles gate commutativity satisfactorily, it fails to preserve the local connectivity inherent to quantum circuits, thereby leading to relatively high matching complexity. In this paper, we introduce a hypergraph representation (HG), a commutativity-aware representation that collapses commuting gates into a single super-node while retaining all local connectivity. This enables matches to be extended locally without revisiting the rest of the circuit, with incremental updates limited to the immediate neighborhood. Experimental results demonstrate that our HG matcher achieves 11--606x speed-up over the DAG-based implementation in Qiskit (Iten et al., 2022) on both random and arithmetic benchmarks, while maintaining the same optimization quality. The acceleration increases with circuit size, confirming that preserving locality and connectivity is the key to scalable quantum circuit optimisation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29095) | 2026-10-22
