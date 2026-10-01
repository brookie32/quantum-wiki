---
title: "Exact Diagonal Completion on Reachable Subspaces: Application to QAOA Placement"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38734"
summary: "arXiv:2609.38734v1 Announce Type: new Abstract: Unused encoding states offer opportunities to simplify quantum circuits. For algorithms restricted to reachable subspaces, unspecified diagonal-operator"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38734v1 Announce Type: new Abstract: Unused encoding states offer opportunities to simplify quantum circuits. For algorithms restricted to reachable subspaces, unspecified diagonal-operator entries can be optimized without changing ideal computation. We investigate exact diagonal completion for the quantum approximate optimization algorithm (QAOA) applied to placement, using permutation-preserving register swaps. We construct exact Manhattan-distance operators through weighted-ell_1 optimization of Walsh coefficients and a sparse recurrence requiring O(sqrt{m}) terms on balanced rectangles, avoiding O(m^4) dense constraint storage. Across 160 geometries, weighted-ell_1 completion reduces controlled-NOT (CX) counts relative to four alternative extensions in all 96 cases with unused binary codes under Gray-code synthesis. On an independently specified 60-case cohort, median reductions relative to virtual-coordinate extension are 28.0%, 53.9%, and 21.6% at six, nine, and twelve sites. Under generic diagonal synthesis, reductions decrease to 10.9%, 1.3%, and 0.7%, demonstrating compiler dependence. Additional ancillas reduce mixer serialization, but token circuits remain deeper than one-hot baselines. Ideal placement simulations show baseline-dependent solution quality, with classical search performing better. OpenROAD integration takes 72 QAOA and 216 classical placements across six RTL designs through clock-tree synthesis and global routing with zero overflow. Completion improves phase construction; no end-to-end advantage is established.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38734) | 2026-10-01
