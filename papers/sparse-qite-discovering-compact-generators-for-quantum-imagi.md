---
title: "Sparse-QITE: Discovering Compact Generators for Quantum Imaginary-Time Evolution via Regularization Methods"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.20791"
summary: "arXiv:2610.20791v1 Announce Type: new Abstract: Quantum imaginary-time evolution (QITE) provides a systematic route to ground-state preparation, but its cost grows rapidly with the locality D of the u"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.20791v1 Announce Type: new Abstract: Quantum imaginary-time evolution (QITE) provides a systematic route to ground-state preparation, but its cost grows rapidly with the locality D of the unitary approximation, for which the local Pauli basis scales as 4^D. We introduce Sparse-QITE, a regularized formulation that promotes compact generators, reducing the number of quantum operations and yielding circuits with fewer gates and lower depth. We derive rigorous bounds on the sparsification error and benchmark the method in one-dimensional transverse-field Ising and antiferromagnetic Heisenberg models. Sparse-QITE exhibits a controllable sparsity--accuracy trade-off while retaining strong compression even in the high-accuracy regime. In scalability experiments with respect to D, the active support grows much more slowly than in standard QITE and, in several regimes, approximately saturates over the domain sizes studied. After circuit construction and transpilation, some of the largest-domain cases require only about 1% of the standard-QITE gate count while maintaining high accuracy. We further introduce adaptive and active-discovery variants: the former selects the regularization strength dynamically during the evolution, while the latter reduces the number of Pauli expectation values that need to be evaluated and, consequently, the measurement requirements. These results establish sparsity-promoting regularization as a route toward more resource-efficient QITE. More broadly, these results suggest that sparsity-promoting regularization may also benefit variational quantum algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.20791) | 2026-10-16
