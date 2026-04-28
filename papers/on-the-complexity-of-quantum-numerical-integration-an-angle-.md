---
title: "On the complexity of quantum numerical integration: an angle-structure characterization"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.24289"
summary: "arXiv:2604.24289v1 Announce Type: new Abstract: We study numerical integration on [0,1] by quantum amplitude estimation (QAE), focusing on the cost of constructing the amplitude oracle. Although QAE i"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.24289v1 Announce Type: new Abstract: We study numerical integration on [0,1] by quantum amplitude estimation (QAE), focusing on the cost of constructing the amplitude oracle. Although QAE improves the statistical component of the integration error, this advantage is relevant only when the integrand has low encoding complexity. We introduce a hierarchy of grid function classes G_n^{(d)}, defined by requiring the angle map Theta_g:{0,1}^no[0,pi] to be multilinear of degree at most d. Membership is classically checkable in O(n2^n) time by the Walsh--Hadamard transform. For ginG_n^{(d)}, the encoding operator factorises into sum_{k=0}^dinom{n}{k} multi-controlled R_Y gates, interpolating between an affine O(n) regime and the generic exponential regime. Combining this structure with classical discretisation estimates for gin C^alpha[0,1], we obtain a depth-versus-accuracy trade-off: gate count O((log(1/arepsilon))^darepsilon^{-1}) suffices to achieve arepsilon-accuracy with constant probability. For d=1 this becomes O(arepsilon^{-1}log(1/arepsilon)), improving over classical Monte Carlo for every alphage1. We also prove an unconditional separation: G_n^{(1)} contains functions of Sobolev regularity s<1/2 for which the quantum oracle cost is O(1/arepsilon), whereas classical deterministic or randomised quadrature requires Omega(arepsilon^{-1/s}) evaluations. These results identify explicit integrand classes for which the full cost of QAE-based integration, including state preparation, is asymptotically better than classical methods. Experiments on SpinQ Triangulum and IBM Kingston illustrate the hierarchy at n=2: circuits inside G_n^{(d)} run successfully, while those exceeding the Triangulum coherence budget fail as predicted.



## Related
- [[a-unified-quantum-computing-quantum-monte-carlo-framework-th|A unified quantum computing quantum Monte Carlo framework through structured state preparation]]
- [[constant-factor-analysis-of-optimal-quantum-linear-solvers-i|Constant Factor Analysis of Optimal Quantum Linear Solvers in Practice]]
- [[quantum-algorithm-for-solving-high-dimensional-linear-stocha|Quantum algorithm for solving high-dimensional linear stochastic differential equations via amplitude encoding of the noise term]]
- [[new-aspects-of-quantum-topological-data-analysis-betti-numbe|New aspects of quantum topological data analysis: Betti number estimation, and testing and tracking of homology and cohomology classes]]
- [[application-of-a-quantum-amplitude-redistribution-algorithm-|Application of a Quantum Amplitude Redistribution Algorithm to the Data Filtering Problem]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.24289) | 2026-04-28
