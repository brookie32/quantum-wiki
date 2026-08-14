---
title: "Quantum simulation of non-Markovian dynamical systems"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.13533"
summary: "arXiv:2608.13533v1 Announce Type: new Abstract: Existing quantum algorithms for simulating dynamical systems -- from Hamiltonian simulation to linear and nonlinear differential equations solvers -- si"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.13533v1 Announce Type: new Abstract: Existing quantum algorithms for simulating dynamical systems -- from Hamiltonian simulation to linear and nonlinear differential equations solvers -- simulate Markovian dynamics, in which the system's future evolution depends solely on its current state. We turn our attention to developing quantum algorithms for non-Markovian dynamical systems where the system's future evolution depends on its past history and thus has memory. Specifically, we develop efficient algorithms for linear Volterra integro-differential equations (VIDEs) with a convolution memory kernel that output a quantum state encoding the state description over a time interval or at a particular time. Given efficient circuits for the problem inputs, our algorithms achieve an exponential speedup in system size over existing classical algorithms. We develop an algorithm for general kernels assuming that extsf{M} < 1, where extsf{M} characterizes the strength of the memory term relative to the dissipation of the Markovian part of the dynamics. We complement this with lower bounds for general-kernel VIDEs when extsf{M} geq 1, showing that the problem becomes intractable for a family of systems. However, by specializing to structured kernels which admit concise decompositions over exponentials, we develop efficient quantum algorithms even when extsf M geq 1 by converting the VIDE into a larger set of ODEs, a procedure which we call Markovianization. As an application of the overall framework, we discuss the Mori-Zwanzig formalism used in open quantum systems and fluid dynamics. Overall, our results expand the range of dynamical systems that quantum computers can simulate efficiently.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.13533) | 2026-08-14
