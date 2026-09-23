---
title: "Continuous perception and adaptive metrics for scalable structure refinement"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.25849"
summary: "arXiv:2609.25849v1 Announce Type: new Abstract: We present a geometry-refinement workflow that adapts to the cost of an energy--gradient evaluation and the reliability of molecular topology. An initia"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25849v1 Announce Type: new Abstract: We present a geometry-refinement workflow that adapts to the cost of an energy--gradient evaluation and the reliability of molecular topology. An initial Cartesian calculation and continuous bonding diagnostics determine whether to begin in projected Cartesian coordinates or in chemically adapted internal coordinates. Chemical perception generates local redundant measurements; sparse rank and conditioning tests combine them into nonredundant, symmetry-adapted coordinates; and a common optimizer uses the selected representation with resident or external calculators. For inexpensive gradients, the projected Cartesian route limits coordinate overhead; a single monitored internal-coordinate step can then provide chemical interpretability. When gradients are costly and topology is certified, symmetry-adapted internal coordinates reduce expensive energy--gradient calls. A quadraticized map improves localized anharmonic cases, while mixed Cartesian/internal charts cover uncertain or complex topologies. Local sparse operators and resident force-field and tight-binding calculators extend both routes to large systems. The same Cartesian calculator contract supports multilevel energy and gradient composition. The measured coordinate pipeline and recurrent resident tight-binding update show near-linear scaling over the tested size ranges; this statement applies to those qualified components, not to arbitrary electronic-structure calculations or cold starts. For certified, directly separable internal charts, the optimizer can use chemically designed Morse or Gaussian maps to quadraticize the local step problem. The quadraticized branch uses a short geometry-local history, while delocalized charts remain unchanged. This reduces iterations in difficult minima without changing the electronic potential or coordinate chart.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.25849) | 2026-09-23
