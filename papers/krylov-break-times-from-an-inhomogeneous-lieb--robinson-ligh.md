---
title: "Krylov Break Times from an Inhomogeneous Lieb--Robinson Light Cone"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27399"
summary: "arXiv:2608.27399v1 Announce Type: new Abstract: Krylov and Lanczos approximations are used in quantum dynamics, quantum subspace methods, and Hamiltonian learning. A practical question is how long an "
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2608.27399v1 Announce Type: new Abstract: Krylov and Lanczos approximations are used in quantum dynamics, quantum subspace methods, and Hamiltonian learning. A practical question is how long an m-dimensional Krylov truncation can be trusted. We argue that this time is fixed by causal propagation on the associated Jacobi chain. The relevant distance is not the Krylov index itself, but the inhomogeneous transport metric rho(m,n) = sum_{j=min(m,n)}^{max(m,n)-1} 1/b_j, where b_j is the Lanczos hopping across the bond j leftrightarrow j+1. We prove a Lieb--Robinson bound in this metric. Its small-weight limit gives the velocity v_{rm LR} = 2, meaning that propagation is exponentially suppressed outside the cone rho(m,n) simeq 2|t|. The error of a finite Krylov approximation to the return amplitude is a round-trip effect: information has to travel from the probe to the truncation boundary and back. Combining the Lieb--Robinson bound with Duhamel's formula yields a lower bound on the error of the truncated dynamics. For a fixed tolerance epsilon, let the break time t_ast(m;epsilon) denote the longest time for which the m-dimensional truncation is guaranteed to reproduce the exact return amplitude within error epsilon. We show that t_ast(m;epsilon) ge au_m[1-o(1)], where au_m = rho(0,m) = sum_{j<m} 1/b_j. When the probe spreads along the chain, this lower bound is also tight, so t_ast(m) simeq au_m. The situation is different when the probe excites only a localized part of the spectrum, or a part already resolved by the truncation. In this case, essentially no signal reaches the boundary. Beyond a state-dependent Krylov dimension m_ast, the approximation can therefore remain accurate at all times, and the break time is effectively infinite. Numerical tests on spin chains and random Jacobi matrices support t_ast(m) simeq au_m in the transport-limited regime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27399) | 2026-08-28
