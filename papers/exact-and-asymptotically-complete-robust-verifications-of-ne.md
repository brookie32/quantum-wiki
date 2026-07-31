---
title: "Exact and Asymptotically Complete Robust Verifications of Neural Networks via Ising Solvers"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.00408"
summary: "arXiv:2603.00408v3 Announce Type: replace-cross Abstract: We present an Ising-compatible framework for formal neural-network robustness verification under bounded input perturbations. For piecewise-li"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2603.00408v3 Announce Type: replace-cross Abstract: We present an Ising-compatible framework for formal neural-network robustness verification under bounded input perturbations. For piecewise-linear activations, the Exact Logarithmic PWL Model (Log-PWL) provides an exact, sound, and complete formulation with a state-optimal logarithmic encoding, reducing the binary variables per neuron from linear to information-theoretically minimal logarithmic complexity. For general bounded element-wise activations, the Asymptotic Step-Envelope Model (Step-Env) uses sound piecewise-constant envelopes whose lower and upper neuron states remain decision variables coupled to a common adversarial input. We prove that its globally optimized output bounds converge uniformly to the true network extrema as the segment width vanishes, yielding asymptotic completeness of verification. We further develop a hybrid Benders solver. Interval pruning, certificate transfer for pruned networks, and layerwise classical--Ising partitioning further reduce spin requirements. Experiments show exact certification fidelity for piecewise-linear networks and near-reference accuracy for sigmoid networks with compact spin budgets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.00408) | 2026-07-31
