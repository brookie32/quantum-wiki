---
title: "Distributed Variational Quantum Linear Solver"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.01426"
summary: "arXiv:2604.01426v2 Announce Type: replace Abstract: This paper develops a distributed variational quantum algorithm for solving large-scale linear equations. For a linear system of the form Ax=b, the "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2604.01426v2 Announce Type: replace Abstract: This paper develops a distributed variational quantum algorithm for solving large-scale linear equations. For a linear system of the form Ax=b, the large square matrix A is partitioned into smaller square block submatrices, each of which is known only to a single noisy intermediate-scale quantum (NISQ) computer. Each NISQ computer communicates with certain other quantum computers in the same row and column of the block partition, where the communication patterns are described by the row- and column-neighbor graphs, both of which are connected. The proposed algorithm integrates a variant of the variational quantum linear solver at each computer with distributed classical optimization techniques. The derivation of the quantum cost function provides insight into the design of the distributed algorithm. Numerical quantum simulations demonstrate that the proposed distributed quantum algorithm can solve linear systems whose size scales with the number of computers and is therefore not limited by the capacity of a single quantum computer.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.01426) | 2026-10-05
