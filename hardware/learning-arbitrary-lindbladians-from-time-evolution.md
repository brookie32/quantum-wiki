---
title: "Learning Arbitrary Lindbladians from Time Evolution"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28610"
summary: "arXiv:2607.28610v1 Announce Type: new Abstract: We study the problem of learning an unknown Markovian open-system generator from access to its physical time evolution. This generator, called a Lindbla"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.28610v1 Announce Type: new Abstract: We study the problem of learning an unknown Markovian open-system generator from access to its physical time evolution. This generator, called a Lindbladian, contains Hamiltonian and dissipative coefficients indexed by an exponentially large family of possible Pauli terms. We propose an efficient algorithm that learns arbitrary Lindbladians from time evolution under minimal assumptions. For a Lindbladian of dynamical strength at most Lambda, the algorithm estimates every coefficient to error epsilon using widetilde O(Lambda^2/epsilon^2) experiments and widetilde O(Lambda/epsilon^2) total evolution time, together with polynomial classical running time. The algorithm consists of two nonadaptive, ancilla-free, and control-free stages: 1. The support-learning stage outputs a candidate support of size poly(Lambda/eta) that contains every Hamiltonian and dissipative coordinate of magnitude at least eta, using widetilde O(Lambda^2/eta^2) experiments with preparations of product Pauli eigenstates and single-qubit Pauli measurements. 2.The coefficient-learning stage estimates all coefficients in any candidate support of size M to error epsilon, using widetilde O(Lambda^2log M/epsilon^{2}) experiments with preparations of random stabilizer states and measurements in random Clifford bases. Composing the two stages identifies and estimates every coefficient of an arbitrary Lindbladian in polynomial time. The experiment-count and total-evolution-time scalings match the lower bounds up to logarithmic factors, so the algorithm is nearly optimal for learning arbitrary Lindbladians.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28610) | 2026-07-31
