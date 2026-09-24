---
title: "From Trainability Diagnostics to Optimization Claims: Boundaries and Controls in Variational Quantum Optimization"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.21243"
summary: "arXiv:2609.21243v1 Announce Type: new Abstract: Barren plateau diagnostics characterize whether gradient signal remains available for training, but surviving signal need not translate into successful "
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21243v1 Announce Type: new Abstract: Barren plateau diagnostics characterize whether gradient signal remains available for training, but surviving signal need not translate into successful optimization. We study this trainability--optimization gap at the level of optimizer steps. Treating coefficient-weighted Hamiltonian-term gradients as task-like components, we introduce step-level diagnostics and derive an exact bridge between signed termwise organization, directional activity, and first-order descent. Resolving this bridge into standard first-order geometry shows that the apparent organization--activity factors are not independent optimization axes and that, at fixed state and update norm, the raw gradient maximizes first-order descent of the summed objective. We compare vanilla gradient descent, a deterministic Hamiltonian-term PCGrad variant, and probe-gated LSO-PCGrad on transverse-field Ising model instances with hardware-efficient and Hamiltonian variational ansatzes, together with matched controls for update norm and probe budget. Blind projection can improve an organization diagnostic while worsening final energy and first-order predictability. After conditioning on standard first-order geometry, residual term-space composition shows no reproducible material incremental association with realized descent, while optimizer-relative update norm shows positive material associations in some settings without cross-regime reproducibility. Matched controls provide no resolved final-energy benefit attributable to the projected direction, and the improvement of LSO-PCGrad is more consistent with probe-based search and step-norm adaptation than with Hamiltonian-term projection itself. These results show that gradient-structure diagnostics can characterize trainability and update geometry without serving as standalone evidence of optimization benefit, which requires controls matched on update norm and search budget.



## Related
- [[from-barren-plateaus-to-spsa-optimization-in-variational-qua|From Barren Plateaus to SPSA Optimization in Variational Quantum Eigensolvers]]
- [[one-coordinate-at-a-time-convergence-guarantees-for-rotosolv|One Coordinate at a Time: Convergence Guarantees for Rotosolve in Variational Quantum Algorithms]]
- [[on-relationship-between-circuit-depth-and-trainability-of-vq|On Relationship Between Circuit Depth and Trainability of VQAs]]
- [[a-representation-theoretic-framework-for-characterizing-barr|A Representation-Theoretic Framework for Characterizing Barren Plateaus]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.21243) | 2026-09-21
