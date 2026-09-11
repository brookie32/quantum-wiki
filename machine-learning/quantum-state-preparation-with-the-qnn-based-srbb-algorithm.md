---
title: "Quantum State Preparation with the QNN-based SRBB Algorithm"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.13647"
summary: "arXiv:2503.13647v2 Announce Type: replace Abstract: In this work, a novel algorithm structured on Lie algebras for the approximate quantum state preparation problem is proposed, addressing a challenge"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2503.13647v2 Announce Type: replace Abstract: In this work, a novel algorithm structured on Lie algebras for the approximate quantum state preparation problem is proposed, addressing a challenge of fundamental importance in many areas of quantum computing. The algorithm uses a variational quantum circuit designed on the Standard Recursive Block Basis (SRBB), a hierarchical construction for the matrix algebra of the SU(2^n) group, which is capable of linking the variational parameters with the topology of the Lie group. Compared to the full algebra, using only diagonal components reduces the number of CNOTs by an exponential factor, as well as the circuit depth, in full agreement with the relaxation principle inherent to the approximation methodology of minimizing resources while achieving high accuracy. The desired quantum state is then approximated by a novel quantum neural network, which is designed based on the diagonal SRBB sub-algebra. This approach provides a new scheme for approximate quantum state preparation in a variational framework and a specific use case for the SRBB hierarchy. The performance of the algorithm is assessed with different loss functions, such as fidelity, trace distance, and Frobenius norm, in relation to two optimizers: Adam and Nelder-Mead. The results highlight the potential of SRBB in close connection with the geometry of unitary groups, achieving high accuracy of up to 4 qubits in simulation, but also its current limitations with an increasing number of qubits. Additionally, the approximate SRBB-based QSP algorithm has been tested on real quantum devices to assess its performance with a small number of qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.13647) | 2026-09-11
