---
title: "Classical Tensor Network and Quantum Fourier Transform Approaches for Large-Scale Carr-Madan Option Pricing"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28435"
summary: "arXiv:2607.28435v1 Announce Type: new Abstract: Fourier-based methods are among the most widely used techniques for pricing European options when the characteristic function of the underlying asset pr"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.28435v1 Announce Type: new Abstract: Fourier-based methods are among the most widely used techniques for pricing European options when the characteristic function of the underlying asset process is available. Their applicability to increasingly fine discretizations, however, is limited by the rapidly growing memory requirements of classical Fourier transforms, which become a computational bottleneck for large-scale pricing problems. In this work, we overcome this limitation by reformulating the Carr-Madan pricing framework using tensor networks. Specifically, we employ the Superfast Fourier Transform (SFFT), a compressed Tensor Train representation of the Quantum Fourier Transform (QFT), and apply it directly to tensorized option pricing without ever explicitly constructing exponentially large vectors or Fourier operators. This formulation also enables a direct comparison between the classical tensor network algorithm and its quantum counterpart through QFT-based option pricing on quantum simulators and quantum hardware. Numerical experiments for European call options demonstrate that the proposed SFFT method maintains pricing accuracy while substantially reducing memory requirements and achieving subexponential computational scaling compared with conventional FFT-based pricing. The accompanying quantum simulations and hardware executions enable a direct comparison between the classical tensor network formulation and its QFT-based quantum counterpart, showing that both approaches avoid the exponential scaling of conventional Fourier implementations and provide complementary perspectives on large-scale option pricing. Together, these results establish a unified framework connecting classical Fourier pricing, tensor network algorithms, and quantum computing approaches, demonstrating how tensorized Fourier methods can provide scalable alternatives for high-dimensional financial computations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28435) | 2026-07-31
