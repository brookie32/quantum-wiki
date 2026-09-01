---
title: "Hamiltonian Simulation and Linear Combination of Unitary Decomposition of Structured Matrices"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.17816"
summary: "arXiv:2603.17816v2 Announce Type: replace Abstract: To process a problem with a Quantum Processing Unit (QPU), it must be transformed into a sequence of quantum operators, or gates. These operators ar"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2603.17816v2 Announce Type: replace Abstract: To process a problem with a Quantum Processing Unit (QPU), it must be transformed into a sequence of quantum operators, or gates. These operators are either packed into a query (i.e. quantum algorithm primitive) that encodes the problem, or used to construct the cost function for Variationnal Quantum Algorithm (VQA). Typical queries are the problem Hamiltonian Simulation (HS) and the problem Block-Encoding (BEing). To construct the circuits associated with the quantum description, the problem must be mapped as a Linear Combination of Hamiltonian (LCH) or a Linear Combination of nitaries (LCU) matrices. All the summed Hamiltonian matrices or unitary matrices must have a known decomposition in basic gates. The complexity of this query should be incorporated into the quantum algorithm's query complexity, thereby limiting the processing possibilities of QPU for many problems. In this work, we propose Hamiltonian matrices used to map the problem of interest, and that behave like a single qubit when expressed in the appropriate basis. It leads to a framework, the Special Tripotent Hamiltonian (STH) Framework, able to implement most of the typical problems considered for quantum computing. These methods address many problems implemented on QPUs, ranging from second-quantization chemistry operators to graphs associated with Partial Differential Equations (PDE), sparse matrices, and higher-order optimization problems. This work underlines interesting properties associated with the STH basic gate decomposition. These include the ability to switch between LCH and LCU, map non-Hermitian problems, and construct the quantum circuit queries required for quantum computing. We also provide a list of STH that are used for the matrix decomposition of many structured matrices. These structured matrices are associated with graph adjacency matrices that can be combined to implement structured matrices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.17816) | 2026-09-01
