---
title: "Block-Wise Variational Quantum Algorithms for PDEs with Interface Penalty Constraints"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.36710"
summary: "arXiv:2609.36710v1 Announce Type: new Abstract: Global variational quantum algorithm (VQA) frameworks for solving partial differential equations (PDEs) often rely on a single expressive ansatz over a "
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.36710v1 Announce Type: new Abstract: Global variational quantum algorithm (VQA) frameworks for solving partial differential equations (PDEs) often rely on a single expressive ansatz over a uniform grid, which becomes structurally inefficient when solutions exhibit spatially heterogeneous complexity such as localized singularities or thin boundary layers. A localized nonsmooth feature can degrade the convergence of the entire global quantum representation, imposing unnecessary circuit depth and amplifying the risk of vanishing gradients in barren plateaus. To overcome this limitation, we propose a block-wise VQA framework for PDEs characterized by spatially heterogeneous solution complexity. The computational domain is decomposed into locally represented quantum subproblems, where grid budgets and ansatz families are dynamically assigned based on a computable difficulty indicator. Artificial block interfaces are coupled through unified jump penalties for state values, derivatives, and physical fluxes, while adaptive reblocking tracks moving rough regions to maintain local accuracy without excessive global qubit overhead. The error analysis rigorously separates spatial discretization, ansatz expressivity, optimization convergence, finite-shot sampling noise, transfer errors from reblocking, and interface-coupling contributions. Reproducible residual-based simulations on representative elliptic, advection--diffusion, and Burgers problems demonstrate lower approximation errors and reduced peak local circuit width compared to global VQA approaches. These results substantiate block-wise quantum resource localization, confirming that high-fidelity PDE solutions can be achieved on near-term quantum devices without requiring a single globally expressive ansatz.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.36710) | 2026-09-30
