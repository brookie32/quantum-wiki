---
title: "Sparse quantum state preparation with improved Toffoli cost"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.09388"
summary: "arXiv:2601.09388v2 Announce Type: replace Abstract: The preparation of quantum states is one of the most fundamental tasks in quantum computing, and a key primitive in many quantum algorithms. Of part"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2601.09388v2 Announce Type: replace Abstract: The preparation of quantum states is one of the most fundamental tasks in quantum computing, and a key primitive in many quantum algorithms. Of particular interest to areas such as quantum simulation and linear-system solvers are sparse quantum states, which contain only a small number s of non-zero computational basis states compared to a generic state. In this work, we present an approach that prepares s-sparse states on n qubits, reducing the number of Toffoli gates required compared to prior art. We work in the established framework of first preparing a dense state on a lceil{log(s)}rceil-qubit sub-register, and then mapping this state to the target state via an isometry, with the latter step dominating the cost of the full algorithm. The speed-up is achieved by designing an efficient algorithm for finding and implementing the isometry. The worst-case Toffoli cost of our isometry circuit, which may be viewed as a batched version of an approach by Malvetti et al., is essentially 2s for sufficiently large values of n, yielding roughly a log(s)/2 improvement factor over the state-of-the-art. In numerical benchmarks on randomly chosen states, the cost is closer to s. With the improved isometry circuit, we examine the dense-state preparation step and present ways to optimize the joint cost of both steps, particularly in the case of target states with purely real coefficients, by outsourcing some sub-tasks from the dense-state preparation to the isometry.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.09388) | 2026-09-07
