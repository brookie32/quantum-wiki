---
title: "Error Mitigation by Zero-Noise Extrapolation (ZNE) in Indirect-Control System"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.13038"
summary: "arXiv:2610.13038v1 Announce Type: new Abstract: The indirect-control paradigm offers a scalable approach to quantum computation by restricting external operations to a small subset of qubits, whereas "
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.13038v1 Announce Type: new Abstract: The indirect-control paradigm offers a scalable approach to quantum computation by restricting external operations to a small subset of qubits, whereas the entire system evolves under its intrinsic many-body Hamiltonian. This framework reduces hardware complexity and limits the noise introduced through control channels. Recently, Anan et al. proposed an implementation of the variational quantum eigensolver (VQE) within this indirect-control architecture. However, the impact and integration of quantum error mitigation techniques in such a setting remain largely unexplored. In particular, zero-noise extrapolation (ZNE), a widely used error mitigation strategy, has not yet been systematically adapted to indirect-control VQE. A key requirement of ZNE is the controlled amplification of noise, which is commonly achieved through circuit-level techniques such as unitary folding. In the indirect-control framework, however, quantum operations are largely governed by continuous time-evolution under the system Hamiltonian, making the construction of physically realizable inverse operations non-trivial. In this study, we investigate the feasibility of implementing ZNE within the indirect-controlVQEframework.We address the challenges associated with unitary folding in the presence of time-evolution operators and, with a minimal relaxation of the indirect-control constraint, we propose a ZNE-based error-mitigation strategy that exploits the symmetry of the one-dimensional XY spin chain.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.13038) | 2026-10-12
