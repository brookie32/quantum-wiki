---
title: "Shadow Quantum Singular Value Transformation with Shallow Quantum Circuits"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40167"
summary: "arXiv:2609.40167v1 Announce Type: new Abstract: We introduce shadow quantum singular value transformation (Shadow QSVT): given an initial state |{psi}rangle, a Hermitian matrix H, a polynomial f, and "
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40167v1 Announce Type: new Abstract: We introduce shadow quantum singular value transformation (Shadow QSVT): given an initial state |{psi}rangle, a Hermitian matrix H, a polynomial f, and a set of observables {O_1,ots,O_m}, the goal is to estimate langle{psi}|f(H)^{agger}O_j f(H)|{psi}rangle for all jin{1,ots,m}. Shadow QSVT provides a systematic route to reduce the quantum resources required by standard QSVT, which constructs a unitary block-encoding of f(H). It uses structure in the input state and observables, together with the fact that many applications require only observable estimates rather than synthesizing the full unitary. We present three algorithms that exploit structure in the initial state and observables to reduce quantum circuit depth. First, we develop a state-aware QSVT algorithm that prepares the target state with low circuit depth when the Krylov subspace associated with H and |psirangle is low-dimensional or admits an accurate low-dimensional approximation. Second, we introduce an observable-aware Shadow QSVT algorithm that combines a new observable-aware Krylov subspace with history states to further reduce circuit depth and gate complexity. Finally, we develop Classical Shadow QSVT, which constructs a classical representation from H, f, and |psirangle without prior knowledge of the observables or explicit preparation of the target state proportional to f(H)|psirangle. This representation enables estimation of the target quantities for observables specified after the quantum computation. Together, these three algorithms provide tools for reducing the circuit depth of QSVT-based computations across a range of settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40167) | 2026-10-01
