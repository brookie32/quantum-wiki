---
title: "Quantum Simulation of Non-Hermitian Special Functions and Dynamics via Contour-based Matrix Decomposition"
date: "2026-11-09"
updated: "2026-11-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.10267"
summary: "arXiv:2511.10267v4 Announce Type: replace Abstract: Simulating non-Hermitian dynamics on quantum computers is often hindered by the decay of success probability and the instability of non-diagonalizab"
last_verified: "2026-11-09"
review_by: "2027-02-07"
stale: false
---

arXiv:2511.10267v4 Announce Type: replace Abstract: Simulating non-Hermitian dynamics on quantum computers is often hindered by the decay of success probability and the instability of non-diagonalizable matrices. Here, we present contour-based matrix decomposition (CBMD), a rigorous and versatile quantum functional calculus framework for simulating non-Hermitian matrix functions. By generalizing the matrix Cauchy residue theorem, CBMD decomposes holomorphic non-Hermitian operators into an analytic infinite contour-residue identity, followed by finite truncation with controlled error to yield linear combinations of Hermitian components. For first-order dynamics, CBMD achieves optimal query complexity across all parameters, strictly matching the optimal performance bounds within the linear combination of Hamiltonian simulation (LCHS) paradigm. Beyond first-order systems, the framework naturally generalizes to complex operator functions, including second-order wave dynamics and non-Hermitian special functions such as Bessel and Airy evolutions. Furthermore, CBMD systematically suppresses the asymptotic growth of non-Hermitian components, yielding a significant reduction in the required number of amplitude amplifications compared to the naive scheme of combining monomials via linear combination of unitaries (LCU) after Taylor expansion. Notably, CBMD avoids explicit dependence on matrix diagonalizability, effectively mitigating the long-standing challenges associated with ill-conditioned eigenvectors and Jordan blocks. Our work establishes a systematic matrix calculus that bridges high-performance classical numerics and fault-tolerant quantum algorithms. It should be noted that CBMD inherits standard LCU overheads, and requires the target function to have a bounded growth order on the real axis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.10267) | 2026-11-09
