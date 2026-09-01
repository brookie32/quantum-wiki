---
title: "A quantum let within the lambda calculus"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.29380"
summary: "arXiv:2608.29380v1 Announce Type: cross Abstract: Since the seminal work of Selinger and Valiron, the standard design for quantum lambda calculi has kept the quantum state outside the program: terms m"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.29380v1 Announce Type: cross Abstract: Since the seminal work of Selinger and Valiron, the standard design for quantum lambda calculi has kept the quantum state outside the program: terms manipulate pointers to an external register. This is largely due to the difficulty of eliminating tensor products. For example, the calculus lambda_rho^irc embeds density matrices directly within terms, where terms carry the entire computation state, a feature particularly appealing for program verification. However, lacking a tensor elimination construct, it can neither access the individual qubits of a compound state nor discard them. Borgna showed that this inability to discard qubits makes the calculus strictly less expressive than the quantum lambda calculus of Selinger and Valiron. In this paper we show that tensor elimination is possible in this setting. The key observation is that the Pauli decomposition, combined with the spectral decomposition of the Pauli matrices, allows any n-qubit density matrix to be expressed as a real linear combination of tensor products of single-qubit density matrices. Exploiting this fact, we extend lambda_rho^irc with a construct let x^{otimes n} = rho in t, which binds each x_i to a single-qubit density matrix arising from the decomposition of rho. We equip the extended calculus with a rewrite system, a type system, and a denotational semantics, and prove Subject Reduction, Progress, Strong Normalisation, Soundness, and Adequacy. The new construct also recovers the missing ability to discard qubits, thereby restoring expressiveness. Moreover, we show that this is achieved in a physically principled way: a variable unused in t is interpreted exactly as being partial-traced out, as dictated by the no-deleting theorem. We illustrate the resulting compositionality through quantum teleportation and the three-qubit bit-flip code.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.29380) | 2026-09-01
