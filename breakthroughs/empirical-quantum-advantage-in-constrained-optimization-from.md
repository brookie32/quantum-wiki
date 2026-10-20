---
title: "Empirical Quantum Advantage in Constrained Optimization from Encoded Unitary Designs"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.14296"
summary: "arXiv:2511.14296v4 Announce Type: replace-cross Abstract: We introduce the Constraint-Enhanced Quantum Approximate Optimization Algorithm (CE-QAOA), a shallow, constraint-aware ansatz that operates in"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2511.14296v4 Announce Type: replace-cross Abstract: We introduce the Constraint-Enhanced Quantum Approximate Optimization Algorithm (CE-QAOA), a shallow, constraint-aware ansatz that operates inside the one-hot product space [n]^m, where m is the number of blocks and each block is initialized in an n-qubit W_n state. We give an ancilla-free, depth-optimal encoder that prepares W_n using n-1 two-qubit rotations per block, and a two-local block-XY mixer that preserves the one-hot manifold and has a constant spectral gap on the one-excitation sector. At the level of expressivity, we establish per-block controllability, implying approximate universality per block. At the level of distributional behavior, we show that, after natural block and symbol permutation twirls, shallow CE-QAOA realizes an encoded unitary 1-design and supports approximate second-moment (2-design) behavior; combined with a Paley-Zygmund argument, this yields finite-shot anticoncentration guarantees. Algorithmically, we wrap constant-depth sampling with a deterministic feasibility checker to obtain a polynomial-time hybrid quantum-classical solver (PHQC) that returns the best observed feasible solution in O(S n^2) time, where S is a polynomial shot budget. We obtain two advantages. First, when CE-QAOA fixes r >= 1 locations different from the start city, we achieve a Theta(n^r) reduction in shot complexity even against a classical sampler that draws uniformly from the feasible set. Second, against a classical baseline restricted to raw bitstring sampling, we show an exp(Theta(n^2)) minimax separation. In noiseless circuit simulations of traveling salesman problem instances with n in {4,...,10} locations from the QOPTLib benchmark library, we recover the global optimum at depth p = 1 using polynomial shot budgets and coarse parameter grids defined by the problem size.



## Related
- [[m-qam-mimo-maximum-likelihood-detection-with-qaoa-ml-rate-of|M-QAM MIMO Maximum-Likelihood Detection with QAOA: ML-Rate Offline Angle Design and Correlated Infinite-Size Spin-Glass Models]]
- [[decoupling-of-the-qaoa-into-independent-spin-boson-systems-a|Decoupling of the QAOA into independent spin-boson systems and high-depth performance on pure and mixed spin glasses]]
- [[quantum-approximate-optimization-via-noise-directed-adaptive|Quantum Approximate Optimization via Noise-Directed Adaptive Warm-Starting]]
- [[improving-feasibility-in-quantum-approximate-optimization-al|Improving Feasibility in Quantum Approximate Optimization Algorithm for Vehicle Routing via Constraint-Aware Initialization and Hybrid XY-X Mixing]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.14296) | 2026-10-16
