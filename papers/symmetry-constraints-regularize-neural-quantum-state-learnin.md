---
title: "Symmetry Constraints Regularize Neural Quantum State Learning"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08798"
summary: "arXiv:2608.08798v1 Announce Type: new Abstract: Neural quantum states (NQS) offer highly expressive variational wavefunctions, but their optimization is frequently bottlenecked by redundant parameters"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08798v1 Announce Type: new Abstract: Neural quantum states (NQS) offer highly expressive variational wavefunctions, but their optimization is frequently bottlenecked by redundant parameters and poorly conditioned landscapes. We demonstrate that embedding Hamiltonian symmetries directly into the variational parameterization geometrically regularizes this learning problem. For Boltzmann-family NQS, we enforce symmetries by tying local Pauli-Z generators along physical geometric orbits, analytically collapsing the trainable coefficient space prior to optimization. To quantify the resulting optimization geometry, we introduce a geometric metric built on the Jacobian and Hessian of the optimization landscape. This framework evaluates the fraction of the physically accessible state space that corresponds to high-quality, low-energy solutions. Evaluating our approach on transverse-field Ising (TFIM) and XXZ spin chains shows that symmetry compilation excises the vast majority of parameters while maintaining ground-state accuracy within the resolution of the reported benchmarks. In large TFIM systems, strong spatial constraints compress thousands of parameters down to tens, delivering substantial runtime accelerations. Our geometric diagnostics indicate that symmetry produces a more favorable target-aware geometry by concentrating the reachable state space around low-energy solutions while retaining broad target basins. Together, our results indicate that symmetry compilation concentrates the expressive power of NQS on states relevant to the target problem, thereby reducing model size and training cost without sacrificing accuracy.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08798) | 2026-08-11
