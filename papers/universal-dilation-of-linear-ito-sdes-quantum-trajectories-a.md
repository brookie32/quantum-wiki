---
title: "Universal Dilation of Linear Ito SDEs: Quantum Trajectories and Lindblad Simulation of Second Moments"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.05928"
summary: "arXiv:2601.05928v3 Announce Type: replace Abstract: We present a universal framework for simulating N-dimensional linear Ito stochastic differential equations (SDEs) on quantum computers with additive"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2601.05928v3 Announce Type: replace Abstract: We present a universal framework for simulating N-dimensional linear Ito stochastic differential equations (SDEs) on quantum computers with additive or multiplicative noises. Building on a unitary dilation technique, we establish a rigorous mapping from the general linear SDEs [ dX_t = A(t) X_t,dt + sum_{j=1}^J B_j(t)X_t,dW_t^j ] to stochastic Schrodinger equations (SSE) on a dilated Hilbert space. Crucially, this embedding is pathwise exact in that the classical solution is recovered as a projection of the dilated quantum state for each fixed noise realization. We demonstrate that the resulting SSEs are {naturally implementable} on digital quantum processors, where the stochastic Wiener increments are encoded directly by preparing the ancillary qubits. Exploiting this physical mapping, we develop two algorithmic strategies: (1) a trajectory-based approach that uses sequential weak measurements to realize efficient stochastic integrators, including a second-order scheme, and (2) an ensemble-based approach that maps moment evolution to a deterministic Lindblad quantum master equation, enabling simulation without Monte Carlo sampling. We provide error bounds based on a stochastic light-cone analysis and validate the framework with numerical experiments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.05928) | 2026-09-11
