---
title: "Implicit Differentiation for Measurement-Efficient Bilevel Quantum-Classical Optimization"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.07717"
summary: "arXiv:2608.07717v1 Announce Type: new Abstract: Quantum optimization has shown promising results for quadratic unconstrained binary optimization (QUBO) problems. Real-world applications, however, ofte"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.07717v1 Announce Type: new Abstract: Quantum optimization has shown promising results for quadratic unconstrained binary optimization (QUBO) problems. Real-world applications, however, often involve polynomial coefficients that depend on tunable external factors - such as demand forecasts or risk preferences - giving rise to bilevel optimization structures. We show how variational quantum algorithms (VQAs) can efficiently handle such parametric problems, making three contributions. First, we propose a bilevel optimization model for diagonal cost Hamiltonians where coefficients depend on a tunable outer parameter: an outer loop adjusts this parameter - reshaping the cost landscape - while an inner VQA optimizes circuit variables. Second, since derivative-free probing methods incur a multiplicative overhead when each outer evaluation requires a complete inner solve, we develop correlator-reuse implicit differentiation (CR-ID), which obtains outer gradients by reusing quantum measurements already collected during inner energy estimation, requiring essentially no additional circuit executions. Experiments across three coefficient families show that CR-ID consistently improves budget-normalized efficiency by ~4% in 1D and over 14% in multi-dimensional settings, showing a significant performance advantage compared to finite-difference methods. Third, we show that this property is architecture-dependent: VQE admits exact reuse gradients, whereas QAOA introduces a state-dependent term that creates a cost-bias trade-off.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.07717) | 2026-08-11
