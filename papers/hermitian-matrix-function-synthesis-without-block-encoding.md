---
title: "Hermitian Matrix Function Synthesis without Block-Encoding"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.18249"
summary: "arXiv:2512.18249v2 Announce Type: replace Abstract: Implementing polynomial functions of Hermitian matrices on quantum hardware is a foundational task in quantum computing, critical for accurate Hamil"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2512.18249v2 Announce Type: replace Abstract: Implementing polynomial functions of Hermitian matrices on quantum hardware is a foundational task in quantum computing, critical for accurate Hamiltonian simulation, quantum linear system solving, high-fidelity state preparation, machine learning kernels, and other advanced quantum algorithms. Existing state-of-the-art techniques, including Qubitization, Quantum Singular Value Transformation (QSVT), and Quantum Signal Processing (QSP), rely heavily on block-encoding the Hermitian matrix. These methods are often constrained by the complexity of preparing the block-encoded state, the overhead associated with the required ancillary qubits, or the challenging problem of angle synthesis for the polynomial's phase factors, which limits the achievable circuit depth and overall efficiency. In this work, we propose a novel and resource-efficient approach to implement arbitrary polynomials of a Hermitian matrix by leveraging the Generalized Quantum Signal Processing (GQSP) framework. Our method circumvents the need for block-encoding and avoids the compounding post-selection overheads characteristic of LCU-based constructions, achieving a stable, degree-independent success probability. We derive closed-form expressions for symmetric polynomial expansions and demonstrate how linear combinations of GQSP circuits can realize the desired transformation. This approach reduces resource overhead and opens new pathways for quantum algorithm design for functions of Hermitian matrices, particularly in settings where the Hermitian operator arises naturally from symmetric combinations of unitaries.



## Related
- [[symplectic-perspective-to-quantum-computing-for-hamiltonian-|Symplectic perspective to quantum computing for Hamiltonian systems]]
- [[a-new-algorithm-for-applying-sequences-of-affine-transformat|A New Algorithm for Applying Sequences of Affine Transformations in Quantum Circuits]]
- [[universal-quantum-control-over-non-hermitian-continuous-vari|Universal quantum control over non-Hermitian continuous-variable systems]]
- [[a-unified-quantum-computing-quantum-monte-carlo-framework-th|A unified quantum computing quantum Monte Carlo framework through structured state preparation]]
- [[encoding-strategies-for-quantum-enhanced-fluid-simulations-o|Encoding strategies for quantum enhanced fluid simulations: opportunities and challenges]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.18249) | 2026-04-28
