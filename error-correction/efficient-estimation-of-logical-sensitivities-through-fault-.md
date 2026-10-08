---
title: "Efficient Estimation of Logical Sensitivities Through Fault-Counting"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10531"
summary: "arXiv:2610.10531v1 Announce Type: new Abstract: Quantum error-correcting circuits are affected by multiple physical noise mechanisms, whose contributions to logical failure must be understood to evalu"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10531v1 Announce Type: new Abstract: Quantum error-correcting circuits are affected by multiple physical noise mechanisms, whose contributions to logical failure must be understood to evaluate code performance and guide improvements in hardware. The individual error budget contributions for an error type i can be characterized by its logical sensitivity nu_i = frac{partial p_L}{partial p_i}, which measures the response of the logical error rate p_L to each physical noise parameter p_i. Normally, nu_i is measured using linear fits such as finite differences, where p_L is measured at two or more values of p_i to calculate partial derivatives. In this paper, we develop a differentiable estimator to obtain all components of nabla_{mathbf p}p_L simultaneously from a single Monte Carlo data set at one noise configuration, using information about the underlying fault configurations. In surface code simulations with circuit-level noise, the estimator agrees with conventional finite differences while requiring one to two orders of magnitude fewer shots to achieve the same variance. We apply this technique to quantify error budgets, resolve sensitivities at the individual qubit level, and infer effective code distance. Finally, we incorporate the sensitivities into Newton root finding to locate and trace threshold contours in multidimensional noise models. These results provide an efficient method for extracting and applying logical sensitivity information from standard quantum error correction simulations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10531) | 2026-10-08
