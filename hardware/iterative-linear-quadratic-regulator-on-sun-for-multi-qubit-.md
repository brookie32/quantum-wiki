---
title: "Iterative linear quadratic regulator on SU(N) for multi-qubit gate synthesis"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.03656"
summary: "arXiv:2608.03656v1 Announce Type: new Abstract: In quantum optimal control theory, gradient-based trajectory optimization techniques have proven versatile in designing multi-qubit quantum gates. Furth"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2608.03656v1 Announce Type: new Abstract: In quantum optimal control theory, gradient-based trajectory optimization techniques have proven versatile in designing multi-qubit quantum gates. Furthermore, incorporating the underlying Lie-group structure can accelerate the optimization process. In this work, we adapt the Lie-group formulation of the iterative linear quadratic regulator (iLQR) to the special unitary group SU(N) and apply it to quantum gate synthesis, systematically comparing it against the standard Euclidean iLQR formulation across multiple two- to five-qubit gates. We find that in the idealized, unconstrained setting, where all Lie-algebra basis elements are available as drive Hamiltonian terms, the Lie-group formulation converges faster than the Euclidean iLQR formulation. If drive terms are constrained to 2-local Hamiltonian terms, the Lie-group variant converges faster in early optimization iterations, but exhibits greater sensitivity to initialization and a stronger tendency towards local minima. These results demonstrate that incorporating Lie-group geometry into iLQR substantially improves convergence and highlight important next steps for improvements in constrained control settings.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.03656) | 2026-08-05
