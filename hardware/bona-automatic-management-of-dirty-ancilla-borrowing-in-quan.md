---
title: "Bona: Automatic Management of Dirty Ancilla Borrowing in Quantum Circuits"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08765"
summary: "arXiv:2608.08765v1 Announce Type: cross Abstract: The management of ancilla qubits has become a critical technique for reducing quantum circuit width. Dirty ancillas, which may be borrowed from any te"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08765v1 Announce Type: cross Abstract: The management of ancilla qubits has become a critical technique for reducing quantum circuit width. Dirty ancillas, which may be borrowed from any temporarily idle qubit regardless of their initial states, offer substantial flexibility for width optimization, but their use has so far required manual and error-prone handling. We formalize the dirty-qubit borrowing problem and establish a fundamental computational limit by proving its NP-hardness. To support practical optimization, we present ona, the first scheduler for dirty-qubit borrowing, built on a novel depth-aware heuristic algorithm. We evaluate ona~ across a variety of benchmarks, including practical quantum circuits and randomly arranged compositions of real circuit modules, and find that it reduces nearly 99% of dirty ancillas on average with controlled depth overhead. In particular, for parallel quantum walk---an essential component of parallel Hamiltonian simulation---ona~ matches the circuit width achieved by the clean-qubit schemes of iteauthor{jiang2024recycling}~(iteyear{jiang2024recycling}) and iteauthor{quantinuum}~(iteyear{quantinuum}), but attains significantly smaller circuit depth, providing concrete evidence that dirty ancillas offer unique optimization advantages in circuits with certain parallelism.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08765) | 2026-08-11
