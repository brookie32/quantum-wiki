---
title: "NEMORA: Neural Equivariant Multipole Operators for Long-Range Atomistic Learning"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.10776"
summary: "arXiv:2610.10776v1 Announce Type: cross Abstract: Equivariant graph neural networks have emerged as foundational architectures for machine-learned interatomic potentials, approaching quantum-chemical "
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.10776v1 Announce Type: cross Abstract: Equivariant graph neural networks have emerged as foundational architectures for machine-learned interatomic potentials, approaching quantum-chemical accuracy at a fraction of the computational cost. These models describe local atomic environments accurately, but finite spatial cutoffs truncate long-range information flow, and stacking message-passing layers can lead to over-smoothing and over-squashing. Existing long-range extensions either prescribe a fixed analytical propagation kernel, restrict long-range communication to scalars or degree-preserving channels, are only approximately equivariant, or incur super-linear computational cost. Combining learnable long-range equivariant transport with multiscale many-body expressivity and efficient scaling for larger systems remains a central challenge. We introduce Neural Equivariant Multipole Operators (NEMORA), a neural equivariant extension of the Fast Multipole Method (FMM) for learning long-range tensorial representations. NEMORA generalizes the FMM's analytical multipole expansion and translation operators to learned equivariant counterparts on an adaptive spatial hierarchy. Its operators couple angular degrees and form many-body interactions across length scales, retaining the FMM's hierarchical organization and analytical radial factors as physical inductive biases while learning data-dependent long-range couplings. NEMORA evaluates in linear time and memory complexity, allowing it to treat larger systems than other long-range methods reaching hundreds of thousands of atoms, and it augments both symmetry-constrained and unconstrained short-range backbones. On non-local benchmarks, it reduces force and energy errors relative to the short-range backbones by over an order of magnitude and up to three orders of magnitude, respectively, which is better than or competitive with existing long-range extensions in accuracy.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.10776) | 2026-10-09
