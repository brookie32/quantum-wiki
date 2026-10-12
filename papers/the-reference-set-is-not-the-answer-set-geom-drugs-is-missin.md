---
title: "The Reference Set Is Not the Answer Set: GEOM-DRUGS Is Missing Low-Energy Conformers on Its Own Energy Surface"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.12523"
summary: "arXiv:2610.12523v1 Announce Type: new Abstract: Machine-learned conformer generators are scored on GEOM-DRUGS by proximity to a reference ensemble that standard benchmark metrics implicitly treat as g"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.12523v1 Announce Type: new Abstract: Machine-learned conformer generators are scored on GEOM-DRUGS by proximity to a reference ensemble that standard benchmark metrics implicitly treat as ground truth. We test whether that finite set is complete on the GFN2-xTB surface used to construct it. Across five public generators, settled, low-energy structures remain outside the 0.75,AA{} reference radius after removing reflections, incorrect stereochemistry, and post-relaxation connectivity changes (2.3--7.0% of submitted conformers, depending on architecture). In a targeted DFT audit, 107 of 113 chemically screened novel/reference pairs remain outside that radius after full omegaB97X-D3BJ re-optimization. A threshold-free complementary test needs no radius and no energy window at all: on 15.0% [8.0, 22.0] of molecules some generator has already found a chemically intact structure lying below the entire released ensemble. A complementary CREST search reproduces the minimum released in 65 of 69 molecules, and in 11 of them it reaches more than 0.5,kcal/mol below the complete released ensemble. Augmenting the references with conformers proposed by held-out architectures raises absolute coverage-precision for every generator tested, by 1.48--2.99 points. Together, these results show that GEOM-DRUGS precision is sensitive not only to generator quality but also to incomplete reference support.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.12523) | 2026-10-12
