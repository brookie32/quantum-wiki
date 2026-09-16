---
title: "Utility-Based Path Selection and Configuration in Quantum Networks via Layered Shortest Paths"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16198"
summary: "arXiv:2609.16198v1 Announce Type: new Abstract: A path in a quantum network is a chain of repeaters that distributes entanglement between two users. Selecting a path requires balancing the rate and qu"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16198v1 Announce Type: new Abstract: A path in a quantum network is a chain of repeaters that distributes entanglement between two users. Selecting a path requires balancing the rate and quality (e.g., fidelity) of the delivered entanglement, but these quantities, unlike standard routing metrics, compose non-additively. The problem is compounded by link-level configuration choices (e.g., distillation rounds or emitter brightness tuning), each trading rate against fidelity, so that a path's performance depends jointly on its route and its per-link settings. We cast this joint path selection and configuration problem as a shortest path computation on a layered graph whose layers track discretized end-to-end fidelity. A single run returns the full rate fidelity Pareto frontier, from which the path maximizing any nondecreasing utility function of rate and fidelity can be selected. We prove that for certain utility functions (including the secret key rate of BB84), the method is a fully polynomial time approximation scheme, returning a near-optimal path within a specified tolerance. We further characterize exactly when cheaper scalarization-based routing suffices: it is optimal for utility functions with convex fidelity profiles, but can be arbitrarily suboptimal otherwise (e.g., for step-like, sigmoidal utilities), whereas the layered method remains reliable in all cases.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16198) | 2026-09-16
