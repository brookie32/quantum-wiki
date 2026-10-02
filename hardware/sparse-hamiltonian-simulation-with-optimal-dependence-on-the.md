---
title: "Sparse Hamiltonian simulation with optimal dependence on the maximum column Euclidean norm"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02030"
summary: "arXiv:2610.02030v1 Announce Type: new Abstract: We give a quantum algorithm for simulating a d-sparse Hermitian Hamiltonian H, assuming a known upper bound Lambda on its maximum column Euclidean norm "
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.02030v1 Announce Type: new Abstract: We give a quantum algorithm for simulating a d-sparse Hermitian Hamiltonian H, assuming a known upper bound Lambda on its maximum column Euclidean norm |H|_{1o2}. For tLambdage1/2, simulation with operator-norm error epsilon uses [ O!left(tLambdasqrt d+sqrt dlog(2/epsilon)right) ] sparse-oracle queries. This removes the subpolynomial overhead in Low's algorithm [STOC 2019], replacing it with an additive logarithmic precision term. For d>1 and tLambdagelog(2/epsilon), the bound matches the worst-case lower bound. A known spectral-norm upper bound may also be used in place of Lambda. The number of 1- and 2-qubit gates is linear in the query scale, up to oracle costs and polynomial overhead in the input bit lengths and logarithmic precision parameters. As applications, we obtain O(kappasqrt d,polylog(kappa/epsilon)) queries for solving d-sparse quantum linear systems with |A|le1 and |A^{-1}|lekappa, under standard sparse and state-preparation access. We also give a gate-efficient implementation of black-box unitaries with at most d nonzero entries per row and column using O(sqrt dlog(2/epsilon)) queries, given sparse access to the unitary and its adjoint. At constant error, the query bound is optimal and yields Theta(sqrt N) queries for arbitrary Nimes N unitaries, resolving the open question on black-box unitary implementation posed by Berry and Childs [QIC 2012].

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02030) | 2026-10-02
