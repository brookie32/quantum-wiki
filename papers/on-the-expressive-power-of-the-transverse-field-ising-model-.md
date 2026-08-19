---
title: "On the Expressive Power of the Transverse-Field Ising Model for Graph Learning"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17750"
summary: "arXiv:2608.17750v1 Announce Type: new Abstract: We study the quantum evolution induced by graph-indexed Ising Hamiltonians as a source of structural signal for graph learning. Graph automorphisms pres"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17750v1 Announce Type: new Abstract: We study the quantum evolution induced by graph-indexed Ising Hamiltonians as a source of structural signal for graph learning. Graph automorphisms preserve symmetries of the Hamiltonian, and these symmetries constrain the quantum evolution in a way that turns time-dependent local measurements into informative probes of graph structure. Leveraging this idea, we introduce QDAGer, a quantum-inspired graph-pair Transformer that injects quantum-dynamical features from time series of node occupations and connected two-point correlators directly into the attention mechanism. We apply QDAGer to learning Graph Edit Distance (GED), an NP-hard similarity measure, using either a direct permutation-invariant embedding discrepancy or an alignment-based surrogate loss. Experiments on multiple GED benchmarks under different edit cost settings show that the proposed dynamical features provide a stronger inductive bias than classical structural alternatives under the same training protocol. In addition, we report ablations where the dynamical signal is replaced by standard random-walk and heat-kernel features while keeping the architecture fixed, highlighting that the gain comes from the injected dynamics rather than model capacity alone.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17750) | 2026-08-19
