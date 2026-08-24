---
title: "Lowering LCU Circuit Width through Maximum-Weight Birkhoff-von Neumann Decomposition"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.27430"
summary: "arXiv:2605.27430v3 Announce Type: replace Abstract: While classical Sinkhorn scaling applies to nonnegative matrices, we show that any complex square matrix whose element-wise absolute value has total"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2605.27430v3 Announce Type: replace Abstract: While classical Sinkhorn scaling applies to nonnegative matrices, we show that any complex square matrix whose element-wise absolute value has total support can be mapped to a phased doubly stochastic matrix, or alternatively embedded into a larger doubly stochastic matrix via matrix completion. Standard Birkhoff-von Neumann and Pauli decompositions represent such matrices as linear combinations of O(N^2) permutation or Pauli terms, leading to a large ancilla overhead in a quantum Linear Combination of Unitaries (LCU) implementation. We prove that a bottleneck variant of Birkhoff's algorithm reduces the number of permutations to O(Nlog(1/arepsilon)), where arepsilon is the ell_1-norm approximation error of the reconstructed matrix, and demonstrate empirically that a largest-weight greedy variant requires only approx 2N terms for dense matrices (the exact average observed is approx 2.4N). The quadratic reduction in term count directly shrinks the ancilla register from 2log_2 N to log_2 N qubits, shortens the SELECT circuit, and is especially valuable in fixed-Hadamard LCU architectures whose success probability scales with 1/K. The approach enables compact quantum implementations of dense operators appearing in optimal transport, non-Hermitian simulation, and other settings amenable to Sinkhorn preconditioning. Furthermore, because the decomposition is a convex combination, the LCU normalization constant is exactly alpha = 1, and the uniform superposition is an eigenvector of the target matrix with eigenvalue~1. This structure can be exploited to achieve high success probability without amplitude amplification in many practical scenarios, including quantum walks and Markov chain simulations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.27430) | 2026-08-24
