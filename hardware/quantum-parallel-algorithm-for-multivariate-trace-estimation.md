---
title: "Quantum Parallel Algorithm for Multivariate Trace Estimation with Applications"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24147"
summary: "arXiv:2611.24147v1 Announce Type: new Abstract: Estimating multivariate traces Tr(A1A2......Ak) is a fundamental task arising across diverse fields. In this paper, We develop a quantum algorithm for t"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24147v1 Announce Type: new Abstract: Estimating multivariate traces Tr(A1A2......Ak) is a fundamental task arising across diverse fields. In this paper, We develop a quantum algorithm for this problem tailored to near-term quantum devices. We access matrices by preparing their vectorized states. This access mode yields a tensor-network representation of the multivariate trace, which in turn guides the design of a parallel algorithm. The resulting circuit has depth dominated solely by that of the input oracle and independent of the number of matrices k, at the cost of a qubit count scaling as {Theta}(k)-a trade-off between circuit depth and circuit size. Moreover, the circuit exhibits a simple modular structure that allows explicit distribution over O(k) devices. We further establish efficient preparation circuits for a broad range of matrix classes, demonstrating the wide applicability of our approach. we present two applications: spectral sum estimation and a quantum implementation of the classical Lanczos method. Both reduce the target problem to sums of multivariate traces, thereby avoiding the construction of matrix polynomial transformations and achieving two levels of parallelism. For certain matrix classes, the resulting algorithms reduce circuit depth by a factor equal to the degree of the approximating polynomial. The shallow circuit depth and distributed implementation make our algorithms particularly suitable for near-term devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24147) | 2026-11-19
