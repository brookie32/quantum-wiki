---
title: "Schrodingerization for quantum linear systems problems"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25660"
summary: "arXiv:2609.25660v1 Announce Type: new Abstract: We develop a Schrodingerization algorithm for quantum linear systems problems in two higher dimensions. The earlier LC-Schrodingerization approach repre"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25660v1 Announce Type: new Abstract: We develop a Schrodingerization algorithm for quantum linear systems problems in two higher dimensions. The earlier LC-Schrodingerization approach represents the solution as a time integral of a homogeneous convection response and implements this integral by a linear combination of unitaries (LCU) over evolution times. We instead use Duhamel's principle to incorporate the integral into an inhomogeneous convection equation with zero initial data. Fourier projection in the convection variable and Schrodingerization in a second auxiliary variable then realize the solution without the separate LCU step. A joint choice of the kernel and recovery procedure gives an evolution time independent of the target accuracy, a uniformly bounded L^2 kernel normalization, and accurate recovery on a fixed interval. We establish the periodization and discretization bounds and analyze the interval recovery probability. With block preconditioning, we retain a single logarithmic precision factor and obtain linear condition-number dependence without variable-time amplitude amplification. Under exact oracle access and given a valid constant-factor solution-norm estimate, the algorithm uses mathcal O(kappa_Alog(1/arepsilon)) queries to each original input oracle, with constant success probability and ell^2 state error at most arepsilon. The matrix-query bound matches the standard worst-case scaling when the supplied norm bounds are tight. UnitaryLab simulations on positive-definite and indefinite systems demonstrate the solution accuracy and probability gain from interval recovery.



## Related
- [[linear-combination-of-schrodingerization-for-quantum-linear-|Linear combination of Schrodingerization for quantum linear systems with optimal matrix-query complexity]]
- [[solving-wave-propagation-problems-via-geometric-quantum-stat|Solving wave propagation problems via geometric quantum state preparation on dispersion manifolds]]
- [[a-qsvt-based-quantum-jacobi-algorithm-for-linear-systems-wit|A QSVT-Based Quantum Jacobi Algorithm for Linear Systems with Application to the Poisson Equation]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25660) | 2026-09-23
