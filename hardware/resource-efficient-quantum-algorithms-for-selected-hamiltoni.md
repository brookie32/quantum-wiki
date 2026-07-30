---
title: "Resource-efficient Quantum Algorithms for Selected Hamiltonian Subspace Diagonalization"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.13160"
summary: "arXiv:2603.13160v2 Announce Type: replace Abstract: Quantum algorithms for selecting a subspace of Hamiltonians to diagonalize have emerged as a promising alternative to variational algorithms in the "
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2603.13160v2 Announce Type: replace Abstract: Quantum algorithms for selecting a subspace of Hamiltonians to diagonalize have emerged as a promising alternative to variational algorithms in the NISQ era. So far, such algorithms, which include the quantum selected configuration interaction (QSCI) and sample-based quantum diagonalization (SQD), have been formulated within second-quantization in Fock space, which leads to inefficient usage of qubit resources. We introduce the first QSCI algorithm developed in the CI-matrix (CIM) framework, which is known to have optimal qubit scaling of exactly lceil log_2 (N) rceil where N is the size of the CIM. In addition, we introduce a novel single-bit flip error mitigation which comes at the overhead of a single qubit and we combine this with a stochastic approximate Trotterization evolution adapted from qDRIFT. Simulating benchmark N_2 and naphthalene molecules on quantum hardware, our results achieved similar accuracy as SQD methods but with significantly less quantum resources. However, our CIM-QSCI algorithm and SQD methods could not match the performance of classical heat-bath CI (HCI) for the same task. Hence, we introduce an augmented version of QSCI called quantum selected heat-bath CI (QSHCI). This variant replaces classical heat-bath sampling with quantum sampling from QSCI to achieve performance comparable to HCI. We note that a current drawback of our approach is the preprocessing cost of O(N^2log N) for constructing the CIM and performing the Pauli decomposition. This can be further improved by considering efficient CIM access models for the stochastic Trotter evolution.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.13160) | 2026-07-30
