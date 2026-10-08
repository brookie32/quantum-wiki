---
title: "Optimizing the Optimizer: Language Models Discover Faster Molecular Relaxation Algorithms"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.06577"
summary: "arXiv:2610.06577v2 Announce Type: replace Abstract: Geometry optimization is a major cost in many quantum-chemical workflows: each optimization step requires one force evaluation, and at the density-f"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.06577v2 Announce Type: replace Abstract: Geometry optimization is a major cost in many quantum-chemical workflows: each optimization step requires one force evaluation, and at the density-functional level that evaluation dominates the wall time. Research in this area has produced a broad range of optimization methods, and we ask whether a language model can improve on the best of them through autoresearch. An agent rewrites the optimizer itself to minimize force-call counts, restrained by two admission gates that reject premature stopping and improvements that do not generalize to unseen molecules. Starting from Sella, the fastest open-source optimizer available, the search produces AutoSella, a family of two optimizers. Both of them deliver consistent force-call reductions relative to Sella across held-out molecular benchmarks and potentials not used during the search. Most notably, at the r2SCAN-3c DFT level, the best variant requires only 40.2-77.2% of Sella's force calls while achieving the same energy reduction, even though agent used no DFT gradients.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.06577) | 2026-10-08
