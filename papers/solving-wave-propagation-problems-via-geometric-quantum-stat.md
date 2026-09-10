---
title: "Solving wave propagation problems via geometric quantum state preparation on dispersion manifolds"
date: "2026-09-10"
updated: "2026-09-10"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.10282"
summary: "arXiv:2609.10282v1 Announce Type: new Abstract: We present a quantum algorithm for solving partial differential equations through a linear-system formulation, focusing on wave propagation problems des"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

arXiv:2609.10282v1 Announce Type: new Abstract: We present a quantum algorithm for solving partial differential equations through a linear-system formulation, focusing on wave propagation problems described by the discretized Helmholtz equation in frequency domain. Although quantum linear-system solvers offer exponential compression of the system degrees of freedom, their runtime complexity is generally governed by the condition number of the discretized operator. Exploiting the analytic structure of the differential operator can provide an alternative to explicit matrix inversion, as illustrated for the screened Poisson equation through an explicit quantum circuit. For the Helmholtz equation, however, the inverse operator becomes singular on the dispersion surface k^2=omega^2/c^2, rendering direct Fourier-space state-preparation methods exponentially inefficient. We address this challenge by directly preparing quantum states supported on the resonant manifold and encoding source locations through Fourier phases. The resulting algorithm eliminates the exponentially large overhead associated with post-selection on the resonant manifold, yielding a success probability that depends linearly on the number of sources and is independent of the computational domain size. More generally, our approach applies to hyperbolic differential equations whose Fourier-space solutions possess singular support on dispersion manifolds, recasting their solution as a problem of geometric quantum state preparation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.10282) | 2026-09-10
