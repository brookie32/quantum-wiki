---
title: "Why Multi-Layer Message Passing Works: Completeness Theory for Graph Neural Network Interatomic Potentials"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.00528"
summary: "arXiv:2609.00528v2 Announce Type: replace-cross Abstract: We prove that the Hypergraph Neural Network, an invariant architecture with 3-body message passing, is a universal approximator for potential "
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.00528v2 Announce Type: replace-cross Abstract: We prove that the Hypergraph Neural Network, an invariant architecture with 3-body message passing, is a universal approximator for potential energy surfaces. Our main contribution is a multi-layer completeness theory. We show that L layers of message passing on sparse, cutoff-based graphs achieve the same representational power as having access to the full L-hop neighborhood, provided the configurations are generic, satisfy an overlap condition and a connectivity condition. This provides the first rigorous justification for the common practice of using multi-layer message passing with a per-layer cutoff smaller than the physical interaction range, the setting used by virtually all practical graph neural network based machine-learned interatomic potentials. As immediate consequences, we show that both DPA3 and CHGNet architectures inherit universal approximation.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.00528) | 2026-09-03
