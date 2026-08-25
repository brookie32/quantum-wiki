---
title: "Sparsity-dependent Complexity Lower Bound of Quantum Linear System Solvers"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.16697"
summary: "arXiv:2601.16697v2 Announce Type: replace Abstract: Quantum linear system (QLS) solvers are a fundamental class of quantum algorithms used in many potential quantum computing applications, including m"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2601.16697v2 Announce Type: replace Abstract: Quantum linear system (QLS) solvers are a fundamental class of quantum algorithms used in many potential quantum computing applications, including machine learning and solving differential equations. The performance of quantum algorithms is often measured by their query complexity, which quantifies the number of oracle calls required to access the input. The main parameters determining the complexity of QLS solvers are the condition number kappa and sparsity s of the linear system, and the target error epsilon. To date, the best known query-complexity lower bound is Omega(kappalog(1/epsilon)), which establishes the optimality of the most recent QLS solvers. The original proof of this lower bound is attributed to Harrow and Kothari, but their result is unpublished. Furthermore, when discussing a more general lower bound including the sparsity s of the linear system, it has become folklore that it should read as Omega( kappa sqrt{s}log(1/epsilon)). In this work, we establish the rigorous lower bound capturing the sparsity dependence of QLS. We prove the lower bound of Omega(kappasqrt{s}) for any quantum algorithm that solves QLS with constant error. While the dependence on all parameters kappa,s,epsilon remains an open problem, our result provides a crucial stepping stone toward the complete characterization of QLS complexity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.16697) | 2026-08-25
