---
title: "Computationally Efficient Optimization of Per-Qubit Clifford Deformation for Non-uniform Biased Noise"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17870"
summary: "arXiv:2608.17870v1 Announce Type: new Abstract: In fault-tolerant quantum computing systems with biased noise, Clifford deformation can substantially reduce the logical error rate (LER) without additi"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17870v1 Announce Type: new Abstract: In fault-tolerant quantum computing systems with biased noise, Clifford deformation can substantially reduce the logical error rate (LER) without additional physical hardware overhead, such as extra qubits, syndrome extraction rounds, or code distance. Although Google Willow calibration data shows that 43% of qubits exhibit strong X/Z bias, existing calibration-aware deformation techniques remain impractical: (1) global searches over the 6^n deformation choices rely on computing-intensive simulations, and (2) local heuristics often underperform undeformed baselines. We present Chameleon, a fast, high-performance, and code-agnostic Clifford deformation compiler. We utilize our approximation to tackle a deformation problem based on an analytical bound on the LER. By minimizing this surrogate, Chameleon finds an optimized deformation that empirically reduces the LER with substantially lower computational overhead. In our evaluation, using calibration models derived from real superconducting devices, Chameleon demonstrates that improvements in our surrogate are strongly correlated with actual LER reductions, with an average rank correlation of rho=0.8 and rho=0.89-0.94 on the most strongly biased system. It also reduces classical computational time from 1.2 days to 3.1 minutes for the BB72 code. Chameleon achieves maximum LER reductions of 19% (13% on average) for surface codes, 16% (7%) for color codes, and 10% (4%) for bivariate bicycle codes relative to competing baselines. The maximum gains for all code families are observed on the most strongly biased system.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17870) | 2026-08-19
