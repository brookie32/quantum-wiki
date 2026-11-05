---
title: "Quantum power iterations via tensor networks"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2404.15048"
summary: "arXiv:2404.15048v2 Announce Type: replace Abstract: In optimization, one of the well-known classical algorithms is power iterations, which recovers the dominant eigenvector of a diagonalizable matrix."
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2404.15048v2 Announce Type: replace Abstract: In optimization, one of the well-known classical algorithms is power iterations, which recovers the dominant eigenvector of a diagonalizable matrix. Since numerous optimization problems can be formulated as an eigenvalue/eigenvector search, this algorithm features wide applicability. Operationally, power iterations perform repeated matrix-to-vector multiplications (exttt{MatVec}) followed by a renormalization step to converge to the dominant eigenvalue/eigenvector. However, classical tensor network realizations can exhibit worst-case exponential growth of tensor ranks with the number of iterations. We propose a quantum realization offering a possible route around this bottleneck. Our method involves casting low-rank representations---MPO for matrices and MPS for vectors---into quantum circuits. Specifically, we recover a unitary approximation by variationally minimizing the Frobenius distance between a target MPO and an MPO ansatz wherein the tensor cores are constrained to unitaries. Such unitary MPOs can be implemented as quantum circuits with ancillary qubits. With appropriate initialization and post-selection on the ancillary space, we realize a single classical iteration. With our proposed methodology, power iterations can be realized entirely on a quantum computer via repeated, static circuit blocks. By exploiting Riemannian optimization and cross-approximation techniques, our methodology becomes instance-agnostic, allowing one to address black-box optimization of functions admitting low-rank tensor network representations within quantum computing. We emphasize that this work establishes the construction and analyzes its reliable operating conditions; it does not demonstrate an end-to-end computational advantage over classical tensor network optimization, which we discuss explicitly.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2404.15048) | 2026-11-05
