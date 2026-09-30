---
title: "Improved Quantum Algorithms for Black-Box Abelian Group Decomposition"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36480"
summary: "arXiv:2609.36480v1 Announce Type: new Abstract: Decomposing finite Abelian black-box groups into cyclic factors is a basic problem in quantum computation. We give a quantum algorithm for decomposing f"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36480v1 Announce Type: new Abstract: Decomposing finite Abelian black-box groups into cyclic factors is a basic problem in quantum computation. We give a quantum algorithm for decomposing finite Abelian black-box groups by adapting the quantum sampling and classical lattice-reduction method of Regev's factoring algorithm. The algorithm computes an invariant-factor decomposition and corresponding cyclic generators with high probability. For a group G of order at most 2^n with unique encodings and reversible group-operation cost T_op = Omega(sqrt(n)), our algorithm uses O(sqrt(n)) quantum circuits, each with O~(n T_op) gates and executed at most O(n) times. For comparison, we consider the Cheung-Mosca algorithm, which decomposes the Sylow p-subgroups separately. We also consider the common-modulus implementation of the extended Cheung-Mosca algorithm. Our algorithm reduces the sum of the circuit gate counts from O~(n^2 T_op) to O~(n^(3/2) T_op). The total quantum time bound decreases from O~(n^3 T_op) to O~(n^(5/2) T_op), and the quantum space bound decreases from O(n^2) to O(n) qubits. The classical computation uses polynomially many bit operations and group-operation queries. These improvements rely on two technical ingredients. We prove that the integer relation lattices used in our algorithm admit, with high probability, integral bases whose vectors have Euclidean norm at most exp(O(sqrt(n))). We preserve the circuit-size advantage of Regev's algorithm for group decomposition by incorporating all O(n) sampled generators while keeping the lattice-reduction dimension at O(sqrt(n)).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36480) | 2026-09-30
