---
title: "Compile-once operation graphs for reusable continuous unitary transformations"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.14831"
summary: "arXiv:2609.14831v1 Announce Type: new Abstract: Continuous unitary transformations repeatedly evaluate the same operator algebra as the coefficients of a Hamiltonian and its observables evolve. We com"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14831v1 Announce Type: new Abstract: Continuous unitary transformations repeatedly evaluate the same operator algebra as the coefficients of a Hamiltonian and its observables evolve. We compile these algebraic relationships once into a numerical operation graph that can be saved and reused for new coefficient sets, additional operators, derivatives, and forward and reverse calculations on CPUs and GPUs. Reuse is demonstrated by applying the same compiled graph to hydrogen and deuterium parameterizations of a reduced molecular model without regenerating the operator equations. The main computational challenge is construction: generated many-body algebra can contain hundreds of millions of contributions before numerical propagation begins. We address this by determining the required storage in advance and writing contributions directly into the final disk-backed representation. In a deliberately large diagnostic-enabled stress test containing more than 350 million generated contributions, peak host memory remains only about 7% above the final stored size. Cross-checks show that CPU and GPU implementations, forward and reverse operations, and repeated loading of the compiled graph reproduce the tested operations to numerical precision. This compile-once representation separates expensive operator-algebra generation from the numerical transformations that reuse it.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.14831) | 2026-09-15
