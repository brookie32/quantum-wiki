---
title: "A New Quantum Linear System Algorithm Beyond the Condition Number and Its Application to Solving Multivariate Polynomial Systems"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.05588"
summary: "arXiv:2510.05588v4 Announce Type: replace Abstract: Given a matrix A of dimension M imes N and a vector ec{b}, the quantum linear system (QLS) problem asks for the preparation of a quantum state |ec{y"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2510.05588v4 Announce Type: replace Abstract: Given a matrix A of dimension M imes N and a vector ec{b}, the quantum linear system (QLS) problem asks for the preparation of a quantum state |ec{y}rangle proportional to the solution of Aec{y} = ec{b}. Existing QLS algorithms have runtimes that scale linearly with the condition number kappa(A), the sparsity of A, and logarithmically with inverse precision, but often overlook structural properties of ec{b}, whose alignment with A's eigenspaces can greatly affect performance. In this work, we present a new QLS algorithm that explicitly leverages the structure of the right-hand side vector ec{b}. The runtime of our algorithm depends polynomially on the sparsity of the augmented matrix H = [A, -ec{b}], the inverse precision, the ell_2 norm of the solution ec{y} = A^+ ec{b}, and a new instance-dependent parameter [ ET= sum_{i=1}^M p_i^2 dot d_i, ] where ec{p} = (AA^{op})^+ ec{b}, and d_i denotes the squared ell_2 norm of the i-th row of H. We also introduce a structure-aware rescaling technique tailored to the solution ec{y} = A^+ ec{b}. Unlike left preconditioning methods, which transform the linear system to DAec{y} = Dec{b}, our approach applies a right rescaling matrix, reformulating the linear system as ADec{z} = ec{b}. As an application of our instance-aware QLS algorithm and new rescaling scheme, we develop a quantum algorithm for solving multivariate polynomial systems in regimes where prior QLS-based methods fail. This yields an end-to-end framework applicable to a broad class of problems. In particular, we apply it to the maximum independent set (MIS) problem, formulated as a special case of a polynomial system, and show through detailed analysis that, under certain conditions, our quantum algorithm for MIS runs in polynomial time.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.05588) | 2026-11-11
