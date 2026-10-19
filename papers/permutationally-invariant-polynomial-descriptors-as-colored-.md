---
title: "Permutationally Invariant Polynomial Descriptors as Colored Multigraphs"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.23034"
summary: "arXiv:2610.23034v1 Announce Type: new Abstract: The combinatorial explosion in monomial counts limits the extension of global permutationally invariant polynomial (PIP) potential energy surfaces to la"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23034v1 Announce Type: new Abstract: The combinatorial explosion in monomial counts limits the extension of global permutationally invariant polynomial (PIP) potential energy surfaces to larger molecular systems. We use graph-theoretic language to reformulate PIPs as colored multigraphs and develop a series of theoretical and computational tools. First, we introduce an offline PIP generation algorithm whose cost has an upper bound independent of atom count for a fixed degree cutoff and number of element types. Second, we introduce a new online PIP evaluation algorithm, termed tensor-network descent. For the full PIP set through degree d in a system of M atoms, the evaluation complexity for 1le dle14 is O!left(f(d)M^{leftlfloor(sqrt{1+8d}+1)/2rightrfloor}right). At the commonly used cutoff of d=5, the online evaluation complexity decreases from the M^{10} scaling of conventional explicit term-by-term computation to M^3. Numerical tests using the full PIP set through degree 5 show that our method achieves speedups of several orders of magnitude on most MD17 systems and remains computationally affordable for systems containing more than one thousand atoms. The method has a native tensor form, supports automatic differentiation, and provides a unified theoretical construction of four classes of PIP descriptors defined consistently across systems---global, atom-centered, bond-centered, and cluster-centered---establishing a representation and computational foundation for PIP potentials for large systems and for transfer across systems. Together, these results show that PIPs are neither inherently restricted to small systems nor intrinsically nontransferable.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.23034) | 2026-10-19
