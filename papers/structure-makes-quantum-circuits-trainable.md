---
title: "Structure makes quantum circuits trainable"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.18378"
summary: "arXiv:2611.18378v1 Announce Type: new Abstract: The scalability of variational quantum algorithms is limited by barren plateaus, where gradients vanish exponentially in system size. This worst-case re"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.18378v1 Announce Type: new Abstract: The scalability of variational quantum algorithms is limited by barren plateaus, where gradients vanish exponentially in system size. This worst-case result raises fundamental questions about the trainability of quantum AI models. We present a major advance towards resolving this trainability question by answering whether a given quantum circuit has a barren plateau. We do this using an analytical framework that bounds the gradient variance for arbitrary input states rho and observables M by decomposing the unitary representation of the associated compact Lie group. When the circuit segments on both sides of a gate form 2-designs, we obtain the variance exactly and prove a sufficient condition for trainability: if rho^{otimes 2} and M^{otimes 2} are sufficiently concentrated on the same irreducible invariant subspace of polynomial dimension, and the differentiated gate moves this subspace by an inverse-polynomial amount, then the gradient variance is at least inverse-polynomial. We further present a sampling algorithm that estimates the gradient variance from runs of the ansatz, without constructing the representation-theoretic projectors. Our algorithm decides whether the variance exceeds a tolerance au with the number of runs polynomial in 1/au, including cases in which the bounds are inconclusive. This resolves the question of the trainability of the circuit before expensive training procedures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.18378) | 2026-11-16
